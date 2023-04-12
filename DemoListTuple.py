# DemoListTuple.py
color = ["red", "blue", "green"]
print(type(color))
print(len(color))
color.append("yellow")
print(color)
color.insert(1, "white")
color += "red"
print(color)
print(color.pop())
print(color.pop())
color.remove("red")
print(color)

print("---set연습---")
a={1,2,3,3}
b={3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print("---tuple---")
tp = (100,200,300)
print(type(tp))
print(len(tp))
print("id :%s, name :%s" % ("kim", "김유신"))

def times(a,b):
    return a+b, a*b

#호출
print(times(3,4))

print("---형식변환---")
a=set((1,2,3))
print(a)
b=list(a)
b.append(4)
print(b)
c=tuple(b)
print(c)

 