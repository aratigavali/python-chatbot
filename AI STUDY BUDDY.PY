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
    "coding":"developer do the coding in different languages.."
    
}
#method / function to response of chatbot 

def getresponse(userquestion):
    userquestion = userquestion.lower().strip()

   #special response for emotion : 

    if "sad" in userquestion:
        return "ohhh  dont worry ! all is welll !!"
    elif "happy" in userquestion:
        return "ohooooooo !! i am so happy to hear that !"

    #normal  question 
    for eachkey in responses:
        if eachkey in userquestion:
           return responses[eachkey]

    return "sorry i am not able to tell that yet , i will learn that soon ! "


   
#take user input 

  



while True : 

    userinput = input("please ask your question :  ")
    reply = getresponse(userinput)

    time.sleep(1)

    print("bot response : " , reply)



    if "bye" in userinput.lower():
        break 