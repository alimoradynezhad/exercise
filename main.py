list =['11','pooya','10','15.5','12','23','45','reza','65.5','65','hamid']
lst2 =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 'x', 'w', 'y', 'z']
for x in list:
    if x[0] in lst2:
        continue
    elif '.' in x:
        continue
    else:
        print(x)