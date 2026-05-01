'''
12345
1234
123
12
1
'''

def pattern(n):
    for i in range(1 , n+1 ):
        for j in range(1 , n+2-i):
            print(j , end="")
        print()

pattern(5)