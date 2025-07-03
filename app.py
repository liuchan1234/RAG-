import chromadb
from 集成分割与向量化 import ollama_embedding_by_api
import requests
db_path = "db/chroma_demo"
collection_name = "collection_v1"
client = chromadb.PersistentClient(path=db_path)

collection = client.get_collection(name=collection_name)
qs = '草莓怎么保存'
qs_embedding = ollama_embedding_by_api(qs)
res = collection.query(query_embeddings=[qs_embedding],n_results=2)
print(res['documents'][0][0])
print(res['documents'][0][1])
context = res['documents']

prompt = f"你是一个健康饮食专家，任务是根据参考信息回答用户问题，如果参考信息不足以回答用户问题，请回复不知道，不要去杜撰任何信息，请用中文回答。参考信息：{context}，来回答问题：{qs}"
response = requests.post(
    url="http://127.0.0.1:11434/api/generate",
    json={
        "model": "deepseek-r1:1.5b",
        "prompt": prompt,
        "stream": False
    }
)
res = response.json()['response']
print(res)