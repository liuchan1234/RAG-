import requests

text = "【绿叶蔬菜（如菠菜、生菜）】保存要点：叶片易萎蔫、发黄，切口易滋生细菌，吸水后腐烂快。保存方法：先摘除黄叶，将根部浸入浅水杯（水位 1-2cm），套塑料袋扎口，放冰箱冷藏室（0-5℃），2-3 天换一次水。"

res = requests.post(
    url="http://127.0.0.1:11434/api/embeddings",
    json={
        "model": "nomic-embed-text",
        "prompt": text
    }
)

embedding_list = res.json()['embedding']

print(text)
print(len(embedding_list), embedding_list)