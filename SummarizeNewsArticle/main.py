import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob
from newspaper import Article


def update_text(widget, value):
    """Update a disabled Tkinter Text widget."""
    widget.config(state="normal")
    widget.delete("1.0", tk.END)
    widget.insert(tk.END, str(value) if value else "Not available")
    widget.config(state="disabled")


def summarize():
    url = url_input.get("1.0", "end").strip()

    if not url:
        messagebox.showwarning("Warning", "Please enter a URL")
        return

    summarize_button.config(state="disabled", text="Processing...")
    root.update_idletasks()

    try:
        # Download and parse the article
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        # Perform sentiment analysis
        analysis = TextBlob(article.text)
        polarity = analysis.sentiment.polarity

        if polarity > 0:
            sentiment_result = "Positive"
        elif polarity < 0:
            sentiment_result = "Negative"
        else:
            sentiment_result = "Neutral"

        # Display extracted information
        update_text(title_box, article.title)
        update_text(author_box, ", ".join(article.authors))
        update_text(publication_box, article.publish_date)
        update_text(summary_box, article.summary)
        update_text(
            sentiment_box,
            f"{sentiment_result} (Polarity: {polarity:.3f})"
        )
        update_text(url_box, url)

        print(f"Title: {article.title}")
        print(f"Authors: {article.authors}")
        print(f"Publication Date: {article.publish_date}")
        print(f"Summary: {article.summary}")
        print(f"Sentiment: {sentiment_result}")
        print(f"Polarity: {polarity}")

    except Exception as error:
        messagebox.showerror("Error", str(error))

    finally:
        summarize_button.config(state="normal", text="Summarize")


# Create main window
root = tk.Tk()
root.title("News Summarizer")
root.geometry("1200x800")


# Title
title_label = tk.Label(root, text="Title")
title_label.pack()

title_box = tk.Text(root, height=1, width=140)
title_box.config(state="disabled", bg="#dddddd")
title_box.pack()


# Author
author_label = tk.Label(root, text="Author")
author_label.pack()

author_box = tk.Text(root, height=1, width=140)
author_box.config(state="disabled", bg="#dddddd")
author_box.pack()


# Publication Date
publication_label = tk.Label(root, text="Publishing Date")
publication_label.pack()

publication_box = tk.Text(root, height=1, width=140)
publication_box.config(state="disabled", bg="#dddddd")
publication_box.pack()


# Summary
summary_label = tk.Label(root, text="Summary")
summary_label.pack()

summary_box = tk.Text(root, height=20, width=140)
summary_box.config(state="disabled", bg="#dddddd")
summary_box.pack()


# Sentiment Analysis
sentiment_label = tk.Label(root, text="Sentiment Analysis")
sentiment_label.pack()

sentiment_box = tk.Text(root, height=1, width=140)
sentiment_box.config(state="disabled", bg="#dddddd")
sentiment_box.pack()


# URL
url_label = tk.Label(root, text="URL")
url_label.pack()

url_input = tk.Text(root, height=1, width=140)
url_input.pack()

url_box = tk.Text(root, height=1, width=140)
url_box.config(state="disabled", bg="#dddddd")
url_box.pack()


# Summarize Button
summarize_button = tk.Button(
    root,
    text="Summarize",
    command=summarize
)
summarize_button.pack(pady=10)


# Run application
root.mainloop()