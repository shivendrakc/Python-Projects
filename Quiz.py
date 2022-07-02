import random  #importing random module
import operator as op  #importing operator module making op as it's alias 
#alias makes a subtitue for a keyword

print("What is your name?")
user = input()
print(f"Hello {user}. Let's start our quiz") #f means f-string which alllows us to add variable without having to use + sign 


score = 0
question = 10

def play():
    #since we imported radom module we can use random and randint is one of the func inside it
    x = random.randint(1, 50)
    y = random.randint(1, 50)

    opt = {
        #op means operater module as we created its alias from this module we are able to use add,sub,mul functions
        '+': op.add,
        '-': op.sub,
        '*': op.mul,
    }
    keys = list(opt.keys()) #creating a list of the keys 
    ops = random.choice(keys) #choosing a random key
    operation = opt[ops] #assigning that random key from the list
    answer = operation(x, y) #using one of the methods of operator module where operation is random key that will act as operator between x and y which are random number

    print(f"what is {x} {ops} {y} ?") 
    user_input = int(input())
    if user_input == answer:
        print("Correct Answer")
        return True
    else:
        print(f"Incorrect. the correct answer is {answer}")
        return  False

for i in range(question):
    if play():
        score += 1 

print(f"Congratulations, You have completed the quiz. you score is {score}/{question}")