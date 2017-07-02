export GOOGLE_APPLICATION_CREDENTIALS=</Users/sathvik/Downloads/membershipdevunited-f08a6254742b.json>

def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)

gcloud beta ml language analyze-entities --content="Contact Us iconSend us a messageicon801.434.9200iconinfo@achildshopefoundation.orgiconOffice: 165 North 1330 West Ste. A1, Orem Utah 84057iconMailing: 2727 West 620 North, Provo Utah 84601"
