# %%
import tweepy
import yfinance as yf
import pandas as pd

# %%
consumer_key = "ha2uNuolkrVghUsTw3Nm8BPwl"
consumer_secret = "OGL06xRegMR9kOBPcKt8n2mb2UsuroNdEwCSyPdD8ywKeWijTy"
access_token = "10205062-vxsohEqlf9Sq1Fcp1dSPgYWjLQZMzRZwp7bVIb2Zt"
access_token_secret = "15H83943KZnTJRqTAWEtA1Ftv3GUJGjfrInxBIylrZJ0q"

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
client = tweepy.API(auth)

finance_client = yf.Ticker("SPY")


# %%
articles_df = pd.read_csv("/media/gyasis/Blade 15 SSD/Users/gyasi/Google Drive (not syncing)/Collection/projects/Words_and_Money/data/labelled_newscatcher_dataset.csv",sep=";" ,error_bad_lines=False)
# %%
articles_df["published_date"] = pd.to_datetime(articles_df["published_date"])
articles_df.head()
# %%
# for index, row in articles_df.iterrows():
#     # Get the published date and title for the article
#     published_date = row["published_date"]
#     title = row["title"]
    
#     # Split the title into keywords
#     keywords = title.split()
    
#     # Search Twitter for the keywords one month from the published date
#     tweets = client.search_tweets(q=keywords, lang="en", since_id=published_date, until=published_date+pd.Timedelta(weeks=4), max_results=1000)
    
#     # Store the tweets in a dataframe
#     tweets_df = pd.DataFrame(tweets)
    
#     # Clean and transform the data as needed
#     tweets_df = tweets_df.drop_duplicates()
#     tweets_df = tweets_df.dropna()
    
    
# %%

import textblob

# # Assume that you have a dataframe with a column "text" containing the tweet text

# # Add a new column to the dataframe for the sentiment analysis
# tweets_df["sentiment"] = None

# # Iterate over the rows in the dataframe
# for index, row in tweets_df.iterrows():
#     # Get the tweet text
#     text = row["text"]
    
#     # Use TextBlob to perform sentiment analysis on the tweet
#     sentiment = textblob.TextBlob(text).sentiment.polarity
    
#     # Store the sentiment in the dataframe
#     tweets_df.at[index, "sentiment"] = sentiment
    
    


articles_df["title_sentiment"] = None

# Iterate over the rows in the dataframe
for index, row in articles_df.iterrows():
    # Get the article title
    title = row["title"]
    
    # Use TextBlob to perform sentiment analysis on the title
    sentiment = textblob.TextBlob(title).sentiment.polarity
    
    # Store the sentiment in the dataframe
    articles_df.at[index, "title_sentiment"] = sentiment
    
# %%
data = articles_df
import plotly.express as px

# Assume that you have a dataframe with columns "topic" and "sentiment"

# Group the data by topic and calculate the percentage of articles in each topic
topic_counts = data.groupby("topic")["topic"].count()
topic_percentages = topic_counts / sum(topic_counts) * 100


topic_counts = data.groupby("topic")
# # Create a pie chart showing the percentage of articles by topic, color-coded by sentiment
# fig = px.pie(data, values="topic", names=topic_percentages.index, title="Percentage of Articles by Topic", color="sentiment")
# fig.show()
# %%
# create a pie chart showing the percentage of articles by topic and sentiment popularity

def pie_graph(data, title, values, names):
    fig = px.pie(data, values=values, names=names, title=title, )
    fig.show()
#give list of unique topics in articles_df.topic

names1 = list(articles_df.topic.unique())   
tree = list(topic_percentages.index)
pie_graph(articles_df, "Percentage of Articles by Topic", names1, tree )
# %%


# %%
fig1 = px.histogram(articles_df, x="title_sentiment", color="topic",)
fig1.show()
# %%
