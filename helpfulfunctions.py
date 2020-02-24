#complex unit sqrt(-1)
i = 1j
j = 1j
#average of the list
def avg(list):
    sum_list = 0
    n = 0
    for i in list:
        sum_list+=i
        n+=1
    return sum_list / n
#round number to closest integer
def round(num):
    if float(num)-int(float(num))<0.5 :
        return int(float(num))
    if float(num)-int(float(num))>=0.5:
        return int(float(num))+1
#encryptes message
def encryption(key):
    alphabet='qrupwtiey-oax2fb3jml1szdc 5gvhnk;#6^07(!$&)@%8*,.9-4?:_"/`-+'
    string=input('Enter string: ')
    len_string=len(string)
    key=int(key)
    repeated=0
    for char  in string:
        spot=alphabet.find(char)
        lenght=len(alphabet)

        new=(spot+len_string*key+int(pow(key,key)))%lenght
        if repeated<len(string)-1:
            print(new,end=',')
            repeated+=1
        else:
            print(new)
#decryptes message
def decryption(list):
    alphabet = 'qrupwtiey-oax2fb3jml1szdc 5gvhnk;#6^07(!$&)@%8*,.9-4?:_"/`-+'
    key=int(input('Enter key: '))
    decrypt_list=[]
    #appends what will happen to symbol after encryption
    for i in range(int(len(alphabet))):
        decrypt_list.append((i+len(list)*key+pow(key,key))%len(alphabet))
    #compares indexes of both and checks the other list what's on that index
    for i in list:
        index_list=decrypt_list.index(i)
        print(alphabet[index_list],end='')
#quadratic_equation using quadratic formula
def quadratic_equation(a,b,c):
    x1=(-b+pow(pow(b,2)-4*a*c,0.5))/2*a
    x2=(-b-pow(pow(b,2)-4*a*c,0.5))/2*a
    print('First solution is',x1)
    print('Second solution is',x2)
def factorial(n):
    x=1
    for i in range(1,n+1):
        x*=i
    print(x)
