import argparse

parser = argparse.ArgumentParser()  # instantiate the ArgumentParser class
parser.add_argument("username")     # define the expected argument
args = parser.parse_args()
print(args.username)

