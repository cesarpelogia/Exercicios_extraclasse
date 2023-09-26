import math as m

pi = 3.14
ang = float(input("\nDigite o ângulo em graus: "))
rang = ang * pi / 180

if (rang > pi / 2 and rang <= pi or rang > 3*pi/2 and rang <= 2*pi):
    print(f"\nSeno: {m.sin(rang):.5f}")

else:
    print(f"\nCo-seno: {m.cos(rang):.5f}")

