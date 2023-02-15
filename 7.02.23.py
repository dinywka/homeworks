#1
strr = "Hello world"
def stand_sort(strr):
    strr1 = ''.join(strr.split())
    listt = strr1.lower()
    return sorted(listt)

print(stand_sort(strr))

def buddle_sort(strr):
    strr1 = ''.join(strr.split())
    strr = strr1.lower()
    listt = []
    fin_list = []
    for i in range(len(strr)):
        listt. append(ord(strr[i]))
    for i in range(len(listt)-1):
        for j in range(0, len(listt) - i -1):
            if listt[j] > listt[j+1]:
                listt[j], listt[j+1] = listt[j+1], listt[j]
    for i in range(len(listt)):
        fin_list.append(chr(listt[i]))
    return(fin_list)

print(buddle_sort(strr))