import fitz

def extract_text_from_pdf(uploaded_file):

    pages = []

    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    for page in pdf:
        pages.append(page.get_text())

    return pages