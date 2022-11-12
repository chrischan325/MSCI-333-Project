import csv
import sys
import numpy as np
from pathlib import Path

# python main.py Tally_6.csv

def main(argv):
    csv_file = Path(argv[1])
    arr = []
    count = 0
    results = {}
    with open(Path(csv_file)) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if float(row[0]) < 0:
                percentiles = []
                np_arr = np.array(arr)
                percentiles.append(np.percentile(np_arr, 85))
                percentiles.append(np.percentile(np_arr, 99))
                count += 1
                results[count] = percentiles
            else:
                arr.append(float(row[1]))
        with open(Path(Path.cwd(), "{}_results.csv".format(csv_file.stem.split('.')[0])), 'w') as file:
            columns = ["run number", "85th percentile", "99th percentile"]
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()

            for run_number, res in results.items():
                writer.writerow({"run number": run_number, "85th percentile": res[0], "99th percentile": res[1]})






if __name__ == "__main__":
    main(sys.argv)