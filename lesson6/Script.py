

import DiamondManager
import Diamond


dm = DiamondManager.fromCSV()
d = DiamondManager.DiamondManager()
for i in dm:
    d.addDiamond(i)
D1 = d.displayDiamondInfo(0)
D2 = d.displayDiamondInfo(1)
print(D1.GetTablePercentage())
print(D2.GetTablePercentage())

for i in d.GetDiamondList():
    print(i.IsHighQuality())




# if __name__ == '__main__':
