l = [1,3,"abc",4,False]

for ele in l:
    if type(ele) == int:
        print(ele + 10)
        continue
    elif type(ele) != int:
        exit
print("i'M OUTSIDE OF THE LOOP")