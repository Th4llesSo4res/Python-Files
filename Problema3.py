Np = 0  
Mp = 0.0    

for _ in range(6):
    N = float(input())  

    if N > 0:
        Np += 1  
        Mp += N

print(f"{Np} valores positivos")

media = Mp / Np
print(f"{media:.1f}")
