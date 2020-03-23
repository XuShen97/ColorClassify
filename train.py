import math
import torch as t

# read trainData
x_py = []
y_py = []
m = 1
for aLine in open("trainData.txt"):
    temp1 = int(aLine[1:3], 16)
    temp2 = int(aLine[3:5], 16)
    temp3 = int(aLine[5:7], 16)
    temp = [1, temp1, temp2, temp3]
    x_py.append(temp)
    y_py.append(int(aLine[8]))
    m += 1
m -= 1

# init of param
x = t.tensor(x_py, dtype=t.float)
y = t.tensor(y_py, dtype=t.float)
theta = t.tensor([[-1], [-1], [-1], [-1]], dtype=t.float)
alpha = 0.00001
epsilon = 1e-3


# define of functions

def h(ax):
    global theta
    return 1 / (1 + math.exp(0 - theta.t().mm(ax.t()).item()))


def cost(ax, ay):
    return -ay * math.log2(h(ax)) - (1 - ay) * math.log2(1 - h(ax))


def j():
    sumTemp = 0
    for i in range(1, m):
        sumTemp += cost(x[i:i+1], y[i].item())
    return sumTemp / m


def updateTheta():
    global theta
    global alpha
    sumTemp = t.tensor([[0], [0], [0], [0]], dtype=t.float)
    for i in range(1, m):
        sumTemp += (h(x[i:i+1]) - y[i].item()) * x[i:i+1].t()
    theta = theta - alpha * sumTemp / m


# main loop
tempJ1 = j()
updateTheta()
tempJ2 = j()
print("Train running...")
print("It only needs several seconds...")
while math.fabs(tempJ1 - tempJ2) > epsilon:
    tempJ1 = tempJ2
    updateTheta()
    tempJ2 = j()


#############################
#           test            #
#############################
resultFile = open("testResult.txt", "w+")
for aLine in open("testData.txt"):
    resultFile.write(aLine[:-1])
    aColor = t.tensor([[1], [int(aLine[1:3], 16)], [int(aLine[3:5], 16)], [int(aLine[5:7], 16)]], dtype=t.float)
    if theta.t().mm(aColor).item() > 0:
        resultFile.write(" 1\n")
    else:
        resultFile.write(" 0\n")

resultFile.close()