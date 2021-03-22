import json

class GetJson():
    def __init__(self):
        self.get()
   
    
    def get(self):
        with open("../data/dataset.json", 'r') as f:
            f = f.read()
            self.data = json.loads(f)

    
    def search(self, symtoms):
        searchList = []
        
        searchList = [x for x in self.data["Medicine"]]

        for i in searchList:
            if symtoms == self.data["Medicine"][i]["therapeuticuses"]:
                dose =  self.data["Medicine"][i]["dosage"]
                name = i
                return dose, name
            else:
                pass


if __name__ == "__main__":       
    data = GetJson()

    print(data.search("peptic ulcer poisoning leucorrhoea"))