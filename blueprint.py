from flask import Blueprint, request, jsonify, render_template
from database import Sdatabase

mambo_route = Blueprint("mambo", __name__, url_prefix="/api/v1/")
dbinstanse=Sdatabase()


@mambo_route.route('/loginsss')
def intro():
    return "start blueprint api" 
  


@mambo_route.route('/login')
def indexb():
    return render_template('/UI/indexfetch.html')



@mambo_route.route('/reg', methods=['POST'])
def reg():

    username = request.form.get('uname', "", type=str)
    email = request.form.get('idno', "", type=str)
    results = {"name": username, "idno": email}
    dbinstanse.insertData(username,email)
    return jsonify(result="success")
