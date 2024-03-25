# ATS Expert Resume, Summary and Cover Letter Assistant
My ATS Resume Assistant utilizes Claude 3.0, a Streamlit UI and Voyage Vector Embeddings and RAG retrieval, Nearest Neighbor Search and Reranking.

# ATS-optimized job application materials
The Job Application Assistant is a Streamlit app that helps job seekers generate ATS-optimized job application materials using AI. By uploading their current resume, and a job description, users can obtain a compelling professional summary statement, a persuasive cover letter, and an updated resume tailored to the target role and optimized for applicant tracking systems (ATS) and human readers.

## Setup
1. Install Miniconda:
   - Download the Miniconda installer for your operating system from the official website: [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
   - Run the installer and follow the installation instructions.

2. Create a new conda virtual environment:
   ```
   conda create --name ats-assistant python=3.11
   ```

3. Activate the conda virtual environment:
   ```
   conda activate ats-assistant
   ```

4. Clone the repository:
   ```
   git clone https://github.com/themindfuldude/atsresumeassistant.git
   ```

5. Navigate to the project directory:
   ```
   cd atsresumeassistant
   ```

6. Install the required dependencies:
   ```
   pip install streamlit langchain langsmith anthropic voyageai numpy
   ```

7. Set up your Anthropic Claude 3.0 API key: [Claude API Key and Installation](https://docs.anthropic.com/claude/docs/getting-access-to-claude)
   - Sign up for an Anthropic account and obtain your API key. [Claude Console Sign Up $5 in free API credits-No Credit Card Required](https://console.anthropic.com)
   - Create a `.streamlit/secrets.toml` file in the project directory.
   - Add the following line to the `secrets.toml` file, replacing `YOUR_API_KEY` with your actual API key:
     ```
     ANTHROPIC_API_KEY = "YOUR_API_KEY"
     ```

8. Set up your Voyage API key: [Voyage API Key and Installation](https://docs.voyageai.com/docs/api-key-and-installation))
   - Sign up for a Voyage account and obtain your API key. [Voyage Sign Up](https://www.voyageai.com/?ref=anthropic)
   - Add the following line to the `.streamlit/secrets.toml` file, replacing `YOUR_VOYAGE_API_KEY` with your actual API key:
     ```
     VOYAGE_API_KEY = "YOUR_VOYAGE_API_KEY"
     ```

## Usage
1. Ensure that the conda virtual environment is activated:
   ```
   conda activate ats-assistant
   ```

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

3. Access the app in your web browser at `http://localhost:8501`.

4. Upload your current resume, cover letter, and the job description in PDF format.

5. Click the "Generate Application Materials" button.

6. The app will process the uploaded files and generate ATS-optimized application materials, including a professional summary statement, a cover letter, and an updated resume.

7. Review the generated materials and use them to enhance your job application.

## Troubleshooting
- If you encounter any issues, make sure you have installed all the required dependencies listed in the setup instructions.
- Ensure that your Anthropic Claude 3.0 API key and Voyage API key are valid and properly set up in the `.streamlit/secrets.toml` file.
- If the app is not loading or responding, try restarting the Streamlit server.

For any further assistance or questions, please open an issue on this GitHub repository.

Gregory Kennedy
