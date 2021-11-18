import os

from flask import Response, app, g, jsonify, request, make_response

from rest_flask.flask import app, db
from rest_flask.models.user import Users
from rest_flask.models.postschema import PostSchema
from settings import APP_NAME, IS_LOCAL, LOG_PATH, NODE_IP

@app.route(f"/api/v1/user", methods=["GET"])
def getUser():
    get_all_user = Users.query.all()
    post_schema = PostSchema(many=True)
    users = post_schema.dump(get_all_user)
    if len(users) == 0:
        return make_response(jsonify({"status": False, "message": "No data found"}), 404)
    else:
        return make_response(jsonify({"status": True, "message": "get data successfully", "data": users}), 200)

@app.route(f"/api/v1/user", methods=["POST"])
def createUser():
    data = request.get_json()
    name = data.get('name')
    birth_year = data.get('birth_year')
    userObj = Users(name, birth_year)
    post_schema = PostSchema()
    result = post_schema.dump(Users.create(userObj))
    if len(result) == 0:
        return make_response(jsonify({"status": False, "message": "unable to get data"}), 404)
    else:
        return make_response(jsonify({"status": True, "message": "get data successfully", "data": result}), 200)

@app.route('/api/v1/user/<id>', methods=['GET'])
def get_user_by_id(id):
    get_user = Users.query.get(id)
    user_schema = PostSchema()
    user = user_schema.dump(get_user)
    if len(user) == 0:
        return make_response(jsonify({"status": False, "message": "unable to add data"}), 404)
    else:
        return make_response(jsonify({"status": True, "message": "get data successfully", "data": user}), 200)

@app.route('/api/v1/user/<id>', methods=['PUT'])
def update_user_by_id(id):
    data = request.get_json()    
    get_users = Users.query.get(id)    
    if get_users is None:
        return make_response(jsonify({"status": False, "message": "unable to get user with provided data"}), 404)   
    if data.get('name'):
       get_users.name = data['name']
    if data.get('birth_year'):
       get_users.birth_year = data['birth_year']
    
    db.session.add(get_users)
    db.session.commit()
    users_schema = PostSchema(only=['id', 'name', 'birth_year'])
    users = users_schema.dump(get_users)

    if len(users) == 0:
        return make_response(jsonify({"status": False, "message": "unable to update data"}), 404)
    else:
        return make_response(jsonify({"status": True, "message": "update data successfully", "data": users}), 200)

@app.route('/api/v1/user/<id>', methods=['DELETE'])
def delete_todo_by_id(id):
   get_todo = Users.query.get(id)
   db.session.delete(get_todo)
   db.session.commit()
   return make_response("", 204)



    

