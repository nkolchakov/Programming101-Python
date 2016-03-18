import requests
import json


def save_to_json(source, file_name):
    with open(file_name, 'w') as fp:
        json.dump(source, fp)


def find_name(db, code):
    for el in db:
        if el['Code'] == code:
            return el['Name']


def main():
    airlines_url = 'http://astral.hacksoft.io/api/airline/'
    countries_url = 'http://data.okfn.org/data/core/country-list/r/data.json'

    r = requests.get(airlines_url)
    air_json = r.json()
    r = requests.get(countries_url)
    countries_json = r.json()

    histogram = {}

    for line in air_json:
        code = line['country_code']
        country_name = find_name(countries_json, code)

        if country_name in histogram:
            histogram[country_name] += 1
        else:
            histogram[country_name] = 1

    save_to_json(histogram, 'result.json')

    print(histogram)

if __name__ == '__main__':
    main()
