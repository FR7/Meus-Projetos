# escreva um programa que leia um valor em metros e a exiba convertida em centímetros e milímetros.

medida = float(input("Uma distância em metros: "))

dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000
print("A medida de {} m corresponde a {:.0f} decímetros, {:.0f} centímetros e {:.0f} milímetros".format(medida, dm, cm, mm))
print("A medida de {} m corresponde a {:.3f} decâmetros, {:.3f} hectômetros e {:.3f} kilômetros".format(medida, dam, hm, km))