import csv
import os.path
import Diamond
class DiamondFileNotFoundError(Exception):
    """File Not Found"""
class DiamondFileFormatError(Exception):
    """Couldn't Read The File"""
def fromCSV():
    try:
        if not os.path.exists('diamonds.csv'):
             raise DiamondFileNotFoundError()
    except DiamondFileNotFoundError:
        print("File Not Found")
    else:
        with open('diamonds.csv', mode='r') as File:
            try:
                csvFile = csv.reader(File)
                if csvFile is None:
                    raise DiamondFileFormatError()
            except DiamondFileFormatError:
                   print("Couldn't Read The File")
            else:
                diamondList = []
                flag = 0
                for lines in csvFile:
                     if flag > 0:
                           d = Diamond.Diamond(float(lines[6]), float(lines[0]), (lines[1]), (lines[6]), (lines[3]),
                                            float(lines[7]), float(lines[8]), float(lines[9]), float(lines[5]))
                           diamondList.append(d)
                     else:
                        flag = 1
            return diamondList



class DiamondManager:
    def __init__(self):
        self.listDiamonds = []



    def addDiamond(self, diamond):
        self.listDiamonds.append(diamond)

    def displayDiamondInfo(self, index):
        ls = self.listDiamonds[index]
        ls.DisplayInfo()
        print("table percentage" + str(ls.GetTablePercentage()) + "highquality" + str(ls.IsHighQuality()) + "CalculateVolume" + str(ls.CalculateVolume()))
        return ls
    def GetDiamondList(self):
        return self.listDiamonds