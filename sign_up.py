import boto3
from botocore.exceptions import ClientError
import os
import generalFunctions



client = boto3.client(
	'cognito-idp',
	region_name='us-east-2',
	aws_access_key_id='secret',
    aws_secret_access_key='secret',
    )

def signup(username,password):
	status={"status":'','message':{}}
	checks=generalFunctions.passwdCheck(password)
	for x in checks:
		if not checks[x]:
			status['status']='err-002'
			status['message'][len(status['message'])]=x
	if 'err' in status['status']:
		return status

	try:
		response = client.sign_up(
			ClientId='secret',
			Username=username,
			Password=password,
		)
		admConfirm(username)
		print("kekw")
		status['message']=str(login(username,password)['AuthenticationResult'])
		status['status']='authorized'
		return status

	except ClientError as e:
		print("lifeless")
		print(e.response['Error'])
		print(e.response['Error']['Message'])
		error=e.response['Error']['Message']

		if (e.response['Error']['Code'] == "UsernameExistsException"):
			status['status']='err-001'
			return status
	
			
	return None
def login(username,password):
 	return client.initiate_auth(
		ClientId='secret',
		AuthFlow='USER_PASSWORD_AUTH',
		AuthParameters={
			'USERNAME':username,
			'PASSWORD':password

		}
	)
def admAuth():
	response = client.admin_initiate_auth(
    UserPoolId='us-east-2_c7UT2FKyX',
    ClientId='secret',
    AuthFlow='USER_PASSWORD_AUTH'
    )
def admConfirm(username):
	client.admin_confirm_sign_up(
    	UserPoolId='us-east-2_c7UT2FKyX',
   		Username=username,
    	
	)
def checkUser(usr,password):
	try:
		login(usr,password)
		return "authorized"
	except ClientError as e:
		if "Incorrect username or password" in e.response['Error']['Message']:
			return "denied"
		else:
			return "denied-404"
if __name__=="__main__":
	try:
		print(login('fdvf43',"#f43Ffwfw1"))
		print("sagge")
	except ClientError as e:
		print(e.response['Error']['Message'])
