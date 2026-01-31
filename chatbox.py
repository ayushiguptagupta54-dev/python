import	google.generativeai	as	ai	
mykey	=	"YOUR_API_KEY"	
ai.configure(api_key=mykey)	
model	=	ai.GenerativeModel("gemini-1.5-pro")	
chat	=	model.start_chat()	
while	True:	
message = input("User: ")	
if(msg=="bye"):	
print("Chatbot:	Good	Bye")	
break	
result	=	chat.send_message(message)	
print("Chatbot:	",	result.text)	
Steps to Run: 
1. Save the Python script as chatbot.py. 
2. Open a terminal and navigate to the script locati