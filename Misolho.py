# misoli № 1
# def domo(a):
#         return ''.join([c*2 for c in a])
# print(domo(str(input())))   




# misoli № 2
# def doro(file):
#         with open(file, 'r+') as file:
#             m = file.read()
#         k = m.lower().split().count("the")
#         return k
# file = "notes.txt"
# l = doro(file)
# print(f"The word 'the' occurs {l} times.")





# misoli № 3
# def sorik(file):
#         with open(file, 'r') as file:
#             c = file.read()
#         a = c.split()
#         m = sum(1 for word in a if word.endswith('e'))
#         return m
# file = "notess.txt"
# e = sorik(file)
# print(f"The number of words ending with 'e' is {e}.")




# misoli № 4
# def solo(file):
#         with open("my_file.txt", 'r+') as file:
#             c = file.read()
#         w = c.split()
#         d = w.count("this")
#         k = w.count("these")
#         return d, k
# file = "my_file.txt"
# d, k = solo(file)
# print(f"The word 'this' occurs {d} times.")
# print(f"The word 'these' occurs {k} times.")




# misoli № 5
# def google(a):
#         if a < 0:
#             return "invalid"
#         elif a == 1:
#             return "Google"
#         else:
#             return f"G{'o' * a}gle"
# print(google(int(input())))



# misoli № 6
# def function(n, m):
#     return any(n in i for i in m)
# a = input()
# list1 = a.split(',')
# list1 = [word.strip() for word in list1]
# d = input()
# print(function(d, list1))





# misoli№ 7
# def solo(n):
#     a = n // 6
#     t = n + a
#     return t
# print(solo(int(input()))) 




# misoli№ 8
# def kolo(a):
#     if len(a) == 0:
#         return ""
#     return a[0] + a[-1]
# print(kolo(str(input())))




# misoli № 9
# def func(a):
#     return a.endswith('s')
# print(func(str(input())))
