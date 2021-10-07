from numpy import number
import streamlit as st
from extract_data import scrape_app_store


def pick_app(options, number_of_reviews):
    """
    Returns a dataframe of all the scraped reviews.
    The arguments are as follows -
    options: Select from the following list of applications to be used.
    number_of_reviews: Give an estimate/definite number of reviews you wanted to be scraped. Defaults to None which will scrape everything.
    """
    app_name = options
    # Prints out the number of request for a particular application
    st.write(f"You have requested {number_of_reviews} reviews for {app_name}.")
    # Returns a dataframe
    st.write(scrape_app_store(app_name, number_of_reviews))


options = st.selectbox(
    "What application would you like to select?", ["Chime", "Vivint"]
)
number_of_reviews = st.number_input(
    "How many reviews would you like to extract?", min_value=20, step=1
)
pick_app(options, number_of_reviews)
