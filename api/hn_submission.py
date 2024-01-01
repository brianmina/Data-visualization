from operator import itemgetter
import requests

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(F"Status code: {r.status_code}")

# Process information about each submisson.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids:
    # Make a new call IPA call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print

