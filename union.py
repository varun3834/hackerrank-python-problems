english=int(input())         #eng vaale
Etotal=set(map(input()," ".split()))
french=int(input())
Ftotal=set(map(input()," ".split()))
# uni=Etotal.union(Ftotal)
# total=len(uni)
print(len(Etotal.union(Ftotal)))
# total=len(Etotal.union(Ftotal))
# print(total)