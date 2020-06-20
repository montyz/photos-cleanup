import csv
import sys

from subprocess import Popen, PIPE, STDOUT

replace_keyword_script = """
on run {photoid, keyword}
	tell application "Photos"
		set thisItem to media item id photoid
		set keywords of thisItem to {keyword}
	end tell
end run
"""


def run_applescript(script, arg_list):
    p = Popen(['osascript', '-'] + arg_list, text=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout, stderr = p.communicate(script)
    return p.returncode, stdout, stderr


def main(argv):
    with open(argv[1]) as inputfile:
        with open("errors.csv", "w") as errorfile:
            inputcsv = csv.DictReader(inputfile)
            errorcsv = csv.DictWriter(errorfile, ["uuid", "error"])
            errorcsv.writeheader()
            for d in inputcsv:
                returncode, stdout, stderr = run_applescript(replace_keyword_script, [d['uuid'], 'deleteme'])
                if returncode != 0:
                    print("{} returned error code: {}".format(d['uuid'], returncode))
                    errorcsv.writerow({'uuid': d['uuid'], 'error': stdout.strip()})
                else:
                    print("{} succeeded".format(d['uuid']))


if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv)
