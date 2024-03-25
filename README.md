# ATS Expert Resume, Summary and Cover Letter Assistant
My ATS Resume Assistant utilizes Claude 3.0, a Streamlit UI and Voyage Vector Embeddings and RAG retrieval, Nearest Neighbor Search and Reranking

README with package installation instructions:
# Job Application Assistant
The Job Application Assistant is a Streamlit app that helps job seekers generate ATS-optimized application materials using AI. By uploading their current resume, and a job description, users can obtain a compelling professional summary statement, a persuasive cover letter, and an updated resume tailored to the target role and optimized for applicant tracking systems (ATS) and human readers.

## Setup
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/job-application-assistant.git
   ```
2. Install the required dependencies:
   ```
   pip install streamlit langchain anthropic voyageai numpy
   ```
3. Set up your Anthropic Claude 3.0 API key:
   - Sign up for an Anthropic account and obtain your API key.
   - Create a `.streamlit/secrets.toml` file in the project directory.
   - Add the following line to the `secrets.toml` file, replacing `YOUR_API_KEY` with your actual API key:
     ```
     ANTHROPIC_API_KEY = "YOUR_API_KEY"
     ```
4. Set up your Voyage API key:
   - Sign up for a Voyage account and obtain your API key.
   - Add the following line to the `.streamlit/secrets.toml` file, replacing `YOUR_VOYAGE_API_KEY` with your actual API key:
     ```
     VOYAGE_API_KEY = "YOUR_VOYAGE_API_KEY"
     ```
## Usage
1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
2. Access the app in your web browser at `http://localhost:8501`.

3. Upload your current resume, cover letter, and the job description in PDF format.

4. Click the "Generate Application Materials" button.

5. The app will process the uploaded files and generate ATS-optimized application materials, including a professional summary statement, a cover letter, and an updated resume.

6. Review the generated materials and use them to enhance your job application.

## Troubleshooting

- If you encounter any issues, make sure you have installed all the required dependencies listed in the setup instructions.
- Ensure that your Anthropic Claude 3.0 API key and Voyage API key are valid and properly set up in the `.streamlit/secrets.toml` file.
- If the app is not loading or responding, try restarting the Streamlit server.

For any further assistance or questions, please open an issue oin this GitHub repository.

Gregory Kennedy
