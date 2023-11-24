i=2
b=lambda x, i=i: x%i==0
print(b(2))
i=3
print(b(2))
b=2
print(callable(b))