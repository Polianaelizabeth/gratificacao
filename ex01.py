horasE = float(input("Horas extras: "))
horas = float(input("horas que faltou: "))

Hminutos: float = (horasE - (2 / 3 * horas)) * 60

if Hminutos < 600:
    premio = float = 100
elif 600 <= Hminutos <= 1200:
    premio = 200
elif 1201 <= Hminutos <= 1800:
    premio = 300
elif  1801 <= Hminutos <= 2400:
    premio = 400
else:
    premio = 500

print("horas extras: ", horasE, " Horas que devia: ", horas, "premio", premio)


