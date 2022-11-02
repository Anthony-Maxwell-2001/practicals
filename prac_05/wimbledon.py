"""
Wimbledon
Estimate: 30 minutes
Actual: 30 minutes 18 seconds
"""

FILENAME = "wimbledon.csv"


def main():
    records = get_records()
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


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


def display_results(champion_to_count, countries):
    print("Wimbledon Champions: ")
    for name, score in champion_to_count.items():
        print(name, score)
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


main()
