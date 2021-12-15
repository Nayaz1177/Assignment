def divby7():
    nl=[]
    for x in range(2000, 3201):
        if (x%7==0) and (x%5!=0):
            nl.append(str(x))
    print (','.join(nl))


def divby7lst():
    lst = [i for i in range(2000, 3201) if i % 7 == 0 if i % 5 != 0]
    print(lst)

divby7()
divby7lst()


