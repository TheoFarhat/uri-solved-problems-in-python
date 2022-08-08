n = float(input())

n100 = n // 100
n_atual = n % 100
n50 = n_atual // 50
n_atual1 = n_atual % 50
n20 = n_atual1 // 20
n_atual2 = n_atual1 % 20
n10 = n_atual2 // 10
n_atual3 = n_atual2 % 10
n5 = n_atual3 // 5
n_atual4= n_atual3 % 5
n2 = n_atual4 // 2
n_atual5 = n_atual4 % 2
n1 = n_atual5 // 1
n_atual6 = n_atual5 % 1
n050 = n_atual6 // (1/2)
n_atual7 = n_atual6 % (1/2)
n025 = n_atual7 // (1/4)
n_atual8 = n_atual7 % (1/4)
n010 = n_atual8 // (1/10)
n_atual9 = n_atual8 % (1/10)
n005 = n_atual9 // (1/20)
n_atual10 = n_atual9 % (1/20)
n_atual11 = round(n_atual10,3) + 0.001
n001 = n_atual11 // (1/100)


print("NOTAS:")
print(f"{n100:.0f} nota(s) de R$ 100.00")
print(f"{n50:.0f} nota(s) de R$ 50.00")
print(f"{n20:.0f} nota(s) de R$ 20.00")
print(f"{n10:.0f} nota(s) de R$ 10.00")
print(f"{n5:.0f} nota(s) de R$ 5.00")
print(f"{n2:.0f} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{n1:.0f} moeda(s) de R$ 1.00")
print(f"{n050:.0f} moeda(s) de R$ 0.50")
print(f"{n025:.0f} moeda(s) de R$ 0.25")
print(f"{n010:.0f} moeda(s) de R$ 0.10")
print(f"{n005:.0f} moeda(s) de R$ 0.05")
print(f"{n001:.0f} moeda(s) de R$ 0.01")