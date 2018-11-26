import json
import sys
from collections import OrderedDict


def main(script):
    data = parse_input(script)
    write_data(data)
    print("Done!")


def parse_input(script):
    with open(script, 'r') as inf:
        lines = inf.readlines()

    lines = lines[1:]

    data = OrderedDict()
    for line in lines:
        values = line.strip().split(",")
        town = values[0].strip()
        store = values[1].strip()

        if town not in data:
            data[town] = [store]
        else:
            data[town].append(store)

    sorted_data = {}
    for town in sorted(data.keys()):
        stores = data[town]
        sorted_data[town] = sorted(stores)

    json_data = {
        "data": sorted_data
    }

    return json_data


def write_data(data):
    json_str = json.dumps(data, sort_keys=True)
    json_str = "var jsonObject = {};".format(json_str)
    with open('stores.json', 'w') as opf:
        opf.write(json_str)


if __name__ == "__main__":
    script_path = str(sys.argv[1])
    main(script_path)
