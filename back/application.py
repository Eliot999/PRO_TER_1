from flask import Flask, jsonify, request
import psycopg2


def main() -> None:
	init_request()
	#request()
	app = Flask(__name__)

	@app.route('/')
	def index():
		return jsonify({1:"test"})



	@app.route("users-auth")
	def auth_verification():
		request_data = request.get_json()
		hash = request_data["password-hash"]


	app.run()



def init_request() -> None:
	global connection
	connection = psycopg2.connect(
    dbname='d16b1gad2orhm9',
    host='ec2-54-74-60-70.eu-west-1.compute.amazonaws.com',
    user='pmyomyswsqtzkx',
    password='6c3b5451b78f81b01f77a1d2317ace62ddbe07b11f38960666fb73d59dfd5340',
    port='5432')


def request(request:str) -> str:
	try:
		cursor = connection.cursor()
		cursor.execute(request)
		result = cursor.fetchall()
	except psycopg2.Error as e:
		return e

if __name__ == '__main__':
	main()

