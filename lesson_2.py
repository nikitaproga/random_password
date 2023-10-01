import random

simvoli = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
nick_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nick_2 = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyz"
vvod = int(input("Введите длину пароля: "))
nick_3 = int(input("Введите длину ника: "))
xranit = ""
nick = ""

nick += random.choice(nick_1)

for i in range(vvod):
    xranit += random.choice(simvoli)

for i in range(nick_3-1):
    nick += random.choice(nick_2)

print("Ваш пароль", xranit)
print("Ваш ник", nick)