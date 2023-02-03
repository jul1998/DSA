# #Assigning Functions to Variables
# def first_function(str):
#     return "I am" + str
#
# print(first_function(" the first function"))
#
#
# #Defining Functions Inside other Functions
# def first_function(str):
#     def second_function(str):
#         return "I am" + str
#
#
#     result = second_function(str)
#     return result
# print(first_function(" an inner function"))
#
# # Passing Functions as Arguments to other Functions
# def first_function(str):
#     """This function uses as parameter the string defined in the second_function_call"""
#     return "I am" + str
#
# def second_function_call(function):
#     """This function uses as parameter the first_function"""
#     str_to_add = " the first function"
#     return function(str_to_add)
#
# print(second_function_call(first_function))
#
# # Functions Returning other Functions
#
# def function_hello():
#     """This function returns what the say_hi function returns"""
#     def say_hi():
#         return "Hi, I am an inner function"
#     return say_hi()
#
# print(function_hello())
#
# # Nested Functions have access to the Enclosing Function's Variable Scope
# def print_message(message):
#     "Enclosong Function"
#     def message_sender():
#         "Nested Function"
#         print(message)
#
#     message_sender()
#
# #Creating Decorators
# def uppercase_decorator(function):
#     def wrapper():
#         """This inner function will modify whatever the function that is passed
#             as argument in uppercase_decorator returns.
#         """
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#
#     return wrapper
#
#
# @uppercase_decorator
# def say_hi():
#     return 'hello there'
#
# print(say_hi())
#
a = {1:9, 2:8, 3:7, 4:6, 5:5}
print(a.items())

try:
    print([1, 2, 3][4])
except IndexError:
    print("IndexError raised")
except:
    print("Exception raised")
else:
    print("Something else happened")
finally:
    print("Cleaning up")