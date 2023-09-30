# ai-companion
AI Companion app based on ChatGPT

### Installation
- Create python venv: `python3 -m venv venv`
- Activate the environment in the project folder: `source venv/bin/activate`
- Create `.env` file and add there open-ai api key like so: `OPENAI_API_KEY=you-key-here`
- Install libs needed: `pip install python-dotenv langchain openai` 
- To generate a requirements file run: `pip freeze > requirements.txt`
- To install deps from the requirements file, run: `pip install -r requirements.txt`
- To deactivate virtual env: `deactivate`