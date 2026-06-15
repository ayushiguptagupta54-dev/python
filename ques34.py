# FIND REPEATED ELEMENTS IN A TUPLE
t = (1,2,3,4,5,6,7,8,9,3,4,)
repeated = []
for item in t:
    if t.count(item)  > 1 and item not in repeated:
        repeated.append(item)
        print("repeated elemnets:", repeated)

        