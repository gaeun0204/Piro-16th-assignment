class InputRangeError(Exception):
    def __init__(self):
        super().__init__('1,2,3 중 하나를 입력하세요')

def brGame(who):
    global num
    global player

    player = who # 현재 순서인 player 저장

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
        print('player{0} : {1}'.format(player, num))
        if num >= 31:
            break;


global num
num = 0
global player

while num < 31:
    brGame('A')

    if num >= 31:
        break;

    brGame('B')

if player == 'A':
    print('playerB win!')
else:
    print('playerA win!')
