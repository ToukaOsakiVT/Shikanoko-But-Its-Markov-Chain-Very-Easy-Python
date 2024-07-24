import random

rslt = []

def Shi():
    rslt.append('し')
    rand = random.randint(0,1)
    if rand == 0:
        Ka()
    else:
        Ta()

def Ka():
    rslt.append('か')
    No()

def No():
    rslt.append('の')
    Ko()

def Ko():
    rslt.append('こ')
    rand = random.randint(0,3)
    if rand == 0:
        Shi()
    elif rand == 1:
        Ko()
    else:
        No()

def Ta():
    rslt.append('た')
    Nn()

def Nn():
    rslt.append('ん')
    rand = random.randint(0,1)
    if rand == 0:
        Ta()
    else:
        Air()

def Air():
    rslt.append('ﾊﾟｧｰﾝ')
    rand = random.randint(0,1)
    if rand == 0:
        Air()


def main():
    Shi()
    print(rslt)

main()
