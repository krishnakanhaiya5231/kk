def create_s3_bucket(bktname='mys3bucket'):
    print("Creating a " + bktname + " S3 bucket!")

# Default function call
create_s3_bucket()
# Function call with arguments
create_s3_bucket('news3bucket')