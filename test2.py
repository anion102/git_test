#master edit information
class Welcome1:
    def __init__(self):
        pass  # will be ignored

    def __init__(self, name):
        pass           # define mutiple constructors is not available, the last init will be the valid method


# hello = Welcome()
welcome = Welcome1('name')


class Welcome2:

    def __init__(self, name='max'):    # argument with default value
        print(name)

welcome2 = Welcome2()
welcome21 = Welcome2('jenny')


class Welcome3:

    def __init__(self, *args, **kwargs):  # uncertain number argument and dictionary argument defined
        print(args)
        print(kwargs)


hello = Welcome3()
welcome3 = Welcome3('name','ah', name='jenny',age=27)
# testing2 change  to merge into master
