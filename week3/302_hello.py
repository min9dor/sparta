a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for even in a_list:
    if even % 2 == 0:
        print(even)

def question(n):
    b_list = range(1, n)
    for i in b_list:
        if i % 2 == 0:
            print(i)
question(100)

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

def count_fruit(x):
    count = 0
    for fruit in fruits:
        if fruit == x:
            count += 1
    print(count)

count_fruit('배')
count_fruit('사과')


