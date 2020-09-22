import setting

arrange = ['0','1','2','3','4','5','6','7','8']
counter = 0
print('marubatsu game\n'
      'select a number in board')

setting.board(arrange)
print('START')


while range(4):
    main_maru_judge = setting.maru(arrange)
    if main_maru_judge == 'w':
        print('You are Winner!')
        counter +=1
        break
    else:
        print('Next turn')
    main_bathu_judge = setting.batsu(arrange)
    if main_bathu_judge == 'w':
        print('You are Winner!')
        counter +=1
        break
    else:
        print('Next turn')


if counter == 0:
    main_maru_judge = setting.maru(arrange)
    if main_maru_judge == 'w':
        print('You are Winner!')
    else:
        print('DRAW')
# 入力エラー　丸バツを入れ替えることができるバグ



