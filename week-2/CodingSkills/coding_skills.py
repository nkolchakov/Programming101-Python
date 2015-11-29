import json
import sys


def read_json():
    filename = 'data.json' #sys.argv[1]
    with open(filename, 'r') as f:
        data = json.load(f)

    return data

#print (read_json())


def task(dictionary):

    res_dict = {}
    # key name = dictionary.keys()[i]
    for i in range(0,len(dictionary.keys())):
        for j in range(0,len(dictionary[dictionary.keys()[i]])):
            for m in range(0,len(dictionary[dictionary.keys()[i]][j]['skills'])):
                name = dictionary[dictionary.keys()[i]][j]['first_name']
                el = dictionary[dictionary.keys()[i]][j]
                lang = el['skills'][m]['name']
                level = el['skills'][m]['level']
               # print {lang:[level,name]}
                lst = [level,name]
                # print lang
                # print lst
                if not (lang in res_dict):
                    res_dict[lang] = [lst]
                else:
                    res_dict[lang].append(lst)
    
    ranking = {}
    for dct in res_dict:
        if len(res_dict[dct]) == 1:
            ranking[dct] = res_dict[dct][0][0]
   # print ranking
    return res_dict

print task(read_json())

task(read_json())

