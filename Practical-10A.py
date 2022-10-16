#Write a program to derive the predicate.

import heapq as hq
my_dict = {'z': 'zebra', 'b': 'ball', 'w': 'whale',
           'a': 'apple', 'm': 'monkey', 'c': 'cat'}

my_list = [(k, v) for k, v in my_dict.items()]

print("Before organizing as heap :", my_list)
hq.heapify(my_list)

print("After organizing as heap :", my_list)
my_dict = dict(my_list)

print("Resultant dictionary :", my_dict)
import heapq as hq
my_dict = {'z': 'zebra', 'b': 'ball', 'w': 'whale',
           'a': 'apple', 'm': 'monkey', 'c': 'cat'}
my_list = [(k, v) for k, v in my_dict.items()]

print("Before organizing as heap :", my_list)
hq.heapify(my_list)

print("After organizing as heap :", my_list)
my_dict = dict(my_list)

print("Resultant dictionary :", my_dict)

import heapq as hq
my_dict = [{'z': 'zebra'}, {'b': 'ball'}, {'w': 'whale'},
           {'a': 'apple'}, {'m': 'monkey'}, {'c': 'cat'}]


my_list = [(k, v) for i in my_dict for k, v in i.items()]

print("Before organizing as heap :", my_list)

hq.heapify(my_list)

print("After organizing as heap :", my_list)
my_dict = dict(my_list)
print("Resultant dictionary :", my_dict)
import heapq as hq
class employee:
    def _init_(self, n, d, yos, s):
        self.name = n
        self.des = d
        self.yos = yos
        self.sal = s
    def print_me(self):
        print("Name :", self.name)
        print("Designation :", self.des)
        print("Years of service :", str(self.yos))
        print("salary :", str(self.sal))
    def _lt_(self, nxt):
        return self.yos < nxt.yos
e1 = employee('Yuvraj', 'manager', 3, 24000)
e2 = employee('Shaban', 'programmer', 2, 15000)
e3 = employee('Vinith', 'Analyst', 5, 30000)
e4 = employee('Iqram', 'programmer', 1, 10000)
emp = [e1, e2, e3, e4]
hq.heapify(emp)
for i in range(0, len(emp)):
    emp[i].print_me()
    print()