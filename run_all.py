from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)
count = 0
with open("local_copy.log", "r") as f:
    for line in f:
        count += 1
print("The total number of legit requests made during the time of the log file.", count)


fileID = open("local_copy.log",'r')

fileID.seek(0)

vector = []
dic = {}
for line in fileID:
    vector = line.split()
    if len(vector) ==10:
        vector = vector[3].split(':')
        vector = vector[0]
        vector = vector[1:]
        if dic.get(vector, -1) == -1:
            dic[vector] = 1
            
        else:
            dic[vector] +=1
print(dic)  


fileID = open("local_copy.log",'r')

fileID.seek(0)

vector = []
dic = {}
for line in fileID:
    vector = line.split()
    if len(vector) ==10:
        vector = vector[3].split(':')
        vector = vector[0]
        vector = vector[3:]
        if dic.get(vector, -1) == -1:
            dic[vector] = 1
            
        else:
            dic[vector] +=1
print(dic)

fileID = open("local_copy.log",'r')

fileID.seek(0)

vector = []
dic = {}
for line in fileID:
    vector = line.split()
    if len(vector) ==10:
        vector = vector[8]
        if dic.get(vector,-1) == -1:
            dic[vector] = 1
        else:
            dic[vector] +=1
total = 0
grandtotal = 0
for item, value in dic.items():
    grandtotal += value
    if item[0] == '4':
        print(item, value)
        total += value
print("The total number of errors is", total)
percent = total / grandtotal * 100
print("The percentage of errors is",percent,'%')

fileID = open("local_copy.log",'r')

fileID.seek(0)

vector = []
dic = {}
for line in fileID:
    vector = line.split()
    if len(vector) ==10:
        vector = vector[8]
        if dic.get(vector,-1) == -1:
            dic[vector] = 1
        else:
            dic[vector] +=1
total = 0
grandtotal = 0
for item, value in dic.items():
    grandtotal += value
    if item[0] == '3':
        print(item, value)
        total += value
print("The total number of redirections is", total)
percent = total / grandtotal * 100
print("The percentage of redirections is",percent,'%')