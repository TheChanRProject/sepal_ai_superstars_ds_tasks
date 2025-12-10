from functools import reduce

def dot_prod(x: list[int], y: list[int]) -> int:

    return reduce(lambda a,b: a+b, map(lambda x: x[0] * x[1], zip(x, y)))

result = dot_prod([1,2,3], [4,5,6])

print(result)

def dot_prod_v2(x: list[int], y: list[int]) -> int:

    return sum(map(lambda x: x[0] * x[1], zip(x,y)))

result = dot_prod_v2([1,2,3], [4,5,6])

print(result)

class list(list):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def dot(self, other_list: list[int]) -> int:
        return sum(map(lambda x: x[0] * x[1], zip(self, other_list)))

x: list = list([1,2,3])

result = x.dot(other_list=[4,5,6])

print(result)