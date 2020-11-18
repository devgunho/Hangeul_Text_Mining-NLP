import pandas as pd

# KKMA
original = pd.read_csv(
    './dataset/패션아이템/morpheme-result_Kkma.csv', encoding="utf8")
df = original.dropna(axis=0).reset_index()
del(df['index'])
df.columns = ['text']
list = []
for sen in df['text']:
    for vocab in sen.split():
        list.append(vocab)
kkma_set = set(list)
print("KKMA len.", len(kkma_set))

ma_kkma = pd.read_csv("./dataset/패션아이템/morpheme-result_Kkma.csv").dropna()
temp = ma_kkma.values.tolist()
ma_kkma_list = []
for sentence in temp:
    temp2 = sentence[0].split()
    for vocab in temp2:
        ma_kkma_list.append(vocab)
kkma_series = pd.Series(ma_kkma_list)
kkma_counts = kkma_series.value_counts()
kkma_counts = kkma_counts.to_frame(name="KKMA")
print(kkma_counts)


# KOMORAN
original = pd.read_csv(
    './dataset/패션아이템/morpheme-result_Komoran.csv', encoding="utf8")
df = original.dropna(axis=0).reset_index()
del(df['index'])
df.columns = ['text']
list = []
for sen in df['text']:
    for vocab in sen.split():
        list.append(vocab)
komoran_set = set(list)
print("KOMORAN len.", len(komoran_set))

# MECAB
original = pd.read_csv(
    './dataset/패션아이템/morpheme-result_MeCab.csv', encoding="utf8")
df = original.dropna(axis=0).reset_index()
del(df['index'])
df.columns = ['text']
list = []
for sen in df['text']:
    for vocab in sen.split():
        list.append(vocab)
mecab_set = set(list)
print("MECAB len.", len(mecab_set))

# OKT
original = pd.read_csv(
    './dataset/패션아이템/morpheme-result_Okt.csv', encoding="utf8")
df = original.dropna(axis=0).reset_index()
del(df['index'])
df.columns = ['text']
list = []
for sen in df['text']:
    for vocab in sen.split():
        list.append(vocab)
okt_set = set(list)
print("OKT len.", len(okt_set))

# HANNANUM
original = pd.read_csv(
    './dataset/패션아이템/morpheme-result_Hannanum.csv', encoding="utf8")
df = original.dropna(axis=0).reset_index()
del(df['index'])
df.columns = ['text']
list = []
for sen in df['text']:
    for vocab in sen.split():
        list.append(vocab)
hannanum_set = set(list)
print("HANNANUM len.", len(hannanum_set))


intersection = kkma_set & komoran_set & mecab_set & okt_set & hannanum_set
print("\nIntersection len.", len(intersection))

df = pd.DataFrame(intersection)
for index, row in df.iterrows():
    print(row[0])
