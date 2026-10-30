# News Summarizer & Sentiment Analysis

A Python-based News Summarizer application that extracts information from online news articles, generates concise summaries, and performs sentiment analysis using TextBlob. The application provides a graphical user interface built with Tkinter.

## Features

- **Article Extraction:** Extracts news article content directly from a URL.
- **Title Extraction:** Retrieves the article title.
- **Author Detection:** Extracts the author's name.
- **Publication Date:** Retrieves the article's publication date.
- **Text Summarization:** Generates a concise summary using Newspaper3k.
- **Sentiment Analysis:** Analyzes the article's text and classifies its sentiment as Positive, Negative, or Neutral.
- **Graphical User Interface:** Displays all extracted information through a Tkinter application.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Tkinter | Graphical User Interface |
| Newspaper3k | News article extraction and summarization |
| TextBlob | Sentiment analysis |
| NLTK | Natural Language Processing support |

## Project Structure

```text
News-Summarizer/
│
├── main.py
├── README.md
└── requirements.txt
```

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd News-Summarizer
```

### 2. Install Dependencies

```bash
pip install newspaper3k lxml_html_clean textblob nltk
```

### 3. Run the Application

```bash
python main.py
```

## How to Use

1. Launch the application.
2. Enter the URL of a news article.
3. Click the **Summarize** button.
4. The application downloads and processes the article.
5. View the extracted title, author, publication date, summary, and sentiment in the GUI.

## How It Works

The application follows these steps:

1. **URL Input:** The user provides a news article URL.
2. **Article Download:** Newspaper3k downloads the article.
3. **Content Extraction:** The article's title, authors, publication date, and text are extracted.
4. **Text Summarization:** Newspaper3k's NLP functionality generates a summary.
5. **Sentiment Analysis:** TextBlob calculates the polarity of the article's text.
6. **Sentiment Classification:**
   - Polarity greater than 0: Positive
   - Polarity less than 0: Negative
   - Polarity equal to 0: Neutral
7. **GUI Display:** The extracted information and analysis results are displayed using Tkinter.

## Example Output

For a Microsoft article about TikTok, the application displays:

- **Title:** Microsoft statement on TikTok
- **Author:** Microsoft Corporate Blogs
- **Publication Date:** 2020-09-13
- **Summary:** A concise summary of the article.
- **Sentiment:** Positive

## Limitations

- Some websites may block automated article extraction.
- The quality of the generated summary depends on the article content.
- TextBlob uses a general-purpose sentiment analysis approach and may not understand sarcasm or complex context accurately.
- Publication dates and author information may not be available for every article.

## Future Improvements

- Add support for multiple news articles.
- Improve the GUI design.
- Add sentiment confidence and visualization.
- Support additional sentiment analysis models such as VADER and BERT.
- Add the ability to export summaries to PDF or TXT files.

## Author

Developed as a Python Natural Language Processing (NLP) project to explore web scraping, text summarization, sentiment analysis, and GUI development.