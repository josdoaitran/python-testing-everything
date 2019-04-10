from pip._vendor.distlib.compat import raw_input


def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(raw_input())
print (fact(x))

#----------------------------------------#

