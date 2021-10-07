from botocore.retries import bucket
import extract_data as ed
from load import upload_to_s3


app_name = "Vivint"
app_id = "com.vivint.vivintsky"
bucket_id = "data-engineering-justine"

apple_data = ed.scrape_app_store('kakaloka')
google_data = ed.scrape_google(app_id,app_name)
apple_filename = f"{app_name} Apple Store Reviews.csv"
google_filename = f"{app_name} Google Play Store Reviews.csv"
upload_to_s3(apple_filename, bucket_id, apple_filename)
upload_to_s3(google_filename,bucket_id,apple_filename)
