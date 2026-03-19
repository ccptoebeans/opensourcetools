#!/usr/bin/env python
"""extract the username and email addresses of contributers to a local or remote git repository
"""
import os, subprocess, argparse, sys, stat

GREY="\033[38;5;145m"
OKCYAN_COLOUR = '\033[96m'
END_COLOUR = '\033[0m'

def rmtree(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(top)

if __name__ == "__main__":
	command_line = argparse.ArgumentParser(description=str(__doc__), formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	command_line.add_argument('--url', help='The URL of the repo we are checking', required=False)
	command_line.add_argument('--dir', help='path to a pre-cloned repo')

	args = command_line.parse_args()

	try:
		location = "OSCHECKER_TMP_DIR"
		if args.dir:
			print(f"{GREY}")
			location = args.dir
			print(f"Reading git repo {location}")
		else:
			if not args.url:
				sys.exit("you must provide a valid git url or --dir path/to/local/repo")
			print(f"{GREY}")
			print(f"cloning from {args.url}")
			subprocess.run(["git", "clone", args.url, location])#, '-q'])

		output = subprocess.check_output(["git", "log", "--pretty=format:'%an %ae'"], cwd=location, universal_newlines=True)

		contribs = output.strip('"')

		unique = set()

		for l in contribs.split("\n"): 
			unique.add(l.strip("'"))
		
		print(f"{END_COLOUR}")
		print(f"{OKCYAN_COLOUR}----- CONTRIBUTERS (username email) -----{END_COLOUR}")
		for c in unique:
			print(c)

	finally:
		if args.url:
			rmtree(location)
		print(f"{END_COLOUR}")
