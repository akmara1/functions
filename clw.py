#1

l = ['name', 'age', '1', '19']
def divide_list(list_1):
    m = int(len(list_1)/2)
    ls1 = list_1[:m]
    ls1.reverse()
    ls2 = list_1[m:]
    ls2.reverse()
    ls1.extend(ls2)
    print(ls1)
divide_list(l)


#2
num = int(input())
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1) + recur_fibo(n-2))
recur_fibo(num)
ls = []
for i in range(num):
    ls.append(recur_fibo(i))
print(ls)

#3
x,y = map(int,input().split())
def add(x,y):
    print(x+y)
def subscribe(x,y):
    print(x-y)
def mix(x,y):
    add(x,y)
    subscribe(x,y)
mix(x,y)

#11

def touch_file():
    name = input("name of file: ")
    file = open(f"{name}.txt", "w")
    file.write("hello world!")
    file.close()

touch_file()
#12
import random
def gen_number():
    ls = [1, 4, 5, 7, 9, 0]
    random.shuffle(ls)
    print("0444" + str(ls[0]) + str(ls[1]) + str(ls[2]) + str(ls[3]) + str(ls[4]) + str(ls[5]))
gen_number()
