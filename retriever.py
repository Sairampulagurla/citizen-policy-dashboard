from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def split_text(text, chunk_size=500):

    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)

    return chunks


def find_relevant_chunk(text, question):

    chunks = split_text(text)

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(chunks + [question])

    similarity = cosine_similarity(vectors[-1], vectors[:-1])

    best_index = similarity.argmax()

    return chunks[best_index]