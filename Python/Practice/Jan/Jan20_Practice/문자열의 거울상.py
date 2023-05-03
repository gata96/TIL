T = int(input())

for t in range(1, T+1):
    case = input()
    text = ''

    for i in case[::-1]:
        if i == 'p':
            text += 'q'
        elif i == 'q':
            text += 'p'
        elif i == 'd':
            text += 'b'
        else:
            text += 'd'

    print(f'#{t} {text}')
            