import uuid
import chromadb
import requests
from 集成分割与向量化 import file_chunk_list, ollama_embedding_by_api

# 1. 初始化 Chroma 数据库（持久化存储到本地目录）
client = chromadb.PersistentClient(path="db/chroma_demo")  # 数据存到 ./db/chroma_demo 文件夹
collection = client.get_or_create_collection(name="collection_v1")  # 类似“表格”，自动创建不存在的集合
documents = []
embeddings = []
chunk_list = file_chunk_list()
for chunk in chunk_list:
    documents.append(chunk)
    embedding = ollama_embedding_by_api(chunk)
    embeddings.append(embedding)
ids = [str(uuid.uuid4()) for _ in documents]

# 2. 插入数据到 Chroma 集合
collection.add(
    ids=ids,           # 每个文档的唯一标识
    documents=documents,  # 原始文本内容
    embeddings=embeddings  # 文本对应的向量（需提前生成）
)
