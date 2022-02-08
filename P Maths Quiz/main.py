
import random
from random import randint
import datetime 


def Response():
    print("\n \n Basic Mathematical Quiz")
    print("_________________________________\n")
    
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        print("A very good morning to you")
    elif hour >= 12 and hour < 18:
        print("Are you enjoying your afternoon?")
    elif hour >=18 and hour <24:
        print("A very lovely evening it is")
    else:
        print("Good day")
        
   
    print("\n \t Quiz Instructions")
    print("---------------------")
    print(""" 
          1. Every question has 25 marks
          2. You are expected to attempt all questions
          3. You need to score a minimum of 50% to pass this quiz
          4. Please attempt all questions
          
          """)
    
    print("\n Continue?")
    
    print("""
          
          1. Yes
          2. No 
          
          """)
    
Response()

def exam():
    correct_answer = "Corect"
    wrong_answer = "Wrong"
    final_score = 0
    
    try:
        #Question 1
        a = randint(503,892)
        b = randint(10589, 45981)
        c = a * b
        print("first number", a)
        print('second number', b)
        question_one = input("What is the result of the second number divided by the first mumber: " )

        
        if float(question_one) == c:
            print(correct_answer)
            final_score += 25
        else:
            print(wrong_answer)
        
        
        #Question 2
        question_two = input("If a number is divided by 4, then 3 is subtracted, the result is 0. What is the number?: ")
        answer_two = 12
        
        if int(question_two) == answer_two:
            print(correct_answer)
            final_score += 25
        else:
            print(wrong_answer)
        
        #question3
        question_three = input("What is 10004 divided 33?: ")
        answer_three = 303.151
        answer_three_2 = 3.1515
        answer_three_3 = 3.15
        answer_three_4 = 3.152
        if float(question_three) == answer_three or float(question_three) == answer_three_2 or float(question_three) == answer_three_3 or float(question_three) == answer_three_4:
            print(correct_answer)
            final_score += 25
        else:
            print(wrong_answer)
        
        #Question 4
        question_four = input("If 1=3, 2=3, 3=5, 4=4, 5=4, what is 6?: ")
        answer_four = 3
        
        if int(question_four) == answer_four:
            final_score += 25
        else:
            print(wrong_answer)
      
    
            
        if final_score >= 50:
            print("Congratulations, you have scored", final_score) 
        else:
            print("Would you like to make another attempt, you have scored below the approved threshold", final_score)
    except ValueError:
        print(wrong_answer)
        
try:
    def consent_func():
        consent_reply = input("Would you like to proceed?: ")
        if int(consent_reply) == 1:
            exam()
        elif int(consent_reply) == 2:
            print("\n Come back next time")
        else:
            print("\n Would you like to quit?")
    consent_func()
except ValueError:
        print("\n This is not part of the instructions")
        print("\n THE END")       
