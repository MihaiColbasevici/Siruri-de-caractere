s = input('Dati sirul de caractere: ')
a = 0
for i  in s:
    if i == 'A':
        a += 1
print(a)
s_b = s.replace('A', '*')
print(s_b)
s_c = s.replace('B', '')
print(s_c)
ma = 0
for j in s:
    if j == 'M' and s[s.index(j) + 1] == 'A':
        ma += 1
print(ma)
s1 = s[:]
for k in s1:
    if k == 'M' and s1[s1.index(k) + 1] == 'A':
        s1 = f"{s1[:s1.index(k)]}{'T'}{s1[s1.index(k) + 1:]}"
print(s1)
s2 = s[:]
for l in s2:
    if l == 'T' and s2[s2.index(l) + 1] == 'O':
        s2 = f"{s2[:s2.index(l)]}{s2[s2.index(l) + 2:]}"
print(s2)
print(s[::-1])