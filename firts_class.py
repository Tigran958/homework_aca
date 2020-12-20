# 1. Calculator in polish notation
# Create a calculator with following requirements:
#   * support following mathematical operations: + - * /
#   * operations can be specified both with signs and names (add: +; sub: -; mul: *; div: /),
#   * operands can be both integers and floats,
#   * the operations must be written in polish notation: + 2 3,
#   * user must be prompted for a single input containing the expression in polish notation,
#   * operators and the operands can be separated by arbitrary number of spaces,
#   * all inputs must be in strict format (everything must be checked and validated),
#   * usage of exceptions is prohibited.
#   * create logging directory and file in that directory
#      1. for exceptions text must be "{system datetime} :: ERROR :: {exception message} :: {input parameters}"
#      2. for information text must be "{system datetime} :: INFO :: {input parameters} :: {result}"
#   * print report about logs after result
# Example:
#     Expression: + 2 3
#     Result: 5
#     Report: INFO-1, ERROR-0
#     Expression: a b
# ERROR: Invalid expression
#     Report: INFO-1, ERROR-1

import os
from datetime import datetime

file_dir = os.path.join(os.getcwd(),'calculator_logs')
file_path = os.path.join(file_dir,'action_logs.txt')

if not os.path.exists(file_dir):
    os.mkdir(file_dir)


expression = input("Tell the numbers: \nex. + 2 5\n")
operators = (('add', '+'), ('sub', '-'), ('mul', '*'), ('div', '/'))

def log_message(time, type_, params, message,):
    return F"{time} :: {type_} :: {message} :: {params}\n"

check = True

while check:
    current_time = datetime.now()
    with open(file_path, 'a') as log_file:
        modified_expres = expression.split()

        if len(modified_expres) == 3:
            operator_ = modified_expres[0]
            passed = False
            for i in operators:
                if operator_ in i:
                    passed = True
            if passed:
                
                valid_ = True
                first = tuple(modified_expres[1]).count('.')
                second = tuple(modified_expres[2]).count('.')
                if first > 0:
                    if first > 1:
                        reason = "Wrong Format"               
                        log_file.write(log_message(current_time, "ERROR", reason, expression))
                        print(f'Expression: {expression}\nResult: "ERROR"\nReport: INFO-0, ERROR-1\n{reason}')
                        valid_ = False
                    else:
                        if modified_expres[1].replace(".","").isdigit() and modified_expres[1] != '.':
                            first_number = float(modified_expres[1])
                        else:
                            reason = "You should write only ints or floats (1.1)"
                            log_file.write(log_message(current_time, "ERROR", reason, expression))
                            print(f'Expression: {expression}\nResult: "ERROR"\nReport: INFO-0, ERROR-1\n{reason}')
                            valid_ = False
                else:
                    if modified_expres[1].isdigit():
                        first_number = int(modified_expres[1])
                    else:
                        reason = "You should write only ints or floats (1.1)"
                        log_file.write(log_message(current_time, "ERROR", reason, expression))
                        print(f'Expression: {expression}\nResult: "ERROR"\nReport: INFO-0, ERROR-1\n{reason}')
                        valid_ = False

                if second > 0:
                    if second > 1:
                        reason = "Wrong Format"               
                        log_file.write(log_message(current_time, "ERROR", reason, expression))
                        print(f'Expression: {expression}\nResult: "ERROR"\nReport: INFO-0, ERROR-1\n{reason}')
                        valid_ = False
                    else: 
                        if modified_expres[2].replace(".","").isdigit() and modified_expres[2] != '.':
                            second_number = float(modified_expres[2])
                        else:
                            reason = "You should write only ints or floats (1.1)"
                            log_file.write(log_message(current_time, "ERROR", reason, expression))
                            print(f'Expression: {expression}\nResult: "ERROR"\nReport: INFO-0, ERROR-1\n{reason}')
                            valid_ = False
                else:
                    if modified_expres[2].isdigit():
                        second_number = int(modified_expres[2])
                    else:
                        reason = "You should write only ints or floats (1.1)"
                        log_file.write(log_message(current_time, "ERROR", reason, expression))
                        print(f'Expression: {expression}\nResult: "ERROR"\nReport: INFO-0, ERROR-1\n{reason}')
                        valid_ = False

                if valid_:
                    if operator_ in operators[0]:
                        result = first_number + second_number           
                    elif operator_ in operators[1]:
                        result = first_number - second_number           
                    elif operator_ in operators[2]:
                        result = first_number * second_number 

                    else:
                        if second_number != 0:
                            result = first_number / second_number
                        else:
                            reason = 'ZeroDIvisionError'
                            log_file.write(log_message(current_time, "ERROR", reason, expression))
                            valid_ = False

                    if valid_:
                        log_file.write(log_message(current_time, "INFO", result, expression))


                        print(f'Expression: {expression}\nResult: {result}\nReport: INFO-1, ERROR-0\n')
                            
            user_answer = input("for quit press: q")

            if user_answer == "q":
                check = False   
                    

        else:
            reason = "Wrong Format"               
            log_file.write(log_message(current_time, "ERROR", reason, expression))
            print(f'Expression: {expression}\nResult: "ERROR"\nReport: INFO-0, ERROR-1\n{reason}')
            
            user_answer = input("for quit press: q")

            if user_answer == "q":
                check = False 





