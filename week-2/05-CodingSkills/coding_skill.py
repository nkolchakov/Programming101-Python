import json
import sys


class Person:

    def __init__(self, first_name, last_name, skills):
        self.first_name = first_name
        self.last_name = last_name
        self.skills = {}
        for kv_pair in skills:
            self.skills[kv_pair['name']] = kv_pair['level']

    def __str__(self):
        return '{} {} - {}'.format(self.first_name,
                                   self.last_name, self.skills)

    def __repr__(self):
        return str(self)


def json_to_people(json):
    people = []
    for el in json['people']:
        curr_person = Person(el['first_name'],
                             el['last_name'],
                             el['skills'])

        people.append(curr_person)
    return people


def read_json(json_name):
    filename = json_name
    with open(filename, 'r') as f:
        data = json.load(f)

    return data


def main():
    json_name = sys.argv[1]
    data = read_json(json_name)
    people = json_to_people(data)
    lang_level_dict = {}
    for person in people:
        els = str(person).split(' - ')
        name = els[0]
        for lang in eval(els[1]):
            level = eval(els[1])[lang]
            lang_name = lang
            tpl = (name, level)
            if lang_name not in lang_level_dict:
                lang_level_dict[lang_name] = [tpl]
            else:
                lang_level_dict[lang_name].append(tpl)

    for key_name in lang_level_dict:
        max_pnts = 0
        name = ''
        for person in lang_level_dict[key_name]:
            pnts = person[1]
            if (pnts > max_pnts):
                max_pnts = pnts
                name = person[0]
        print ('{} - {}'.format(key_name, name))

if __name__ == '__main__':
    main()

