abc = ('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z').split()
num = int(input())
for c in range(0, num):
    if c == 0:
        print(f'{abc[c] * 1}')
    else:
        c += 1
        print(f'{abc[c - 1] * c}')


