from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

S1 = "data science is fun"
S2 = "science makes data useful"

vectorizer = CountVectorizer().fit([S1, S2])

vectors = vectorizer.transform([S1, S2])

cos_sim = cosine_similarity(vectors[0], vectors[1])[0][0]

print("Cosine Similarity:", cos_sim)