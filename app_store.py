from botocore.retries import bucket
import extract_data as ed
from load import upload_to_s3

app_name = input(
    "Please choose application from the following: Vivint or Chime? "
)


if app_name == 'Vivint':
    app_id = "com.vivint.vivintsky"
else:
    app_id = "com.onedebit.chime"

bucket_id = "data-engineering-justine"

apple_data = ed.scrape_app_store(app_name)
apple_filename = f"{app_name} Apple Store Reviews.csv"
upload_to_s3(apple_filename, bucket_id, apple_filename)

