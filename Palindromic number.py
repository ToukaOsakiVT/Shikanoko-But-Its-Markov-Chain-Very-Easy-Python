
default = int(10)

def swap(swaped = int):
    temp = str(swaped)[::-1]
    return int(temp)

def equals(check = str):
    if check == check[::-1]:
        return 1
    return 0


def main():
    base = default
    
    while (base < 100000):
        rslt = base
        print(str(base))
        count = int(0)
        while (not equals(str(rslt))):
            count += 1
            rslt = rslt + swap(rslt)
            print(str(rslt))
            if count > 100:
                break
        print ('-----')
        base += 1
        

main()