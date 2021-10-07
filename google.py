from botocore.retries import bucket
import extract_data as ed
from load import upload_to_s3

app_name = input(str("Please choose application from the following: Vivint or Chime? "))

if app_name == 'Vivint':
    app_id = "com.vivint.vivintsky"
else:
    app_id = "com.onedebit.chime"

bucket_id = "data-engineering-justine"

google_data = ed.scrape_google(app_id,app_name)
google_filename = f"{app_name} Google Play Store Reviews.csv"
upload_to_s3(google_filename,bucket_id,google_filename)
