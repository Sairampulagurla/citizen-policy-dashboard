import streamlit as st
from pdf_reader import extract_text_from_pdf
from compressor import compress_text
from summarizer import generate_summary
from assistant import ask_policy_question

# Page configuration
st.set_page_config(
    page_title="Citizen Policy Dashboard",
    page_icon="📄",
    layout="wide"
)

# Custom UI styling
st.markdown("""
<style>
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
    height: 45px;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("📄 Citizen Policy Dashboard")

st.markdown("""
Upload a government policy document to:

- 📊 Analyze policy metrics  
- 🧠 Generate citizen-friendly summary  
- 💬 Ask questions about the policy  
""")

# Layout
col1, col2 = st.columns([1,2])

# Upload section
with col1:
    uploaded_file = st.file_uploader("Upload Policy PDF", type="pdf")

# Reset session when file removed
if uploaded_file is None:
    st.session_state.policy_text = None
    st.session_state.chat_history = []

# Initialize session state
if "policy_text" not in st.session_state:
    st.session_state.policy_text = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# If file uploaded
if uploaded_file:

    with col1:
        st.success("PDF uploaded successfully")

        if st.button("Analyze Policy"):

            with st.spinner("Extracting text from PDF..."):
                pages = extract_text_from_pdf(uploaded_file)

            with st.spinner("Compressing document..."):
                compressed_text, original_tokens, compressed_tokens = compress_text(pages)

            if compressed_text is None:
                st.error("Compression API failed. Please try again.")
                st.stop()

            reduction = ((original_tokens - compressed_tokens) / original_tokens) * 100

            # Show metrics
            st.subheader("📊 Document Metrics")

            m1, m2, m3 = st.columns(3)
            m1.metric("Original Tokens", original_tokens)
            m2.metric("Compressed Tokens", compressed_tokens)
            m3.metric("Reduction %", f"{round(reduction,2)}%")

            with st.spinner("Generating citizen-friendly summary..."):
                summary = generate_summary(compressed_text)

            st.session_state.policy_text = compressed_text
            st.session_state.chat_history = []

    # Summary section on right
    with col2:

        st.subheader("🧠 Policy Summary")

        if 'summary' in locals():
            st.write(summary)

# Question section
if st.session_state.policy_text:

    st.divider()
    st.subheader("💬 Ask Questions About This Policy")

    with st.form("question_form"):

        question = st.text_input("Type your question")

        submitted = st.form_submit_button("Ask")

        if submitted and question:

            answer = ask_policy_question(st.session_state.policy_text, question)

            st.session_state.chat_history.append(("User", question))
            st.session_state.chat_history.append(("AI", answer))

    # Display chat history
    for role, message in st.session_state.chat_history:

        if role == "User":
            st.markdown(f"**🧑 You:** {message}")
        else:
            st.markdown(f"**🤖 AI:** {message}")