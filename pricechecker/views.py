from flask import Blueprint, jsonify, render_template, make_response, request
from flask_restful import Api, Resource
from pricechecker.resources.price_checker_resources import PriceCheckerResource



class Home(Resource):
    def post(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template("home2.html"), headers)

    def get(self):
        result = {"name": "", "price":"", "image":"", "link":""}
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template("home.html", result=result), headers)





price = Blueprint(
    "bot", __name__
)

api = Api(price)

api.add_resource(Home, '/')
api.add_resource(PriceCheckerResource, "/get_price")