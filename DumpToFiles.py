import os
import json, csv, pickle


class DumpToFiles:

    def __init__(self, obj, dirName):
        self.obj = obj
        self.dirName = dirName
        self.PATH = os.path.join(os.getcwd(), 'DumpedFiles')

    def dumpToJson(self):
        fileName = str(self.dirName) + '_to_json.json'
        fileNameFull = os.path.join(self.PATH, fileName)
        with open(fileNameFull, 'w') as f:
            print(json.dumps(self.obj, indent=4), file=f)
        
    def dumpToCSV(self):
        fileName = str(self.dirName) + '_to_csv.csv'
        fileNameFull = os.path.join(self.PATH, fileName)
        data = [["id", "name", "type", "parent", "size"]]
        i = 0
        for key, value in self.obj.items():
            data.append([i, key] + [x for x in value.values()])
            i += 1


        with open(fileNameFull, 'w', newline='', encoding='utf-8') as f_write:
            writer = csv.writer(f_write, dialect='excel', quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerows(data)

    def dumpToPickle(self):
        fileName = str(self.dirName) + '_to_pickle.picle'
        fileNameFull = os.path.join(self.PATH, fileName)
        with open(fileNameFull, 'wb') as f:
            pickle.dump(self.obj, f)
        
