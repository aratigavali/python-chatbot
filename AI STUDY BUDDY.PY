#RULE BASED AI PYTHON CHATBOT 

import datetime 
import time 



name = input ("hii! , please enter your name : ")
presenthour = datetime.datetime.now().hour 

if 5 <= presenthour <= 11 :
    print("good morning dear " , name)
elif 11 <= presenthour <= 17:
    print("good afternoon dear " , name)
elif 17 <= presenthour <= 20 :
    print("good evening dear ", name )
else:
    print("good night dear ", name )


print("======== NAMASTE ! ========")

print("welcome to your chatbot!")
print("you can ask me basic question ,  type 'bye' to exit from the chatbot ")

#chatbot memory creation (dictionary of response )

responses = {
    "hello" : "hi welcome . how can i help you ? ",
    "how are you": "i am very  fine . thank you ",
    "who are you" : "i am smart ai chatbot" ,
    "motivate me" : "keep going , EVERY BUG OF YOUR PROJECT MAKES YOU A BETTER DEVELOPER",
    "happy" : "great to hear that ☺ ",
    "sad":"dont worry all is well!",
    "what is python":"python is programming langauge ",
    "hi":"hello",
    "study plan":"umm tell me about ur timetable",
    "bye":"okk have a good day ! ",
    "coding":"developer do the coding in different languages..",
    "explain machine learning": "Machine Learning is a branch of AI that allows computers to learn patterns from data and make predictions.",
    "what is ai": "AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.",
    "study tips": "Study regularly, make short notes, practice questions, and take small breaks.",
    "exam preparation": "Start with important topics, revise your notes, practice previous questions, and manage your study time.",
    "python": "Python is a popular programming language used for web development, data analysis, automation, AI and Machine Learning."
    
}
#method / function to response of chatbot 

def getresponse(userquestion):
    userquestion = userquestion.lower().strip()

   #special response for emotion : 

    if "sad" in userquestion:
        return "ohhh  dont worry ! all is welll !!"
    
    elif "happy" in userquestion:
        return "ohooooooo !! i am so happy to hear that !"

    elif "study" in userquestion:
        return "Study Tip: Choose one topic, study for 25 minutes, take a 5-minute break, and then revise what you learned."

    elif "quiz" in userquestion:
        return "Quiz Time! What is the full form of AI?"

    elif "explain python" in userquestion:
        return "Python is a high-level programming language known for its simple syntax. It is widely used in AI, Machine Learning, Data Science, and web development."

    elif "explain machine learning" in userquestion:
        return "Machine Learning is a branch of AI where computers learn patterns from data and use them to make predictions or decisions."

    elif "explain ai" in userquestion:
        return "Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence, such as learning, reasoning, and problem-solving."

    #normal  question 
    for eachkey in responses:
        if eachkey in userquestion:
           return responses[eachkey]

    return "sorry i am not able to tell that yet , i will learn that soon ! "


   
#take user input 

  



while True : 

    userinput = input("please ask your question :  ")

    if "quiz" in userinput.lower():
        print("🧠 Quiz Time!")
        answer = input("What is the full form of AI? ")

        if answer.lower().strip() == "artificial intelligence":
            print("🎉 Correct! Well done!")
        else:
            print("❌ Not quite. The correct answer is Artificial Intelligence.")

        continue

    reply = getresponse(userinput)

    time.sleep(1)

    print("bot response : " , reply)



    if "bye" in userinput.lower():
        break 
