import pandas as pd

# 读取Excel文件
df = pd.read_excel(r'D:\平台证书\服务器证书\系统提供商识别.xlsx')

# 将A列和B列的数据都转换为字符串类型
df['notify_host'] = df['notify_host'].astype(str).str.split(':').str[0]
df['top_Domain'] = df['top_Domain'].astype(str)

# 遍历A列的值，根据B列的值删除对应部分，并保存到C列
def remove_suffix(row):
    a_value = row['notify_host']
    for b_value in df['top_Domain']:
        if a_value.endswith(b_value):
            a_value = a_value[:-len(b_value)].rsplit('.',1)[-1]
    return a_value
    

df['C'] = df.apply(remove_suffix, axis=1)
a = ['notify_host','top_Domain','C']
# 保存处理后的数据到新的Excel文件
df[a].to_excel('output.xlsx',na_rep = '', index=False)
print('done')