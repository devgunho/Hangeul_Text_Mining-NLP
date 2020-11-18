#!/usr/bin/env python
# coding: utf-8

# # Topic Modeling, LDA

# Latent Dirichlet Allocation, LDA

# In[6]:


from collections import Counter
import random
documents = [["Hadoop", "Big Data", "HBase", "Java", "Spark", "Storm", "Cassandra"],
["NoSQL", "MongoDB", "Cassandra", "HBase", "Postgres"],
["Python", "scikit-learn", "scipy", "numpy", "statsmodels", "pandas"],
["R", "Python", "statistics", "regression", "probability"],
["machine learning", "regression", "decision trees", "libsvm"],
["Python", "R", "Java", "C++", "Haskell", "programming languages"],
["statistics", "probability", "mathematics", "theory"],
["machine learning", "scikit-learn", "Mahout", "neural networks"],
["neural networks", "deep learning", "Big Data", "artificial intelligence"],
["Hadoop", "Java", "MapReduce", "Big Data"],
["statistics", "R", "statsmodels"],
["C++", "deep learning", "artificial intelligence", "probability"],
["pandas", "R", "Python"],
["databases", "HBase", "Postgres", "MySQL", "MongoDB"],
["libsvm", "regression", "support vector machines"]]
random.seed(0)
# 총 문서의 수
D = len(documents)

# topic 수 지정
K=4

# 각 단어를 임의의 토픽에 랜덤 배정
document_topics = [[random.randrange(K) for word in document]
for document in documents]

# 각 토픽이 각 문서에 할당되는 횟수
# Counter로 구성된 리스트
# 각 Counter는 각 문서를 의미
document_topic_counts = [Counter() for _ in documents]


# 각 단어가 각 토픽에 할당되는 횟수
# Counter로 구성된 리스트
# 각 Counter는 각 토픽을 의미
topic_word_counts = [Counter() for _ in range(K)]

# 각 토픽에 할당되는 총 단어수
# 숫자로 구성된 리스트
# 각각의 숫자는 각 토픽을 의미함
topic_counts = [0 for _ in range(K)]

# 각 문서에 포함되는 총 단어수
# 숫자로 구성된 리스트
# 각각의 숫자는 각 문서를 의미함
document_lengths = list(map(len, documents))

# 단어 종류의 수
distinct_words = set(word for document in documents for word in document)
V = len(distinct_words)

# 총 문서의 수
D = len(documents)


# In[7]:


def p_topic_given_document(topic, d, alpha=0.1):
    # 문서 d의 모든 단어 가운데 topic에 속하는
    # 단어의 비율 (alpha를 더해 smoothing)
    return ((document_topic_counts[d][topic] + alpha) / (document_lengths[d] + K * alpha))

def p_word_given_topic(word, topic, beta=0.1):
    # topic에 속한 단어 가운데 word의 비율
    # (beta를 더해 smoothing)
    return ((topic_word_counts[topic][word] + beta) / (topic_counts[topic] + V * beta))

def topic_weight(d, word, k):
    # 문서와 문서의 단어가 주어지면
    # k번째 토픽의 weight를 반환
    return p_word_given_topic(word, k) * p_topic_given_document(k, d)

def choose_new_topic(d, word):
    return sample_from([topic_weight(d, word, k) for k in range(K)])

def sample_from(weights):
    # i를 weights[i] / sum(weights)
    # 확률로 반환
    total = sum(weights)
    # 0과 total 사이를 균일하게 선택
    rnd = total * random.random()
    # 아래 식을 만족하는 가장 작은 i를 반환
    # weights[0] + ... + weights[i] >= rnd
    for i, w in enumerate(weights):
        rnd -= w
        if rnd <= 0:
            return i


# In[8]:


# 위와 같이 랜덤 초기화한 상태에서
# AB를 구하는 데 필요한 숫자를 세어봄
for d in range(D):
    for word, topic in zip(documents[d], document_topics[d]):
        document_topic_counts[d][topic] += 1
        topic_word_counts[topic][word] += 1
        topic_counts[topic] += 1


# '토픽-단어' 와 '문서-토픽' 에 대한 결합확률분포(unknown)로부터 표본을 얻음
# 
# ---
# ### Gibbs Sampler (깁스 샘플링)
# 
# 깁스 샘플링은 다음 상태를 뽑을 때 한꺼번에 모든 변수(차원)의 값을 정하는 것이 아니라 변수 하나씩 값을 선택한다.
# 
# 다른 모든 변수는 현재값으로 고정되어 있다고 가정했을때, 이 변수가 가질 수 있는 값의 조건부 분포로부터 하나를 샘플링하는 것이다.
# 
# 이 과정을 모든 변수에 대해서 반복하면 하나의 새로운 상태가 만들어진다.
# 
# 즉, 새로운 Markov Chain이 형성 되는 것이다.
# 
# ⇒ 최종적으로, 우리는 새롭게 형성된 마코프 체인을 통해서 sample을 얻게 된다.
# 
# ---
#  
# iteration : 1000

# In[9]:


for iter in range(1000):
    for d in range(D):
        for i, (word, topic) in enumerate(zip(documents[d],
                                              document_topics[d])):
            # 깁스 샘플링 수행을 위해
            # 샘플링 대상 word와 topic을 제외하고 세어봄
            document_topic_counts[d][topic] -= 1
            topic_word_counts[topic][word] -= 1
            topic_counts[topic] -= 1
            document_lengths[d] -= 1

            # 깁스 샘플링 대상 word와 topic을 제외한 
            # 말뭉치 모든 word의 topic 정보를 토대로
            # 샘플링 대상 word의 새로운 topic을 선택
            new_topic = choose_new_topic(d, word)
            document_topics[d][i] = new_topic

            # 샘플링 대상 word의 새로운 topic을 반영해 
            # 말뭉치 정보 업데이트
            document_topic_counts[d][new_topic] += 1
            topic_word_counts[new_topic][word] += 1
            topic_counts[new_topic] += 1
            document_lengths[d] += 1


# inference 결과 첫번째 문서의 토픽 비중

# In[10]:


document_topic_counts[0]


# 첫번째 토픽의 단어 비중

# In[11]:


topic_word_counts[0]


# 이 토픽은 대략 ‘Big Data’에 해당하는 주제인 것으로 추론
