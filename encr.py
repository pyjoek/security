alph = "abcdefghijklmnopqrstuvwxyz"

size = len(alph)
name = "abc"
passwd = ""

for i in name:
    index = alph.find(i)
    if (int(index) + 13) <= 25:
        index += 13
        passwd += alph[index]
    else:
        news = 26 - (index + 13)
        passwd += alph[abs(news)]

print(passwd)
