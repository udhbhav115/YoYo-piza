	
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
 
app = Flask(__name__,)
 
english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("data/data1.yml")
lst=[]
@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    #print(userText)
    #if len(lst)!=0:
    #    print(lst[-1])
    #if(len(lst)!=0 and "phone" in lst[-1]):
    #    print("first if")
    #   if(userText.lower()=="okay"):
    #       return "Please enter your details"
    #   else:
    #       return "please enter okay"
    #lst.append(str(english_bot.get_response(userText)))
    return str(english_bot.get_response(userText.lower()))
 
 
if __name__ == "__main__":
    app.run()