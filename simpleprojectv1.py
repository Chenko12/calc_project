restart = True

def check_restart():
    flag = input(''' do you want to calculate another numbers?
               	            enter yes for calculate again
               	            insert no for close the program''')

    if flag == "yes":
        flag = True
        return flag
    else:
        flag = False
        return flag

def calculate_sum(first_number, second_number):
   sum = first_number + second_number
   return sum

def calculate_sub(first_number, second_number):
  sub = first_number - second_number
  return sub
 
def calculate_mul(first_number, second_number):
  mul = first_number * second_number
  return mul 

def calculate_div(first_number, second_number):
  if second_number != 0:
      div = first_number / second_number
      return div
  else:
    print("You can't divide by zero! please try again")
  
print("Hello welcome to my calculator please follow the instructions below")

while restart:
    user_inputA = input('Hello please enter your first number \n')
    user_inputA = int(user_inputA)
    user_inputB = input('now insert another one \n')
    user_inputB = int(user_inputB)

    user_choice = input('''please choose:
        		                 1. for sum
        		                 2. for dif
        		                 3. for mul
        		                 4. for div\n''')
    user_choice = int(user_choice)

    if user_choice == 1:
        user_result = calculate_sum(user_inputA, user_inputB)
        print(f"your sum is {user_result}\n")

        restart = check_restart()

    elif user_choice == 2:
        user_result = calculate_sub(user_inputA, user_inputB)
        print(f"your dif is {user_result}\n")

        restart = check_restart()

    elif user_choice == 3:
        user_result = calculate_mul(user_inputA, user_inputB)
        print(f"your mul is {user_result}\n")

        restart = check_restart()

    elif user_choice == 4:
        user_result = calculate_div(user_inputA, user_inputB)
        print(f"your div is {user_result}\n")

        restart = check_restart()





