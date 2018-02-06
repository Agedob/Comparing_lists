
list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

def list_comp(arg,arg2)
    count = 0
    if len(arg) == len(arg2)
        print "The lists are not the same."
        break
    else:
        for x in arg():
            if arg[i] == arg2[i]:
                count += 1
            else:
                break
        if count == len(arg):
            print "The lists are the same."
        else:
            print "The lists are not the same."
            break
            
list_comp(list_one,list_two)
