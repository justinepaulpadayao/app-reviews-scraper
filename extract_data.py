from logging import exception
from google_play_scraper import app, Sort, reviews, reviews_all
from app_store_scraper import AppStore
import pandas as pd
import numpy as np
import random


def scrape_google(app_id, app_name):
    """
    Takes App ID and App Name as argument.
    Scrapes all reviews in Google Play US then transforms data into a dataframe and saves a csv copy.
    Example:
        app_id  = 'com.vivint.vivintsky'
        app_name = 'Vivint'
    """
    # Scrapes Google Play data
    try:
        app_reviews = reviews_all(
            app_id,
            sleep_milliseconds=0,  # defaults to 0
            lang="en",  # defaults to 'en'
            country="us",  # defaults to 'us'
            sort=Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
        )
    except Exception:
        print("App ID does not exist. Please get the correct ")

    else:

        # Transforms the json file into a dataframe
        df = pd.DataFrame(np.array(app_reviews), columns=["review"])
        df = df.join(pd.DataFrame(df.pop("review").tolist()))

        # Reindexes the column according to database schema
        df = df.reindex(
            columns=[
                "reviewId",
                "userName",
                "userImage",
                "content",
                "score",
                "thumbsUpCount",
                "reviewCreatedVersion",
                "at",
                "replyContent",
                "repliedAt",
            ]
        )

        # Removes the header and saves the file into a csv for a local copy.
        df.to_csv(f"{app_name} Google Play Reviews.csv", index=False)
        print(f"Successfully scraped {df.shape[0]} reviews from Google Play Store")
        return df


def scrape_app_store(app_name, how_many=None):
    """
    Takes a string object of the filename and count of reviews as an argument.
    Scrapes all reviews in the App Store US then transforms data into a dataframe and saves a csv copy.
    Example:
        app_name = 'Vivint'
        how_many = 10 (defaults to None if you want all reviews)
    """

    try:
        # Scrapes App Store data
        app_info = AppStore(country="us", app_name=app_name)

    except Exception as e:
        print("Application name does not exist. Please choose the correct name.")

    else:

        app_info.review(how_many=how_many, sleep=random.randint(30, 35))

        # Transforms the json file into a dataframe
        df = pd.DataFrame(np.array(app_info.reviews), columns=["review"])
        df = df.join(pd.DataFrame(df.pop("review").tolist()))

        # Saves the file into a csv for a local copy.
        df.to_csv(f"{app_name} Apple Store Reviews.csv", index=False)
        print(f"Successfully scraped {df.shape[0]} reviews from App Store.")

        return df
