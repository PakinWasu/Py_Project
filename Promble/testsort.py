def selectionSort(score):
    for fillslot in range(len(score)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if score[location]<score[positionOfMax]:
                positionOfMax = location
        tempa = score[fillslot]
        score[fillslot] = score[positionOfMax]
        score[positionOfMax]= tempa
    

stdcore = [90,50,80,70,100,70]
selectionSort(stdcore)
print(stdcore)


def sequentialSearch(liscore,score):
    pos = 0
    keepo = []

    while pos < len(liscore) :
        if liscore[pos] == score:
            keepo.append(pos)
        
        pos += 1
    return keepo

print(sequentialSearch(stdcore,70))