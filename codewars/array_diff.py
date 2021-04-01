def array_diff(a, b):
    temp = []
    if b != []:
        for x in b:
            if a != x:
                print(a)
                temp.append(a)
        return(temp)

    else:
         return a


value = array_diff([1,2,2,4,5], [2,4])# == [2]
print(value)
#v = array_diff([1,2,2], [])
#print(v)
