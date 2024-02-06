from flask import Blueprint, request
from flask_restful import Api, Resource, reqparse
from .. import db
from ..model.login2 import LoginUser #### WARN: This Method DOES NOT EXIST

loginUserBp = Blueprint("LoginUser", __name__)
loginUserApi = Api(loginUserBp)

class LoginUserAPI(Resource):
    def get(self):
        id = request.args.get("id")
        loginUser = db.session.query(LoginUser).get(id)
        if loginUser:
            return loginUser.to_dict()
        return {"message": "not found"}, 404

    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument("username", required=True, type=str)
        parser.add_argument("password", required=True, type=str)
        parser.add_argument("state", required=True, type=str)
        args = parser.parse_args()
        loginUser = LoginUser(args["username"], args["password"], args["state"])

        try:
            db.session.add(loginUser)
            db.session.commit()
            return loginUser.to_dict(), 201
        except Exception as exception:
            db.session.rollback()
            return {"message":f"error {exception}"}, 500

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        parser.add_argument("username")
        parser.add_argument("password")
        parser.add_argument("state")
        args = parser.parse_args()
        
        try:
            loginUser = db.session.query(LoginUser).get(args["id"])
            if loginUser:
                if args["username"] is not None:
                    loginUser.username = args["username"]
                if args["password"] is not None:
                    loginUser.password = args["password"]
                if args["password"] is not None:
                    loginUser.password = args["state"]
                db.session.commit()
                return loginUser.to_dict(), 200
            else:
                return {"message": "not found"}, 404
        except Exception as exception:
            db.session.rollback()
            return {"message": f"error {exception}"}, 500
    
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", required=True, type=int)
        args = parser.parse_args()

        try:
            loginUser = db.session.query(LoginUser).get(args["id"])
            if loginUser:
                db.session.delete(loginUser)
                db.session.commit()
                return loginUser.to_dict()
            else:
                return {"message": "not found"}, 404
        except Exception as exception:
            db.session.rollback()
            return {"message": f"error {exception}"}, 500

class LoginUserListAPI(Resource):
    def get(self):
        loginUser = db.session.query(LoginUser).all()
        return [loginUser.to_dict() for login in loginUser]
    
    def delete(self):
        try:
            db.session.query(LoginUser).delete()
            db.session.commit()
            return
        except Exception as exception:
            db.session.rollback()
            return {"message": f"error {exception}"}

loginUserApi.add_resource(LoginUserAPI, "/loginUser")
loginUserApi.add_resource(LoginUserListAPI, "/loginUserList")