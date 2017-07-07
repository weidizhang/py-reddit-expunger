from Expunger import Expunger

__author__ = "Weidi Zhang"

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help = "Username")
parser.add_argument("-p", "--password", help = "Password")
parser.add_argument("-i", "--id", help = "OAuth Client ID")
parser.add_argument("-s", "--secret", help = "OAuth Client Secret")
parser.add_argument("-v", "--verbose", dest = "verbose", action = "store_true", help = "Enable verbose mode")
parser.add_argument("-c", "--limit", help = "Comment limit, default: 1000")

parser.set_defaults(verbose = False, limit = 1000)

args = parser.parse_args()

if (args.username is not None) and (args.password is not None) and (args.id is not None) and (args.secret is not None):
	expunger = Expunger(args.username, args.password, args.id, args.secret)
	expunger.setVerboseMode(args.verbose)
	expunger.reddit.setCommentLimit(args.limit)

	expunger.run()
else:
	print("Error: username, password, id, secret arguments are required")
	print("For help: python3 CLI.py --help")
