fileID = open("local_copy.log",'r')

fileID.seek(0)

vector = []
dic = {}
for line in fileID:
    vector = line.split()
    if len(vector) ==10:
        vector = vector[6]
        if dic.get(vector,-1) == -1:
            dic[vector] = 1
        else:
            dic[vector] +=1
print(vector)