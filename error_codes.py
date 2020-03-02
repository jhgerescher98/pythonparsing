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


        
