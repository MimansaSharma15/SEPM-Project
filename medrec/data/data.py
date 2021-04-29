import json
from medrec.ML.rake_text import final_out
from nltk.corpus import stopwords
from collections import Counter


class CustomData:
    def __init__(self, path_ay: str, path_allo: str):
        self.path_ay = path_ay

        with open(self.path_ay) as f:
            f = f.read()
            self.data_ay = json.loads(f)

        self.path_allo = path_allo

        with open(self.path_allo) as f:
            f = f.read()
            self.data_allo = json.loads(f)
        self.stopwords = stopwords.words('english')

    def search_sym(self, symptom: str) -> str:
        """

        Returns:
             sym
        """
        symptom = symptom.lower()

        if len(symptom) > 100:
            keywords = set(final_out(symptom))
            for num, sym in self.data_ay['Symptom'].items():
                sym = set(sym)
                if sym & keywords:
                    return num

        for num, sym in self.data_ay['Symptom'].items():
            if sym.lower() == symptom:
                return num

    def search_med(self, symp: str) -> str:
        """

        Args:
            symp:

        Returns:
            med
        """

        for num, med in self.data_ay['English common name of herbal substance'].items():
            num_sym = self.search_sym(symp)
            if num == num_sym:
                return med

        return "Medicine not Found"

    def search_allo(self, symp):
        try:
            symp = [i for i in self.data_allo if i['Symptoms'].lower() == symp.lower()][0]
        except Exception as e:
            return "Medicine Not Found"

        return symp['Medicine']


if __name__ == '__main__':
    data = CustomData(path_ay='medicine_ayur.json', path_allo='allo.json')
    print(data.search_med('Urinary tract and genital disorders'))
    print(data.search_allo('cough, chest pains and an accompanying shortness of breath'))
