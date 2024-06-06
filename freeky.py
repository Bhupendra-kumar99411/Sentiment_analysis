import json
import random
from faker import Faker

fake = Faker()

def generate_tweet():
    return {
        "date": fake.date_time_this_decade().isoformat(),
        "hashtag": "#" + fake.word(),
        "username": fake.user_name(),
        "tweet": fake.sentence(),
        # "sentiment": random.choice(["positive", "negative", "neutral"])
        "sentiment": random.choice(["positive", "negative"])
        # "sentiment": random.choice([ "negative", "neutral"])
    }

def generate_json(num_rows):
    tweets = [generate_tweet() for _ in range(num_rows)]
    data = {"tweets": tweets}
    return json.dumps(data, indent=2)

if __name__ == "__main__":
    num_rows = 100000 # Change this to the desired number of rows
    json_data = generate_json(num_rows)

    with open("tweets_data25.json", "w") as json_file:
        json_file.write(json_data)

    print(f"JSON file with {num_rows} rows generated successfully.")
