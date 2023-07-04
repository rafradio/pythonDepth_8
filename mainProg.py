import sys
from Serialisation import Serialisation as SRLZ
from DumpToFiles import DumpToFiles as DMPF

def main(args):
    data = args[1] if len(args) > 1 else 'firstdir'
    srlz = SRLZ(data)
    srlz.walkDir(data)
    dmpf = DMPF(srlz.dictFolders, data)
    dmpf.dumpToJson()
    dmpf.dumpToCSV()
    # for key, value in srlz.dictFolders.items():
    #     print(f'{key}: {value}')

if __name__ == '__main__':
    main(sys.argv)