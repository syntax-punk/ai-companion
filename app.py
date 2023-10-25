import sys

from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

load_dotenv()

loader = DirectoryLoader('./collection', glob='*.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

def start_chattin():
  print("-> Yo this is your AI companion. Type 'exit' to quit.")
  while True:
    query = input("[you]: ").lower()
    if query == 'exit':
      break

    response = index.query(query, llm=ChatOpenAI())
    print("[ai]: " + response)


if __name__ == '__main__':
    start_chattin()
