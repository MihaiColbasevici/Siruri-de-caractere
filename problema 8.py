sir = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z Z"
p1 = ""
for i in sir:
    a = chr(ord(i)+1)
    p1 += a
    b = p1.replace('!',' ')
    c = b.replace('[','Z')
print(c)
for j in sir:
    sir2 = sir.replace('Z', 'A')
print(sir2)
for k in sir:
    sir3 = sir.replace(' ', '-')
print(sir3)
