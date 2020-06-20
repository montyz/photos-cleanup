import csv
import sys

def main(argv):
    with open(argv[1]) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row[0])

if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv)