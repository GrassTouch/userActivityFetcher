import argparse
import requests
import json

parser = argparse.ArgumentParser()  # instantiate the ArgumentParser class
parser.add_argument("username")     # specify a positional argument
args = parser.parse_args()          # run the parser, extracts data into args (an argparse.Namespace object)
print(args.username)

base_url = "https://api.github.com/users"
url = f"{base_url}/{args.username}/events"  # using f-string to embed username inside the url
print(url)

r = requests.get(url)

print(r.text)