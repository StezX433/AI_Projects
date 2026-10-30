
from transformers import pipeline

# Load pretrained RoBERTa model
model = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

# Enter a sentence
text = input("Enter a sentence: ")

# Perform sentiment analysis
result = model(text)

# Display output
print("\nSentiment:", result[0]['label'])
print("Confidence:", round(result[0]['score'] * 100, 2), "%")
