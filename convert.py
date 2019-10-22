#GNU Genel Kamu Linsansi ile lisanslanmistir
#Author: Burak Shen
#Date: 22.10.2019

import inquirer

values = [
    "bit",
    "kilobit",
    "megabit",
    "gigabit",
    "terabit",
    "petabit",
    "byte",
    "kilobyte",
    "megabyte",
    "gigabyte",
    "terabyte",
    "petabyte"
]
#values2 = [
#    1,
#    1000,
#    1000*1000,
#    1000*1000*1000,
#    1000*1000*1000*1000,
#    1000*1000*1000*1000*1000,
#    8,
#    8*1000,
#    8*1000*1000,
#    8*1000*1000*1000,
#    8*1000*1000*1000*1000,
#    8*1000*1000*1000*1000*1000
#]

questions = [
    inquirer.List("type", message="Girilecek tip", choices=values)
]
answers = inquirer.prompt(questions)

questions2 = [
    inquirer.Text("type", message="Girilen deger", choices=values)
]
answers2 = inquirer.prompt(questions2)

questions3 = [
    inquirer.List("type", message="Cikacak tip", choices=values)
]
answers3 = inquirer.prompt(questions3)

def calculation(a):
    if a==0 :
        return 1
    elif a!=6:
        c=1
        for b in range(a):
            c=c*1000
        if(a>6):
            c=c*8
        return c
    else:
        return a*8

for i, value in enumerate(values):
    if(answers["type"] == value):
        printing1 = calculation(i)*int(answers2["type"])
for i, value in enumerate(values):
    if(answers3["type"] == value):
        printing2 = calculation(i)*int(answers2["type"])
print(printing1/printing2*int(answers2["type"]))
