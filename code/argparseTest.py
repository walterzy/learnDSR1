import argparse

parser = argparse.ArgumentParser(description="This is an example program.")

parser.add_argument("name", help="uaer name")
parser.add_argument("-a", "--age", type=int, help="user age", default=18)
parser.add_argument("-v", "--verbose", action="store_true", help="if show detailed information")

args = parser.parse_args()

print(f"Hello, {args.name}!")
if args.verbose:
    print(f"Age: {args.age}")