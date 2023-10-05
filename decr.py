alph = "abcdefghijklmnopqrstuvwxyz"

size = len(alph)
name = "nop"
passwd = ""

for i in name:
    index = alph.find(i)
    if (index - 13) <= 0:
        index = 13 - index
        passwd += alph[index]
    else:
        news = index - 13
        passwd += alph[abs(news)]

print(passwd)
