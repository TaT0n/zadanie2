spis = ['qqq', 'eee', 'eee', 'rrr', 'ttt', 'yyy', 'qqq', 'www']
nspis = []  # создание нового списка
for i in spis:
    if i not in nspis:
        nspis.append(i)
print(nspis)
