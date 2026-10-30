from newspaper import Article
from textblob import TextBlob

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
    result = TextBlob(text).sentiment
    label = "Positive" if result.polarity > 0 else "Negative" if result.polarity < 0 else "Neutral"
    print("\n=== TextBlob ===")
    print(f"Polarity: {result.polarity:.4f} (-1 to +1)")
    print(f"Subjectivity: {result.subjectivity:.4f} (0 to 1)")
    print("Overall:", label)

if __name__ == "__main__":
    main()
