
from weChart.config.VarConfig import *

thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")

# thislist.insert(1,"ooo")
thislist.insert(-1,"1ooo")
# thislist.insert(-1,["ooo"])
# print(thislist)

# file_path=  "D:\\Users\\Admin\\PycharmProjects\\weChart\\weChart"






with open(filePath, "w", encoding="utf-8")as f:
    for i  in thislist:
        # i = str(i).strip('[').strip(']').replace("","").replace("","")
        i = str(i).strip('[').strip(']').replace("","").replace("","")
        print(i)
        f.write(i+",")

