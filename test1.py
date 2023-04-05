import builtins
# exception class location
# exception is an unexpected event that disrupts the normal flow of program
# examples: TypeError, NameError, AttributeError,....

result = None
try:
    a = float(input("NUmber 1: "))
    b = float(input("NUmber 2: "))
except Exception as e:
    print("Error: ", e)
    print("Error: ", type(e))

try:
    result =a / b
except ZeroDivisionError as ex:
    print("Error=", ex)
else:
    print('__else__')      # else statement will be executed when except statement is not executed
finally:
    print('__finally__')   # finally statement will be executed whether exception happens or not;
    # can use it to close files, close connection or re-connect with database, redis
    # or other thing important needed to do with or without exception

print(result)
print("end")