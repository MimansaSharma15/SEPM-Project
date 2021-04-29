import re
import json


def clean_data(path: str):
    with open(path) as f:
        f = f.read()

    json_data = json.loads(f)
    all_symp = []
    for i in json_data:
        all_symp.append(i['Symptoms'])
    # all_symp = [i for i in all_symp if len(i)]
    all_symp = ' '.join(all_symp)
    print(all_symp)

    # print(symptoms)
    # print(json.dumps(json_data, indent=4))


clean_data('allo.json')
