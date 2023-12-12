def basic_operations(a,b):
    output={}
    try:
        a=float(a)
        b=float(b)
        try:
            output['division']=a/b
        except ZeroDivisionError:
            print('\n\t_ERROR_ Division by zero is not allowed: in basic_operations\n')
        output['addition']=a+b
        output['subtration']=a-b
        output['multiplication']=a*b
    except ValueError:
        print('\n\t_ERROR_ renter only a number: in basic_operations\n')
    return output
            


def power_operation(base, exponent, **kwargs):
    try:
        base=float(base)
        exponent=float(exponent)
        powered=(base**exponent)
        modulo=0
        if 'modulo' in kwargs:
            try:
                modulo=float(kwargs['modulo'])
                powered=powered%modulo
            except ValueError:
                print('\n\t_ERROR_ please enter only a number: in power_operations, modulo\n')
        return powered
    except ZeroDivisionError:
        print('\n\t_ERROR_ division by zero is not allowed: in power_operations, modulo\n')

    
    

def apply_operations(operations):
    def each(my_tuple):
        lambda_func=my_tuple[0]
        x=my_tuple[1][0]
        y=my_tuple[1][1]
        return lambda_func(x,y)
    
    output=map(each, operations)
    return list(output)
