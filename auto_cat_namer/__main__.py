import argparse
import csv
from .catscanner import write_name_to_image


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-csv", help="Load data from CSV like (filename, name)")
    parser.add_argument("--output-path", help="Output path to rendered images")
    args = parser.parse_args()

    if args.input_csv is None or args.output_path is None:
        print("You must pass --input-csv and output--path")
        return

    with open(args.input_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        
        for i, row in enumerate(csv_reader):
            if i == 0:
                continue
            filename, name = row
            write_name_to_image(name, filename, args.output_path)


if __name__ == "__main__":
    main()
