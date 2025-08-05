import argparse
import requests
import json

# cli argument method
# parser = argparse.ArgumentParser()  # instantiate the ArgumentParser class
# parser.add_argument("username")     # specify a positional argument
# args = parser.parse_args()          # run the parser, extracts data into args (an argparse.Namespace object)
# print(args.username)

# prompt for input method
username = input("enter a github username: ")


base_url = "https://api.github.com/users"
url = f"{base_url}/{username}/events"  # using f-string to embed username inside the url
print(url)

r = requests.get(url)
dict = r.json()
print(dict)
# print(r.text)
# print(r.content)