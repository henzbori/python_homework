# Task 1: Diary

import traceback

try:
    with open('diary.txt', 'a') as file:
        content = input("What happened today?")
        file.write(content + "\n") 
        while True:
            content = input("What else?")
            if content.lower() == 'done for now':
                break
            file.write(content + "\n")  
except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
    else:
        print("Content to be appended to the file.")
