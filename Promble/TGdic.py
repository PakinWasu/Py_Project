studentss = {'Boss':{'Dismath':82,'Intro':90,'IntroLab':93,'Compro':90,'ComproLab':94,'SA':83,'Eng':80,'Human':79},
           'Chin':{'Dismath':82,'Intro':90,'IntroLab':93,'Compro':90,'ComproLab':94,'SA':83,'Eng':80,'Human':79},
           'Vas' :{'Dismath':82,'Intro':90,'IntroLab':93,'Compro':90,'ComproLab':94,'SA':83,'Eng':80,'Human':79},
           'Jez' :{'Dismath':0,'Intro':51,'IntroLab':61,'Compro':71,'ComproLab':81,'SA':66,'Eng':77,'Human':58},
           'Tub' :{'Dismath':82,'Intro':90,'IntroLab':93,'Compro':90,'ComproLab':94,'SA':83,'Eng':80,'Human':79}, 
           'Nine':{'Dismath':82,'Intro':90,'IntroLab':93,'Compro':90,'ComproLab':94,'SA':83,'Eng':80,'Human':79}, 
           }

def display_student(std):
    for name in std.keys():
        print(name)
        for sub in std[name].keys():
            print(sub,std[name][sub])
        print()
def insert_student(student):
    numstd = int(input('How many student add : '))
    for i in range(numstd):
        namenew = input('What name : ')
        student[namenew] = {}
        sub = int(input('How many subject add'))
        for j in range(sub):
            subject = input('Subject name : ')
            score = int(input('What score : '))
            student[namenew].update({subject:score})   

delete_student(studentss)
display_student(studentss)