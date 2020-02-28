count = 0
with open("local_copy.log", "r") as f:
    for line in f:
        count += 1
print("The total number of requests made during the time of the log file.", count)