
from transformers import pipeline

# Load pretrained BERT model
model = pipeline(
    "sentiment-analysis",
    model="textattack/bert-base-uncased-SST-2"
)

# Enter text
text = input("Enter a sentence: ")

# Perform sentiment analysis
result = model(text)

# Display result
print("\nSentiment:", result[0]['label'])
print("Confidence:", round(result[0]['score'] * 100, 2), "%")
