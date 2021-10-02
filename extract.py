from google_play_scraper import app, Sort, reviews, reviews_all
from app_store_scraper import AppStore
import pandas as pd
import numpy as np
from pprint import pprint
import random

def scrape_google(app_id):
    """
    Scrapes all reviews in Google Play then transforms data into a dataframe and saves a csv copy.
    """
    # Scrapes Google Play data
    app_reviews = reviews_all(
        app_id,
        sleep_milliseconds=0,  # defaults to 0
        lang="en",  # defaults to 'en'
        country="us",  # defaults to 'us'
        sort=Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
    )

    # Transforms the json file into a dataframe
    df = pd.DataFrame(np.array(app_reviews), columns=["review"])
    df = df.join(pd.DataFrame(df.pop("review").tolist()))

    # Saves the file into a csv for a local copy.
    df.to_csv(f"{app_id}.csv")
    print(f"Successfully scraped {df.shape[0]} reviews from Google Play Store")
    return df


def scrape_app_store(app_name):
    """
    Scrapes all reviews in the App Store then transforms data into a dataframe and saves a csv copy.
    """

    # Scrapes App Store data
    app_info = AppStore(country="us", app_name=app_name)
    app_info.review(how_many = 10, sleep=random.randint(30, 35))

    # Transforms the json file into a dataframe
    df = pd.DataFrame(np.array(app_info.reviews),columns=['review'])
    df_chime = df.join(pd.DataFrame(df.pop('review').tolist()))

    # Saves the file into a csv for a local copy.
    df_chime.to_csv(f"{app_name} App Store Reviews.csv")
    print(f"Successfully scraped {df_chime.shape[0]} reviews from App Store")
    return print(df_chime)




