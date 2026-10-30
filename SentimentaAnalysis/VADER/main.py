from newspaper import Article
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_text():
    value = input("Enter an article URL or paste text: ").strip()
    if value.startswith(("http://", "https://")):
        article = Article(value)
        article.download()
        article.parse()
        if not article.text.strip():
            raise ValueError("No article text could be extracted.")
        print("Title:", article.title)
        return article.text
    return value

def main():
    text = get_text()
    scores = SentimentIntensityAnalyzer().polarity_scores(text)
    compound = scores["compound"]
    label = "Positive" if compound >= 0.05 else "Negative" if compound <= -0.05 else "Neutral"
    print("\n=== VADER ===")
    for key, value in scores.items():
        print(f"{key.title()}: {value:.4f}")
    print("Overall:", label)

if __name__ == "__main__":
    main()
