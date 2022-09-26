import csv
import random
import math

kineticLabel = {
    "cartwheeling" : 0,
    "golf chipping": 1,
    "golf driving" : 2,
    "golf putting": 3,
    "push up": 4,
    "situp": 5,
    "somersaulting": 6
}
def folderName(n):
    if n == "golf chipping" or n == "golf driving" or n == "golf putting":
        return "golf"
    else:
        return n.replace(" ", "")

with open('annotations.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

kinecticed = [[kineticLabel[item[0]], folderName(item[0])+"/"+item[1]+".mp4"] for item in data[1:]]
random.shuffle(kinecticed)

idx = math.floor((len(kinecticed) * 0.9))

train = kinecticed[:idx]
validate = kinecticed[idx:]


with open('train.txt', 'w') as f:
    for line in train:
        f.write(line[1] + " " + str(line[0]) + '\n')

with open('validate.txt', 'w') as f:
    for line in validate:
        f.write(line[1] + " " + str(line[0]) + '\n')