

def c_to_f(c):
    if(isinstance(c,int) or isinstance(c,float)):
        return c * 1.8 + 32
    else:
        return "0.00: Invalid value for celsuis provided"
    # return Fahrenheit for a Celsius value
    



def f_to_c(c):
    if(isinstance(c,int) or isinstance(c,float)):
        return (c - 32) / 1.8
    else:
        return "0.00: Invalid value for fahrenheit provided"
    # return Celsius for a Fahrenheit value
    
    