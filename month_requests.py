
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