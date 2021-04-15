import json


class CustomData:
    def __init__(self, path: str):
        self.path = path

        with open(self.path) as f:
            f = f.read()
            self.data = json.loads(f)

    def search_sym(self, symptom: str) -> str:
        """

        Returns:
             sym
        """
        for num, sym in self.data['Symptom'].items():
            if sym == symptom:
                return num

    def search_med(self, symp: str) -> str:
        """

        Args:
            symp:

        Returns:
            med
        """
        for num, med in self.data['English common name of herbal substance'].items():
            num_sym = self.search_sym(symp)
            if num == num_sym:
                return med


if __name__ == '__main__':
    data = CustomData(path='medicine_ayur.json')
    print(data.search_med('Urinary tract and genital disorders'))
