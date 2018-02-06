
list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

def list_comp(arg, arg2):
    count = 0
    if len(arg) != len(arg2):
        print "The lists are not the same."
    else:
        for x in range(0, len(arg), 1):
            if arg[x] == arg2[x]:
                count = count + 1
            else:
                break
        if count == len(arg):
            print "The lists are the same."
            print count
        else:
            print "The lists are not the same."
            print count

list_comp(list_one,list_two)
