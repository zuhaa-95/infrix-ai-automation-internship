import streamlit as st

st.title("FIR & Court Document Analyzer")
st.write("Upload an FIR or court document to get a summary and ask questions about it.")
uploaded_file = st.file_uploader("Upload your FIR/Court document (PDF or TXT)", type=["pdf", "txt"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    st.write("File name:", uploaded_file.name)
    # Extract text depending on file type
    if uploaded_file.name.endswith(".pdf"):
        import pdfplumber
        with pdfplumber.open(uploaded_file) as pdf:
            extracted_text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    extracted_text += page_text + "\n"
    else:
        extracted_text = uploaded_file.read().decode("utf-8")

    st.subheader("Extracted Text Preview")
    st.text_area("Document content", extracted_text, height=300)
    if st.button("Summarize Document"):
        with st.spinner("Analyzing document with AI..."):
            import requests
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3.2",
                    "prompt": f"Summarize this FIR/court document in simple, plain English. Include key details like parties involved, date, location, and nature of the complaint:\n\n{extracted_text}",
                    "stream": False
                }
            )
            result = response.json()
            summary = result["response"]

        st.subheader("AI Summary")
        st.write(summary)
        st.subheader("Ask a Question About This Document")
    user_question = st.text_input("Type your question here")

    if st.button("Get Answer") and user_question:
        with st.spinner("Thinking..."):
            import requests
            qa_response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3.2",
                    "prompt": f"Based on this FIR/court document, answer the question below in simple plain English.\n\nDocument:\n{extracted_text}\n\nQuestion: {user_question}\n\nAnswer:",
                    "stream": False
                }
            )
            qa_result = qa_response.json()
            answer = qa_result["response"]

        st.write("**Answer:**", answer)