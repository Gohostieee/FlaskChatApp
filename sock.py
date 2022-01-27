from flask_socketio import SocketIO, send
from threading import Thread
from flask import request
from time import sleep

def init(app):
	global socketio
	socketio = SocketIO(app)
	@socketio.on('disconnect')
	def disc(data):
		print(data, " disconenected idk")
	@socketio.on('message')
	def handle_message(data):
			print(data, " champions")
			print(request.sid,data, 'ROCKSTAR')
	@socketio.on('new_partner')
	def searchAppend(data):
			print("uwaaaa")
			global searching
			searching.append(request.sid)
			print("appended ", data,request.sid)
	return socketio

def findChat():
	global socket
	global searching
	searching=[]
	while True:
			if len(searching)>1:
				usr1=searching[0]
				usr2=searching[1]
				if usr1==usr2:
					searching.append(searching.pop(1))
				searching.remove(usr1)
				searching.remove(usr2)
				print("kewwdsdwdadadwd")
				socketio.emit("partner",usr1,room=usr2)
				socketio.emit("partner",usr2,room=usr1)
def heartBeat():
	global socket
	
if __name__=='__main__':
	wowee=findChat()
	wowee.start()

     