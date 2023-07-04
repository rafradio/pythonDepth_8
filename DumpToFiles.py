import json

class DumpToFiles:

    def __init__(self, obj, dirName):
        self.obj = obj
        self.dirName = dirName

    def dumpToJson(self):
        fileName = str(self.dirName) + '_to_json.json'
        with open(fileName, 'w') as f:
            print(json.dumps(self.obj, indent=4), file=f)
        