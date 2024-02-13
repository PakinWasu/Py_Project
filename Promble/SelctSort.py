def selectionSort(score,name):
    for fillslot in range(len(score)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if score[location]<score[positionOfMax]:
                positionOfMax = location
        tempa = score[fillslot]
        score[fillslot] = score[positionOfMax]
        score[positionOfMax]= tempa

        tempb = name[fillslot]
        name[fillslot] = name[positionOfMax]
        name[positionOfMax] = tempb
def sequentialSearch(liscore,score):
    pos = 0
    keepo = []

    while pos < len(liscore) :
        if liscore[pos] == score:
            keepo.append(pos)
        
        pos += 1
    return keepo
Stdnum = int(input('Enter the number of students: '))
Stdname= []
Stdnscore = []
for i in range(Stdnum):
    Stdname.append(input('Enter student name: '))
    Stdnscore.append(int(input('Enter student score: ')))

selectionSort(Stdnscore,Stdname)

print('-- Sorted Scores (Selection Sort) --')
for i in range(len(Stdname)):
    print(Stdname[i],' : ',Stdnscore[i])
print('-- Top 3 Highest Scores --      ')
for i in range(3):
    print(Stdname[i],' : ',Stdnscore[i])
print('-- Top 3 Lowest Scores --')
for i in range(len(Stdnscore)-1,len(Stdnscore)-4,-1):
    print(Stdname[i],' : ',Stdnscore[i])

scoreSearch = int(input('Enter the score to search: '))
print('Found student with score',scoreSearch,':')
for i in sequentialSearch(Stdnscore,scoreSearch):
    print(Stdname[i],' : ',Stdnscore[i])