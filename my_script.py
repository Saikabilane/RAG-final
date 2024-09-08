import google.generativeai as genai
import chromadb
chroma_client = chromadb.PersistentClient(path="./collection")
from pypdf import PdfReader
import pdfplumber
import streamlit as st

api_key = "AIzaSyBt41MC3ZSxYlBktQH0WN_OFP45Jz7zjYs"
genai.configure(api_key = api_key)
model = genai.GenerativeModel('gemini-1.5-flash')
filePath = "./anatomy_vol_3_edited_final.pdf"

reader = PdfReader(filePath)
pages = len(reader.pages)

texts = []
ids = []
count = 1
for page in range(pages):
    text = reader.pages[page].extract_text()
    texts.append(text)
    ids.append("id"+str(count))
    count += 1

collection = chroma_client.create_collection(name="my_collection")

collection.add(
    documents = texts,
    ids=ids
)