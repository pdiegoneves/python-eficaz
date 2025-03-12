# Evite usar blocos else depois de laços for e while
for i in range(3):
    print(f'Loop {i}')
    if i == 1:
        print('Loop Break!')
        break
else:
    print('Else block!')


print("-----")
for i in range(3):
    print(f'Loop {i}')
else:
    print('Else block!')


print("-----")
for x in []:
    print('Never runs')
else:
    print('For Else block!')


