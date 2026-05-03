# Movie Recommendation System

A content-based movie recommendation system built using Machine Learning that suggests 5 similar movies based on your selection.

## How it Works
- TMDB 5000 movies dataset is cleaned and preprocessed
- Movie metadata is combined into tags and stemmed using NLTK PortStemmer
- Count Vectorizer converts tags into numerical vectors
- Cosine Similarity finds the 5 most similar movies

## Tech Stack
- Python, Pandas, NumPy
- NLTK (PortStemmer)
- Scikit-learn (CountVectorizer, Cosine Similarity)
- Streamlit
- Pickle

## How to Run
1. Install dependencies
```bash
pip install -r requirements.txt
```
2. Generate `similarity.pkl` by running `movie_recommender.ipynb`
3. Run the app
```bash
streamlit run app.py
```

## Note
`similarity.pkl` is not included due to GitHub's file size limit (180MB). Run the notebook to generate it locally.
