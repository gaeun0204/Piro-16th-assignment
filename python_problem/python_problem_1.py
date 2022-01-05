from random import randint

class InputRangeError(Exception):
    def __init__(self):
        super().__init__('1,2,3 중 하나를 입력하세요')

def brGame(who):
    global num
    global turn

    turn = who

    if turn == 'computer':
        cnt = randint(1, 3)
    else:
        while 1:
            try:
                cnt = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
                if (cnt < 1 or cnt >= 4):
                    raise InputRangeError
                break
            except ValueError:
                print('정수를 입력하세요')
            except InputRangeError as e:
                print(e)

    for i in range(cnt):
        num += 1
        print('{0} {1}'.format(turn, num))
        if num >= 31:
            break;


global num
num = 0
global turn

while num < 31:
    brGame('computer')

    if num >= 31: # 예외처리: 종료조건
        break;

    brGame('player')

if turn == 'player':
    print('computer win!')
else:
    print('player win!')
