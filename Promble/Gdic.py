studentss = {'Boss':{'Dismath':82,'Intro':90,'IntroLab':93,'Compro':90,'ComproLab':94,'SA':83,'Eng':80,'Human':79},
           'Chin':{'Dismath':82,'Intro':90,'IntroLab':93,'Compro':90,'ComproLab':94,'SA':83,'Eng':80,'Human':79},
           'Vas' :{'Dismath':82,'Intro':90,'IntroLab':93,'Compro':90,'ComproLab':94,'SA':83,'Eng':80,'Human':79},
           'Jez' :{'Dismath':0,'Intro':51,'IntroLab':61,'Compro':71,'ComproLab':81,'SA':66,'Eng':77,'Human':58},
           'Tub' :{'Dismath':82,'Intro':90,'IntroLab':93,'Compro':90,'ComproLab':94,'SA':83,'Eng':80,'Human':79}, 
           'Nine':{'Dismath':82,'Intro':90,'IntroLab':93,'Compro':90,'ComproLab':94,'SA':83,'Eng':80,'Human':79}, 
           }



def main():
    while True:
        print('''Please select option -
        1. ViewAll
        2. InsertData
        3. Update/ModifyData
        4. DeleteData
        5. SearchData
        Enter other for exit program''')
        select_options = int(input('Select operations form 1,2,3,4,5 : '))
        if select_options == 1:
            display_student(studentss)
        elif select_options == 2:
            insert_student(studentss)
        elif select_options == 3:
            edit_student(studentss)
        elif select_options == 4:
            delete_student(studentss)
        elif select_options == 5:
            search_student(studentss)
        else:
            return 
def display_student(student):
    for name in student.keys():
        print(name)
        for sub in student[name].keys():
            print(sub,student[name][sub])
        print()
def insert_student(student):
    numstd = int(input('How many student add : '))
    for i in range(numstd):
        namenew = input('What name : ')
        student[namenew] = {}
        sub = int(input('How many subject add : '))
        for j in range(sub):
            subject = input('Subject name : ')
            score = int(input('What score : '))
            student[namenew].update({subject:score})   

def edit_student (student):
    for i in student.keys():
        print(i,end='  ')
    print()
    namenew = input('What name : ')
    print(namenew," :",end='')
    if namenew in student: 
        for i in student[namenew]:
            print(i,student[namenew][i],end='  ')
        print()

        subject = input('Subject name : ')
        score = int(input('What score : '))
        if subject in  student[namenew]:
            student[namenew].update({subject:score}) 
        else :
            print("Don't have this subject name")
    else:
         print("Don't have this student name")

def delete_student(student):
    print('''Delete Option
          1. Delete subject
          2. Delete student
          Enter other for exit program''')
    choice = int(input('Select operations form 1,2,3,4 : '))
    if choice == 1:
        deletesubject(studentss)
    elif choice == 2:
        deletestd(studentss)
    else:
        pass

def deletesubject(student):
    for i in student.keys():
        print(i,end='  ')
    print()   
    namenew = input('What name : ')
    print(namenew," :",end='')
    if namenew in student: 
        for i in student[namenew]:
            print(i,student[namenew][i],end='  ')
        print()
        
        subject = input('Subject name : ')
        if subject in  student[namenew]:
            student[namenew].pop(subject) 
        else :
            print("Don't have this subject name")
    else:
        print("Don't have this student name")    
def deletestd(student):
    for i in student.keys():
        print(i,end='  ')
    print()
    namenew = input('What name : ') 
    if namenew in student: 
        student.pop(namenew) 
    else:
        print("Don't have this student name")    
def search_student(student):
    for i in student.keys():
        print(i,end='  ')
    print() 
    namenew = input('What name : ')
    print(namenew," : ",end='')
    if namenew in student: 
        for i in student[namenew]:
            print(i,student[namenew][i],end='  ')
        print()
    else:
         print("Don't have this student name")
main()