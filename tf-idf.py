from sklearn.feature_extraction.text import TfidfVectorizer

# Sample documents
documents = [
    "Data science is the field of study that combines domain expertise, programming skills, and knowledge of mathematics and statistics.",
    "Machine learning is a subfield of data science that focuses on the development of algorithms that learn from and make predictions on data.",
    "Statistics is a branch of mathematics that deals with data collection, analysis, interpretation, and presentation."
]

# Create a TfidfVectorizer object
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the documents into a TF-IDF matrix
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# Get the feature names (words)
feature_names = tfidf_vectorizer.get_feature_names_out()

# Convert the TF-IDF matrix to a dense format
dense_tfidf_matrix = tfidf_matrix.todense()

# Convert dense matrix to a list of lists
tfidf_list = dense_tfidf_matrix.tolist()

# Print each document's TF-IDF scores
for i, doc in enumerate(tfidf_list):
    print(f"Document {i+1}:")
    for j, score in enumerate(doc):
        if score > 0:
            print(f"  {feature_names[j]}: {score:.4f}")
    print("\n")
