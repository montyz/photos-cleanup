import csv
import sys
import clean
import importlib.resources

from subprocess import Popen, PIPE, STDOUT


def run_applescript(script, arg_list):
    with importlib.resources.path(clean, script) as fn:
        p = Popen(['osascript', fn] + arg_list, text=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        stdout, stderr = p.communicate(script)
        return p.returncode, stdout, stderr


def main(argv):
    with open(argv[1]) as inputfile:
        with open("errors.csv", "w") as errorfile:
            inputcsv = csv.DictReader(inputfile)
            errorcsv = csv.DictWriter(errorfile, ["uuid", "error"])
            errorcsv.writeheader()
            for d in inputcsv:
                keyword = d['tags']
                returncode, stdout, stderr = run_applescript("tagphoto.scpt", [d['uuid'], keyword])
                if returncode != 0:
                    print("{} returned error code: {}".format(d['uuid'], returncode))
                    errorcsv.writerow({'uuid': d['uuid'], 'error': stdout.strip()})
                else:
                    print("{} succeeded".format(d['uuid']))


if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv)
