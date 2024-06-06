import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon (if not already downloaded)
# nltk.download('vader_lexicon')

# Create a SentimentIntensityAnalyzer object
sid = SentimentIntensityAnalyzer()

# Sample tweets
# tweets = [
#     "I love NLTK! It's a fantastic tool for natural language processing.",
#     "This movie is terrible. I can't stand it.",
#     "The weather today is nice and sunny.",
#     "I'm feeling happy and excited about the upcoming project."
# ]

# # Perform sentiment analysis on each tweet
# for tweet in tweets:
tweet = input()
print(f"Tweet: {tweet}")
sentiment_scores = sid.polarity_scores(tweet)
print(f"Sentiment Scores: {sentiment_scores}")

    # Determine sentiment label based on the compound score
if sentiment_scores['compound'] >= 0.05:
    sentiment_label = 'Positive'
elif sentiment_scores['compound'] <= -0.05:
    sentiment_label = 'Negative'
else:
    sentiment_label = 'Neutral'
        
print(f"Sentiment Label: {sentiment_label}\n")
