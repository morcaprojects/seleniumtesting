import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_cnn_articles():
    # Base URL
    base_url = "https://edition.cnn.com"
    
    # Fetch the homepage
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find article links
    matches = soup.find_all('div', attrs={'data-open-link': True})
    links = []
    for match in matches:
        partial_link = match['data-open-link']
        if partial_link:
            if partial_link.startswith('http'):
                links.append(partial_link)
            else:
                links.append(base_url + partial_link)

    # Create DataFrame
    df = pd.DataFrame(columns=['link', 'headline', 'text'])

    # Loop through each link to get the headline and text
    for link in links:
        article_response = requests.get(link)
        article_soup = BeautifulSoup(article_response.content, 'html.parser')
        
        # Extract headline
        headline_tag = article_soup.find('h1', attrs={'data-editable': 'headlineText'})
        headline = headline_tag.text if headline_tag else 'No headline available'
        
        # Extract text
        paragraphs = article_soup.find_all('p', class_='paragraph inline-placeholder')
        text = '\n'.join(paragraph.text for paragraph in paragraphs)
        
        # Append data to DataFrame
        df.loc[len(df)] = [link, headline, text]

    return df

# Usage
df = scrape_cnn_articles()
st.markdown(df.head())
