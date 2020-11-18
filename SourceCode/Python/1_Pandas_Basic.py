#!/usr/bin/env python
# coding: utf-8

# # 판다스(Pandas)
# 
# 판다스(Pandas)는 파이썬 데이터 처리를 위한 라이브러리이다.

# In[1]:


import pandas as pd


# Pandas는 총 세 가지의 데이터 구조를 사용한다.
# 
# 1. 시리즈(Series)
# 2. 데이터프레임(DataFrame)
# 3. 패널(Panel)

# ### 1) 시리즈(Series)
# 
# 시리즈 클래스는 1차원 배열의 값(values)에 각 값에 대응되는 인덱스(index)를 부여할 수 있는 구조를 갖고 있다.

# In[2]:


sr = pd.Series([17000, 18000, 1000, 5000],
       index=["홍길동", "김길동", "이길동", "박길동"])
print(sr)


# In[3]:


print(sr.values)


# In[4]:


print(sr.index)


# ### 2) 데이터프레임(DataFrame)
# 
# 데이터프레임은 2차원 리스트를 매개변수로 전달한다.
# 
# 2차원이므로 행방향 인덱스(index)와 열방향 인덱스(column)가 존재한다.
# 
# 즉, 행과 열을 가지는 자료구조이다.
# 
# 시리즈가 인덱스(index)와 값(values)으로 구성된다면, 데이터프레임은 열(columns)까지 추가되어 열(columns), 인덱스(index), 값(values)으로 구성된다.

# In[5]:


values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
index = ['one', 'two', 'three']
columns = ['A', 'B', 'C']

df = pd.DataFrame(values, index=index, columns=columns)
print(df)


# In[6]:


# 인덱스 출력
print(df.index)


# In[7]:


# 열 출력
print(df.columns)


# In[8]:


# 값 출력
print(df.values)


# ### 3) 데이터프레임의 생성
# 
# 데이터프레임은 리스트(List), 시리즈(Series), 딕셔너리(dict), Numpy의 ndarrays, 또 다른 데이터프레임으로 생성할 수 있다.

# In[9]:


# 리스트로 생성하기
data = [
    ['1000', 'Steve', 90.72], 
    ['1001', 'James', 78.09], 
    ['1002', 'Doyeon', 98.43], 
    ['1003', 'Jane', 64.19], 
    ['1004', 'Pilwoong', 81.30],
    ['1005', 'Tony', 99.14],
]
df = pd.DataFrame(data)
print(df)


# In[10]:


df = pd.DataFrame(data, columns=['학번', '이름', '점수'])
print(df)


# In[11]:


# 딕셔너리로 생성하기
data = { '학번' : ['1000', '1001', '1002', '1003', '1004', '1005'],
'이름' : [ 'Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],
         '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]}

df = pd.DataFrame(data)
print(df)


# ### 4) 데이터프레임 조회하기
# 
# 아래의 명령어는 데이터프레임에서 원하는 구간만 확인하기 위한 명령어로서 유용하게 사용된다.
# 
# - df.head(n) - 앞 부분을 n개만 보기
# - df.tail(n) - 뒷 부분을 n개만 보기
# - df['열이름'] - 해당되는 열을 확인

# In[12]:


# 앞 부분을 3개만 보기
print(df.head(3))


# In[13]:


# 뒷 부분을 3개만 보기
print(df.tail(3)) 


# In[14]:


# '학번'에 해당되는 열을 보기
print(df['학번'])


# ### 5) 외부 데이터 읽기

# Pandas는 CSV, 텍스트, Excel, SQL, HTML, JSON 등 다양한 데이터 파일을 읽고 데이터 프레임을 생성할 수 있다.
# 
# 예를 들어, csv 파일을 읽을 때는 pandas.read_csv()를 통해 읽을 수 있다.

# In[15]:


df=pd.read_excel('./dataset/코로나19/원문데이터_코로나19.xlsx',sheet_name='Worksheet')


# In[16]:


print(df)


# In[17]:


print(df.index)

