from flask import Flask,render_template,request,jsonify
import flask
import sign_up,generalFunctions
from botocore.exceptions import ClientError
from Crypto.Cipher import AES
import signal,sys
from threading import Thread
import json
import sock
application= Flask(__name__, template_folder='templates')
socketio=None
searching=[]
socket=sock.init(app=application)
searching=[]

socket2=Thread(target=sock.findChat)
socket2.daemon=True
socket2.start()

@application.route("/",methods=['POST','GET'])
def home_page():
   return render_template('mainPage_v2.html')

@application.route("/login",methods=['POST'])
def login():
   usr=None
   password=None 
   if request.method=="POST":
      if request.form.get("request")=="sign-up":
         usr=request.form.get("username")
         password=request.form.get("password")
         print(usr,password) 
         if usr!=None:  
            response=sign_up.signup(usr,password)
            print(response)
            if response['status']=='authorized':
               response['message']={"usr":usr,"password":password}
               print("\n KEKEWKKWEKEWKEKW\n",response['message'])
               response['message'] = generalFunctions.encrypt(json.dumps((response['message']))).decode()
            print("fav moment")
            print(jsonify(response))
            return jsonify(response)
         else:
            response['status']='huh'
            return jsonify(response)
      elif request.form.get("request")=="login":
         usr=request.form.get("username")
         password=request.form.get("password")
         if usr!=None:  
            response=dict()
            response['status']=sign_up.checkUser(usr,password)
            if response['status']=="authorized":
               response['message']={"usr":usr,"password":password}
               response['message'] = generalFunctions.encrypt(json.dumps((response['message']))).decode()
            return jsonify(response)
         else:
            response['status']='huh'
            return jsonify(response)





@application.route("/loadPage",methods=['POST'])
def loadPage():
   page=request.form.get("page")
   chatId=request.form.get("id")
   if chatId:
      return render_template(page,val=chatId+"-chat",val2=chatId+"-load",val3=chatId+"-inp",val4=chatId+"-list")

   return render_template(page)



@application.route("/generalFunctions",methods=['POST'])
def genFunc():
   print('kekws')
   if request.method=="POST":
      req=request.form.get("req")
      if req=="checkUser":
         usr=request.form.get("user")
         usr=json.loads(generalFunctions.decrypt(usr.encode()))

         print(usr['usr'])
         return sign_up.checkUser(usr['usr'],usr['password'])
@application.route("/sendMsg",methods=['POST'])
def sendmsg():
   if request.method=="POST":

      messg=request.form.get("message")
      sender=request.form.get("self")
      receiver=request.form.get("room")
      socket.emit("new_message",[messg,sender],room=receiver)



if __name__ == '__main__':
   socket.socketio.run(application)
