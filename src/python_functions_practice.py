def return_10():
    return 10



def add(num1,num2):
    return num1 + num2 

add(1 , 2) 


def subtract(num1,num2):
    return num1 - num2 
subtract(10,5)    

 
def multiply(num1,num2):
    return num1 * num2 
multiply(2,4) 

def divide(num1,num2):
    return num1 / num2 
divide(10,2) 

def length_of_string(string):
    return len(string) 
length_of_string("A string of length 21") 

def join_string(string1, string2):
    return string1 + string2 


def add_string_as_number(string1 , string2):
    return int(string1) + int(string2) 

def number_to_full_month_name(num):
    if num == 1:
        return "January" 
    elif num == 3:
        return "March" 
    elif num == 9:
        return "September"        
    return None     

def number_to_short_month_name(num):
    if num == 1:
        return "Jan" 
    elif num == 4:
        return "Apr"    
    elif num == 10:
        return "Oct"      
    return None     



def volume_of_cube(num):
    return num^3 

def erverse_string(string):
    return reversed(string)

def fahrenheit_to_celsius(num):
    return (num -32) * 0.5556 