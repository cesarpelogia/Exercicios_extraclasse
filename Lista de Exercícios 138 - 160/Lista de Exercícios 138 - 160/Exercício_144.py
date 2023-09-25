saldoM=float(input("\nDigite seu saldo médio do ultimo ano: "))

if (saldoM <= 500):
    credito = 0

elif (saldoM > 500 and saldoM <= 1000):
    credito = saldoM * 0.3
elif (saldoM > 1000 and saldoM  <=3000):
    credito = saldoM * 0.6
else:
    credito = saldoM * 0.5

if (credito == 0):
    print(f"\nComo seu saldo era: {saldoM}, seu crédito será de {credito}.")

else:
    print(f"\nComo seu saldo era de {saldoM}, seu crédito sera de {credito}.")