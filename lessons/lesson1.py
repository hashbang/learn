import re

def start():
    print """
          Hi! Welcome to #! learn\n
  
          We will start by introducing some basics of using the shell\n
          
          Lets first start with the "echo" command.\n
          
          Try "echo Hello World"\n
          """
    answer = raw_input("$ ")
    correct = False

    while not(correct):
        if re.match(r"^echo ", answer):
            print answer[5:]
            if answer[5:].lower() == 'hello world':
                print "Correct!"
                correct = True
                break
            else:
                answer = raw_input("$ ")
        else:
            print "That command is invalid. Try 'echo Hello World'"
            answer = raw_input("$ ")
        
if __name__ == "__main__":
    start()