# 读取文件内容
with open("knowledge/1.txt", encoding='utf-8',mode='r') as fp:
    data = fp.read()
# 根据换行切割文件内容
chunk_list = data.split('\n\n')
chunk_list = [chunk for chunk in chunk_list if chunk]
print(len(chunk_list))
print(chunk_list[0])
