var="This is a global variable since is not present within a function!"

def fun(arg):
    return None

def fun_with_default_value(arg_with_default_value = None):
    return None

def fun_with_tuple_arg(*arg):
    return None

def fun_with_dictionary_arg(**arg):
    return None

def fun_with_list_arg(l):
    l.append(3)

nl = [1, 2]
fun_with_list_arg(nl)
print(nl)

def add(a, b):
    return a + b