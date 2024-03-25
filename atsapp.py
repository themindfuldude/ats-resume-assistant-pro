```Python Streamlit code using Voyage embeddings and API:

import streamlit as st
import os
import voyageai
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import Anthropic

# Set up Streamlit app
st.set_page_config(page_title="Job Application Assistant", layout="wide")
st.title("Job Application Assistant")

# Initialize Claude 3.0 API
os.environ["ANTHROPIC_API_KEY"] = st.secrets["ANTHROPIC_API_KEY"]
llm = Anthropic(model="claude-v1")

# Initialize Voyage API
os.environ["VOYAGE_API_KEY"] = st.secrets["VOYAGE_API_KEY"]
vo = voyageai.Client()

# Function to process uploaded files
def process_files(resume, cover_letter, job_description):
    loader = PyPDFLoader(resume)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    # Embed the documents using Voyage API
    documents_embeddings = vo.embed(
        [doc.page_content for doc in texts], model="voyage-2", input_type="document"
    ).embeddings

    query = f"""
    Using the provided resume, cover letter, and job description, please generate:
    1. An ATS-compliant professional summary statement.
    2. An ATS-compliant cover letter.
    3. An ATS-compliant resume.
    Ensure the generated content is tailored to the target role and industry, free of errors, and adheres to best practices for modern job search documents.
    """

    # Get the embedding of the query
    query_embedding = vo.embed(
        [query], model="voyage-2", input_type="query"
    ).embeddings[0]

    # Compute the similarity and retrieve the most relevant document
    similarities = np.dot(documents_embeddings, query_embedding)
    retrieved_id = np.argmax(similarities)
    retrieved_doc = texts[retrieved_id].page_content

    # Rerank the retrieved documents using Voyage API
    documents_reranked = vo.rerank(
        query,
        [doc.page_content for doc in texts],
        model="rerank-lite-1",
        top_k=3
    )

    reranked_docs = [r.document for r in documents_reranked.results]

    chain = load_qa_chain(llm, chain_type="stuff")
    result = chain.run(input_documents=reranked_docs, question=query)

    return result

# Streamlit app layout
with st.form(key="my_form"):
    resume = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
    cover_letter = st.file_uploader("Upload your cover letter (PDF)", type=["pdf"])
    job_description = st.file_uploader("Upload the job description (PDF)", type=["pdf"])
    submit_button = st.form_submit_button(label="Generate Application Materials")

if submit_button:
    if resume and cover_letter and job_description:
        result = process_files(resume, cover_letter, job_description)
        st.markdown("## Generated Application Materials")
        st.markdown(result)
    else:
        st.warning("Please upload all required files.")
