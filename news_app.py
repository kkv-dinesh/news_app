import streamlit as st
import requests
import pandas as pd

NEWS_API_KEY = '5ec52e37ff9940e2a674d64ac7a09b94'

@st.cache_data(ttl=3600)  # Cache data for 1 hour
def fetch_headlines():
    try:
        response = requests.get(f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}')
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()['articles']
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching headlines: {e}")
        return []

def process_headlines(headlines):
    df = pd.DataFrame(headlines)
    df['Published At'] = pd.to_datetime(df['publishedAt']).dt.strftime('%Y-%m-%d %H:%M:%S')
    df['Source'] = df['source'].apply(lambda x: x['name'])
    df = df.rename(columns={'title': 'Title'})  # Rename the 'title' column to 'Title'
    return df

def visualize_headlines(df):
    st.write('## Latest Headlines')
    st.table(df[['Title', 'Source', 'Published At']].reset_index(drop=True))

def main():
    st.set_page_config(layout="wide")  # Set wide layout
    st.title('News Headlines')

    headlines = fetch_headlines()

    if headlines:
        df = process_headlines(headlines)
        visualize_headlines(df)
    else:
        st.warning("No headlines available.")

if __name__ == '__main__':
    main()