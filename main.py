from function import display_month

#รอบสุดท้าย
input_number = input("Enter Value:")
print("Type is number ? :",input_number.isnumeric())
try:
    #int(input_number)
    try:
        input_number = int(input_number)
        print("is number")
    except:
        input_number = float(input_number)
        print("is float")
except:
    input_number = str(input_number)
    print("is string")
result = display_month(input_number)
print("Output is :",result)



#รอบ3
# input_number = input("Enter Value:")
# print("Type is number ? :",input_number.isnumeric())
# try:
#     #int(input_number)

#     if type(float(input_number))== float:
#         input_number = float(input_number)
#     elif input_number.isalpha():
#         result = display_month(input_number)
#     else:
#         input_number = int(input_number)
#     print("Is number")
#     print(input_number)
# except:
#     input_number = str(input_number)
#     print("Is string")
# result = display_month(input_number)
# print("Output is :",result)





#รอบ2
# input_number = input()
# if input_number.isnumeric():
#     if type(input_number) == float:
#         input_number = float(input_number)
#     elif input_number.isalpha():
#         result = display_month(input_number)
#     else:
#         input_number = int(input_number)
# result = display_month(input_number)
# print("Output is :",result)




#รอบ1
# input_number = int(input())
# print(type(input_number))
# result = display_month(input_number)
# print(result)

# input_number = input()
# if input_number.isdigit():
#     input_number = int(input_number)
#     result = display_month(input_number)
#     print("month is :",result)
# else:
#     print("Invalid input. Please enter a number.")

