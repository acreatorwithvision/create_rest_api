from flask import Flask, jsonify, request

#name of flask app
app=Flask(__name__)


#this creates a GET request api which will fetch user-data from user_id	
@app.route("/get-user/<user_id>")
def get_user(user_id):
	user_data={
		"user_id":user_id,
		"name":"Suhas G",
		"email":"suhasg@gmail.com"
	}
		
	extra=request.args.get("extra")
	if extra:
		user_data["extra"]=extra
	return jsonify(user_data), 200

#this creates a POST request api which can be in tested in postman body.
@app.route("/create-user",methods=["POST"])
def create_user():
	data=request.get_json()
	
	return jsonify(data), 201

if __name__=="__main__":
	app.run(debug=True)
