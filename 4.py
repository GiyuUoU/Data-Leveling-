'''
1
22
333
4444
55555
'''

def pattern(N):
    for i in range(1 , N+1):
        for j in range( 1 , i+1):
            print(i , end="")
        print()

pattern(5)