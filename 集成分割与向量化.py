import requests
import functools


def file_chunk_list():
    """读取知识文件，按空行分割为多个知识片段"""
    with open("knowledge/1.txt", encoding='utf-8') as fp:
        data = fp.read()
    chunk_list = data.split("\n\n")
    return [chunk.strip() for chunk in chunk_list if chunk.strip()]


def ollama_embedding_by_api(text):
    """调用 Ollama 的 embeddings API 生成文本嵌入"""
    try:
        res = requests.post(
            url="http://127.0.0.1:11434/api/embeddings",
            json={
                "model": "nomic-embed-text",
                "prompt": text  # 使用包裹后的文本
            }
        )
        res.raise_for_status()
        embedding = res.json()["embedding"]
        return embedding
    except Exception as e:
        print(f"嵌入失败：{e}")
        return None


def run():
    """主流程：处理所有知识片段，生成嵌入"""
    chunk_list = file_chunk_list()
    print(f"共加载 {len(chunk_list)} 个知识片段")

    for idx, chunk in enumerate(chunk_list, 1):
        print(f"\n=== 处理第 {idx} 个片段 ===")
        print(f"内容预览：{chunk[:80]}...")

        embedding = ollama_embedding_by_api(chunk)
        if embedding:
            print(f"嵌入维度：{len(embedding)}")
            # TODO：存储 embedding 和原始文本到向量数据库

    print("\n所有知识片段处理完成！")


if __name__ == "__main__":
    run()