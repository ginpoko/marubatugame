def board(arrange):

    print(arrange[0],arrange[1],arrange[2],sep='|')
    print('-+-+-')
    print(arrange[3],arrange[4],arrange[5],sep='|')
    print('-+-+-')
    print(arrange[6],arrange[7],arrange[8],sep='|')
    print()

def judge(arrange):
    if arrange[0] == arrange[1] == arrange[2]:
        return 0
    elif arrange[3] == arrange[4] == arrange[5]:
        return 0
    elif arrange[6] == arrange[7] == arrange[8]:
        return 0
    elif arrange[0] == arrange[3] == arrange[6]:
        return 0
    elif arrange[1] == arrange[4] == arrange[7]:
        return 0
    elif arrange[2] == arrange[5] == arrange[8]:
        return 0
    elif arrange[0] == arrange[4] == arrange[8]:
        return 0
    elif arrange[2] == arrange[4] == arrange[6]:
        return 0
    else:
        return 1



def maru(arrange):
    number = input('input a number in 0~8: ')
    print('')
    int_number = int(number)
    arrange[int_number] = '◯'
    board(arrange)
    judge(arrange)
    maru_judge = judge(arrange)
    if maru_judge ==0:
        return 'w'
    else:
        return 'l'

def batsu(arrange):
    number = input('input a number in 0~8: ')
    print('')
    int_number = int(number)
    arrange[int_number] = '×'
    board(arrange)
    judge(arrange)
    bathu_judge = judge(arrange)
    if bathu_judge ==0:
        return 'w'



