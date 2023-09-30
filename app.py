import sys

from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
load_dotenv()

query = sys.argv[1]


# loader = TextLoader('data.txt')
loader = DirectoryLoader('./collection', glob='*.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query, llm=ChatOpenAI()))