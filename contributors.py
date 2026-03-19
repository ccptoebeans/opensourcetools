#!/usr/bin/env python
"""extract the username and email addresses of contributers to a local or remote git repository
"""
import os, subprocess, argparse, sys, stat, tempfile, shutil

GREY="\033[38;5;145m"
OKCYAN_COLOUR = '\033[96m'
END_COLOUR = '\033[0m'
FAIL_COLOUR = '\033[91m'

if __name__ == "__main__":
	command_line = argparse.ArgumentParser(description=str(__doc__), formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	command_line.add_argument('--url', help='The URL of the repo we are checking', required=False)
	command_line.add_argument('--dir', help='Path to a pre-cloned repo')
	command_line.add_argument('--mailmap', help='Output a template mailmap file to a specified location EG: "--mailmap .mailmap" (https://git-scm.com/docs/gitmailmap)')
	command_line.add_argument('--anonymize', help='When --mailmap is specified, this will cause all contributer information to be mapped to anonimized data', action='store_true')
	command_line.add_argument('--anonusername', help='when outputing a mailmap, this username will be used instead of the default "Anonymous CCP Employee"', default="Anonymous CCP Employee")
	command_line.add_argument('--anonemail', help='when outputing a mailmap, this email address will be used instead of the default "anonymous.employee@ccpgames.com"', default="anonymous.employee@ccpgames.com")

	args = command_line.parse_args()

	if args.dir and args.url:
		sys.exit(f"{FAIL_COLOUR}error: you may provide either --url or --dir, not both{END_COLOUR}")

	if not args.mailmap and args.anonymize:
		sys.exit(f"{FAIL_COLOUR}error: --mailmap must specified when setting --anonymize{END_COLOUR}")

	try:
		location = ""
		if args.dir:
			print(f"{GREY}")
			location = args.dir
			print(f"Reading git repo {location}")
		else:
			if not args.url:
				sys.exit(f"{FAIL_COLOUR}error: You must provide a valid git url '--url git@github.com...' or git directory '--dir path/to/local/repo'{END_COLOUR}")
			location = tempfile.mkdtemp()
			print(f"{GREY}")
			print(f"cloning from {args.url}")
			subprocess.run(["git", "clone", args.url, location])

		output = subprocess.check_output(["git", "log", "--pretty=format:'%an <%ae>'"], cwd=location, universal_newlines=True)

		contribs = output.strip('"')

		unique = set()

		for l in contribs.split("\n"): 
			unique.add(l.strip("'"))
		
		print(f"{END_COLOUR}")
		print(f"{OKCYAN_COLOUR}----- CONTRIBUTERS (username <email>) -----{END_COLOUR}")
		for c in unique:
			print(c)

		if args.mailmap:
			with open(args.mailmap, 'w') as mailmapfile:
				for c in unique:
					line = c
					if args.anonymize:
						line = f"{args.anonusername} <{args.anonemail}> {c}"
					mailmapfile.write(line + "\n")

	finally:
		if args.url:
			# delete readonly files https://docs.python.org/3/library/shutil.html#shutil-rmtree-example
			def remove_readonly(func, path, _):
			    "Clear the readonly bit and reattempt the removal"
			    os.chmod(path, stat.S_IWRITE)
			    func(path)

			shutil.rmtree(location, onexc=remove_readonly)
		print(f"{END_COLOUR}")
