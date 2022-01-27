import boto3
client = boto3.client('dynamodb',
	region_name='us-east-2',
	aws_access_key_id='secret',
    aws_secret_access_key='secret',)
db = boto3.resource('dynamodb',
	region_name='us-east-2',
	aws_access_key_id='secret',
    aws_secret_access_key='secret',)
table = db.Table("Searching")
def get_usr_amount():
	req=table.get_item(
	Key={
	"genevievie":  'users',
	})
	return req["Item"]['amount']

def put_user_searching(username):
	currUsr=get_usr_amount()
	table.update_item(
		Key={"genevievie":'users',},
		UpdateExpression="set amount = :r",
		ExpressionAttributeValues={
        		':r': currUsr+1,
 		})
	return table.put_item(
		Item={
			"genevievie":  f'usr-{currUsr+1}',
			"name":username

		})
if __name__=="__main__":
	put_user_searching("kekw")