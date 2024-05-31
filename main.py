import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from scraping import scrape_trt_news, scrape_cnn_articles

# Usage
df = scrape_cnn_articles()
st.markdown(len(df))
st.markdown(df.head())
