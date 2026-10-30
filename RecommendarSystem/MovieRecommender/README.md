# Movie Recommendation System

A content-based movie recommendation system built using Python and Machine Learning. The project recommends movies based on similarities in their genres, keywords, cast, crew, and overview.

It uses CountVectorizer to convert movie metadata into numerical feature vectors and Cosine Similarity to identify movies with similar content.

## Features

- **Content-Based Filtering:** Recommends movies based on their metadata and content.
- **Movie Metadata Processing:** Combines overview, genres, keywords, cast, and crew information.
- **Text Vectorization:** Uses CountVectorizer to convert text data into numerical vectors.
- **Similarity Calculation:** Uses Cosine Similarity to calculate similarities between movies.
- **Top 5 Recommendations:** Returns five movies most similar to the selected movie.
- **Movie Lookup:** Accepts a movie title and checks whether it exists in the dataset.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and preprocessing |
| NumPy | Numerical operations |
| Scikit-learn | CountVectorizer and Cosine Similarity |
| Jupyter Notebook | Development environment |

## Project Structure

```text
MovieRecommender/
│
├── MovieRecommend.ipynb
├── README.md
└── requirements.txt
```

## How It Works

The recommendation system follows these steps:

### 1. Data Preprocessing

Movie metadata is processed to prepare it for recommendation.

The following columns are combined:

- Overview
- Genres
- Keywords
- Cast
- Crew

These features are combined into a single column called `tags`.

### 2. Text Vectorization

CountVectorizer converts the movie tags into numerical feature vectors.

Configuration:

```python
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(
    max_features=5000,
    stop_words='english'
)

vector = cv.fit_transform(new['tags']).toarray()
```

### 3. Cosine Similarity

Cosine Similarity calculates how similar two movie vectors are.

```python
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vector)
```

Movies with higher similarity scores are considered more relevant to the selected movie.

### 4. Movie Recommendation

The recommendation function identifies the selected movie and retrieves the five most similar movies.

```python
def recommend(movie):
    movie_index = new.index[new['title'] == movie]

    if len(movie_index) == 0:
        print("Movie not found! Please enter a valid movie title.")
        return

    index = new.index.get_loc(movie_index[0])

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    for i in distances[1:6]:
        print(new.iloc[i[0]].title)
```

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd MovieRecommender
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open `MovieRecommend.ipynb` and execute the notebook cells in order.

## How to Use

Once the notebook has been executed:

1. Call the `recommend()` function.
2. Enter a movie title that exists in the dataset.
3. The system calculates similarity scores.
4. The five most similar movies are displayed.

Example:

```python
recommend('The Lego Movie')
```

## Recommendation Approach

This project uses **Content-Based Filtering**.

Unlike collaborative filtering, which relies on user ratings or preferences, content-based filtering recommends movies by comparing their characteristics.

The system uses:

- Movie descriptions
- Genres
- Keywords
- Cast information
- Crew information

This allows recommendations to be generated based on movie content rather than user interaction history.

## Limitations

- Recommendations depend on the quality and completeness of movie metadata.
- Movie titles must match entries in the dataset.
- The system does not consider individual user preferences or ratings.
- CountVectorizer does not understand semantic meaning between words.
- Recommendations are limited to movies available in the dataset.

## Future Improvements

- Develop an interactive web application using Streamlit.
- Add movie posters using an external movie database API.
- Implement fuzzy matching for movie title searches.
- Explore TF-IDF vectorization and compare recommendation quality.
- Experiment with collaborative filtering.
- Add user ratings and personalized recommendations.

## Author

Developed as a Machine Learning project to explore Natural Language Processing, text vectorization, similarity measurement, and content-based recommendation systems.