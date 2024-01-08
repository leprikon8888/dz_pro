#простые числа от1 до n
# def me_func(n):
#     for i in range(2, n+1):
#         for j in range(2,i):
#             if i%j == 0:
#                 break
#         else:
#             yield i
#
#
# for x in me_func(100):
#     print(x)
#
# a = list(me_func(8))
# print(a)

n = 10
x = (i for i in range(2, n+1) if all(i % j != 0 for j in range(2, i)))

for i in x:
    print(i)


x = (i for i in range(2, n+1) if all(i % j != 0 for j in range(2, i)))
for i in x:
    print(i)