import json


class CustomAllo:
    def __init__(self, path: str):
        self.path = path

        with open(self.path) as f:
            f = f.read()
            self.data = json.loads(f)

    def search_symp(self, symp):
        try:
            symp = [i for i in self.data if i['Symptoms'].lower() == symp.lower()][0]
        except Exception as e:
            return "Medicine Not Found"

        return symp['Medicine']


if __name__ == '__main__':
    data = CustomAllo('allo.json')
    print(data.search_symp("acute/chronic symptoms of breathlessness"))
