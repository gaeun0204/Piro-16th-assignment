class InputRangeError(Exception):
    def __init__(self):
        super().__init__('1,2,3 중 하나를 입력하세요')

def InputCount():
    while 1:
        try:
            global cnt
            cnt = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
            if (cnt < 1 or cnt >= 4):
                raise InputRangeError
            break
        except ValueError:
            print('정수를 입력하세요')
        except InputRangeError as e:
            print(e)

num = 0

InputCount() # playerA 입력
for i in range(cnt):
    num += 1
    print('playerA :', num)

InputCount() # playerB 입력
for i in range(cnt):
    num += 1
    print('playerB :', num)
