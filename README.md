Citizen Policy Dashboard
***Overview

-The Citizen Policy Dashboard is an AI-powered system designed to simplify complex government policy documents for citizens.
-Government policy PDFs are often long and may contain 100,000+ tokens, which exceed the context limits of many Large Language Models (LLMs). Processing such large documents directly increases computation cost and may cause system failures.
-To solve this problem, the system uses Map-Reduce Token Compression, which reduces the size of the document while preserving important information. The compressed content is then used to generate a simplified summary and answer user questions about the policy.

**Problem Statement

PS 3 — Token Compression: The AI Legislative Analyzer
-Government policy documents are often difficult for citizens to understand because:
-They are very long and complex
-They contain technical and legal language
-They exceed the token limits of many AI models
-This project focuses on reducing token usage while preserving key policy information, enabling efficient AI-based analysis of large documents.

**Technologies Used
***Programming Language
Python – Used for implementing the core logic and system modules.

***Web Application Framework
Streamlit – Used to build the interactive dashboard interface.

***AI Model Integration
Groq API – Used to generate summaries and answer policy-related questions using Large Language Models.

***PDF Text Extraction
PyMuPDF – Extracts text from uploaded government policy PDF files.

***Token Counting
tiktoken – Calculates token counts before and after compression.

***Compression Technique
Map-Reduce Token Compression Pipeline – Used to process very large documents efficiently.

***Map-Reduce Token Compression
Policy documents can contain hundreds of pages. Sending the entire document directly to an AI model may exceed token limits.
To solve this problem, the system uses a Map-Reduce compression approach.

***Map Phase
The full document is divided into smaller chunks.
Example:
100 page document
↓
10 chunks
Each chunk = 10 pages
Each chunk is processed independently and compressed.
This ensures the document stays within token limits.

***Reduce Phase
After each chunk is compressed, the outputs are combined into a final compressed document.
Compressed Chunk 1
Compressed Chunk 2
Compressed Chunk 3
↓
Final Compressed Document
This final compressed representation retains the most important information from the original policy document.

***System Workflow

The system follows this pipeline:

User uploads policy PDF
↓
Text extraction from all pages
↓
Document divided into chunks
↓
Map phase: each chunk compressed
↓
Reduce phase: compressed chunks combined
↓
AI generates citizen-friendly summary
↓
User asks questions about the policy

***Key Features
*Upload government policy PDF documents
*Extract text from multi-page PDFs
*Compress large documents using Map-Reduce token compression
*Generate simplified summaries for citizens
*Ask questions about policies using AI
*Display token reduction metrics

Example document:

Original Tokens: 114,917
Compressed Tokens: 3,073
Token Reduction: 97.33%
This significantly reduces token usage while preserving important information.

## Installation & Running the Project
### 1. Install required dependencies
-pip install -r requirements.txt

### 2. Run the application
-streamlit run app.py

### 4. Open the application in your browser
-http://localhost:8501



Author
Sai Ram
