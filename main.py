list = [
        [[1,2,5,6,2],
        [1,2,5,6,2]],

        [[1,2,5,6,5],
        [1,2,5,6,5,3]],

        [[1,2,5,6,5,16],
        [1,2,5,6,5]],

        [['celery','carrots','bread','milk'],
        ['celery','carrots','bread','cream']]
]

def list_comp(arg, arg2):
    count = 0
    if len(arg) != len(arg2):
        print("The lists are not the same.")
    else:
        for x in range(0, len(arg), 1):
            if arg[x] == arg2[x]:
                count = count + 1
            else:
                break
        if count == len(arg):
            print("The lists are the same.")
            print(count)
        else:
            print("The lists are not the same.")
            print(count)

list_comp(list[0][0], list[0][1])

# print(list[0])
