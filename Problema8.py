N = int(input())

h = N // 3600 
N = N % 3600

m = N // 60
s = N % 60

print(f"{h}:{m}:{s}")