# ai-companion
A very simple AI Companion app fuelled by OpenAI and LangChain.

Read the [blog here](https://syntaxpunk.com/blog/ai-companion).

### Installation
- Create python venv: `python3 -m venv venv`
- Activate the environment in the project folder: `source venv/bin/activate`
- Create `.env` file and add there open-ai api key like so: `OPENAI_API_KEY=you-key-here`
- Install libs needed: `pip install python-dotenv langchain openai` 
- To generate a requirements file run: `pip freeze > requirements.txt`
- To install deps from the requirements file, run: `pip install -r requirements.txt`
- To deactivate virtual env: `deactivate`

### Running
- Call the app via python `python app.py`
- Now feel free asking questions about the data provided in the collection
- Here is some example:

```text
-> Yo this is your AI companion. Type 'exit' to quit.

[you]: how many apples do I have?
[ai]: 3
[you]: what's the name of the first person on my contacts list?
[ai]: Erik Olsen
[you]: exit
``` 
