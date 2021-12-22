import os


os.chdir("../pythontest/pytest")
with open("set.txt", mode="r", encoding=("utf-8")) as f:
    lst = f.readlines()

lsts = []
for i in lst:
    s = i.strip()
    lsts.append(s)

print(set(lsts))
