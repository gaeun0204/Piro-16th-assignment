
studentsInfo = []


class NumofDataError(Exception):
    def __init__(self):
        super().__init__('Num of data is not 3!')

class AlreadyExistNameError(Exception):
    def __init__(self):
        super().__init__('Already exist name!')

class Student():
    def __init__(self, name, midscore, finalscore):
        self.name = name
        self.midscore = midscore
        self.finalscore = finalscore
        self.grade = 0


def Menu1(name, midscore, finalscore):
    #사전에 학생 정보 저장하는 코딩
    studentsInfo.append(Student(name, midscore, finalscore))

def Menu2():
    #학점 부여 하는 코딩
    for i in range(len(studentsInfo)):
        if studentsInfo[i].grade == 0:
            avg = (studentsInfo[i].midscore + studentsInfo[i].finalscore) / 2
            if avg >= 90:
                studentsInfo[i].grade = 'A'
            elif avg >= 80:
                studentsInfo[i].grade = 'B'
            elif avg >= 70:
                studentsInfo[i].grade = 'C'
            else:
                studentsInfo[i].grade = 'D'

def Menu3():
    #출력 코딩
    print('\n------------------------------------')
    print('name\tmid\tfinal\tgrade')
    print('------------------------------------')
    for i in range(len(studentsInfo)):
        print('{0}\t{1}\t{2}\t{3}'.format(studentsInfo[i].name, studentsInfo[i].midscore, studentsInfo[i].finalscore, studentsInfo[i].grade))

def Menu4(delname):
    #학생 정보 삭제하는 코딩
    for i in range(len(studentsInfo)):
        if studentsInfo[i].name == delname:
            del studentsInfo[i]
            break # 반드시 써줘야 함! 삭제 후에 len(studentsInfo)의 값이 달라지므로 그대로 두면 'list index out of range' 에러 발생.


#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 sore2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")

while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")

    if choice == "1":
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출

        try:
            data = input('Enter name mid-score final-score : ').split() # 입력데이터 리스트에 저장

            if len(data) != 3: # 예외처리: 데이터 입력 개수가 3개인지
                raise NumofDataError

            for i in range(len(studentsInfo)): # 예외처리: 이미 존재하는 이름인지
                if studentsInfo[i].name == data[0]:
                        raise AlreadyExistNameError

            try: # 예외처리: 입력 점수 값들이 양의 정수인지
                data[1] = int(data[1])
                data[2] = int(data[2])
            except:
                raise ValueError('Score is not positive integer!')
            if (data[1] < 1) or (data[2] < 1):
                raise ValueError('Score is not positive integer!')

            Menu1(data[0], data[1], data[2]) # 예외사항이 아닌 경우만 1번 함수 호출
        except Exception as e:
            print(e)

    elif choice == "2":
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력
        if not studentsInfo:
            print('No student data!')
        else:
            Menu2()
            print('Grading to all students.')
    
    elif choice == "3":
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출
        if not studentsInfo:
            print('No student data!')
        else:
            flag = 0
            for i in range(len(studentsInfo)):
                if studentsInfo[i].grade == 0:
                    flag = 1
                    break
            if flag == 1:
                print("There is a student who didn't get grade.")
            else:
                Menu3()        

    elif choice == "4":
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
        if not studentsInfo:
            print('No student data!')
        else:
            delname = input('Enter the name to delete : ')
            flag = 0
            for i in range(len(studentsInfo)):
                if studentsInfo[i].name == delname:
                    flag = 1
                    break
            if flag == 0:
                print('Not exist name!')
            else:
                Menu4(delname)
                print(delname, 'student information is deleted.')

    elif choice == "5":
        print('Exit Program!')
        break;

    else:
        print('Wrong number. Choose again.')
