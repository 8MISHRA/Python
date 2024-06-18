# my_list = [1,7,5,8,3,2,0,-1]
# def func(my_list):
#     """
#     returns lesser numbers than 5
#     """

#     copy = my_list[:]

#     for i in range (len(copy)-1):
#         if my_list[i] >= 5:
#             my_list.remove(my_list[i])

#     print(my_list)

# x = [1,7,5,8,3,2,0,-1]
# print(func(x))

# def cfbm(s):
#     '''
#     returns the count of how many times....

#     '''
#     x = 0
#     for i in range(len(s)//2):
#         if s [i] == s [len(s)-i-1]:
#             x = x + 1
#     return x

# print(cfbm('abcdefcba'))
            

# def find_composite(a, b):
#     '''
#     return a list of all non prime.....
#     '''
#     copy = []
#     for i in range (a, b+1):
#         if i > 3:
#             for x in range(3, i):
#                 if (i%x) == 0:
#                     copy = copy + [i]
#     return  [4] + copy

# print(find_composite(2, 10))

# def sumfold(my_list):
#     x = 0
#     for i in range (len(my_list)):
#         x = x + my_list[i]
#     return my_list

# print(sumfold(my_list))

# my_list = [[1,2,1], [1,2,6,7], [], [0]]
# def collapse(ragged):

#     x = []
#     if i in range (len (my_list)):
#         if len(my_list[i]) == 0:
#             x = x + [0.0]
#         else:
#             x = x + (math.fsum(my_list(i)))/len(my_list(i))
#     return x

# print(collapse(my_list))
