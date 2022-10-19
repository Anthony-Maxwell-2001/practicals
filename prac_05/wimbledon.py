"""
Wimbledon
Estimate: 30 minutes
Actual:
"""

FILENAME = "wimbledon.csv"


def main():
    records = get_records()
    champion_to_count, countries = process_records(records)


def get_records():
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            records.append(parts)
        return records


def process_records(records):
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        try:
            champion_to_count[record[2]] += 1
        except KeyError:
            champion_to_count[record[2]] = 1

    print(countries)
    print(champion_to_count)
    return champion_to_count, countries


main()
