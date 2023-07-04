import os
from pathlib import Path
import shutil

class Serialisation:
    def __init__(self, dir):
        self.DIR = dir
        self.dictFolders = {}

    def walkDir(self, dirName, parent='main folder', type='folder'):
        
        size = 0
        parentPath = os.path.join(os.getcwd(), parent) if parent != 'main folder' else os.getcwd()
        key = dirName.replace(str(parentPath), '')
        self.putFolderInfo(key, parent)

        dirNameFull = os.path.join(os.getcwd(), dirName)

        dir_tupple = list(os.walk(dirNameFull))[0]
        if len(dir_tupple[1]) > 0:
            for d in dir_tupple[1]:
                size += self.walkDir(dir_tupple[0] + '\\' + d, str(dirName))

        if len(dir_tupple[2]) > 0:
            size += self.putFileInfo(dir_tupple)

        # print(key, size)
        self.dictFolders[key]['size'] = size

        return size
    
    def putFolderInfo(self, key, parent):
        self.dictFolders[key] = {}
        self.dictFolders[key]['type'] = 'folder'
        self.dictFolders[key]['parent'] = parent.replace(str(os.getcwd()), '')
        

    def putFileInfo(self, dir_tupple):
        size = 0
        for f in dir_tupple[2]:
            self.dictFolders[f] = {}
            self.dictFolders[f]['type'] = 'file'
            self.dictFolders[f]['parent'] = dir_tupple[0].replace(str(os.getcwd()), '')
            pathFile = os.path.join(dir_tupple[0], f)
            self.dictFolders[f]['size'] = os.path.getsize(pathFile)
            size += os.path.getsize(pathFile)

        return size
