import argparse

parser = argparse.ArgumentParser()  # instantiate the ArgumentParser class
parser.add_argument("username")     # specify a positional argument
args = parser.parse_args()          # run the parser, extracts data into args (an argparse.Namespace object)
print(args.username)

