from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from flask_restx import  Api, Resource
from flasgger import Swagger



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.cart'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

swagger = Swagger(app)
api = Api(app)

ma = Marshmallow(app)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    order = db.Column(db.Integer)

def __init__(self,name,order):
    self.name = name
    self.order= order

class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'order')

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@app.route('/shaleen', methods=['GET'])
def trial():
    
    return "test flask by shaleen"

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return 'hello'

@app.route('/shaleen', methods=['POST'])
def trialpost():
    name = request.json
    return jsonify(name)

@api.route('/test', methods=['POST'])
class trialpost2(Resource):
    def post(self):
      name = request.json
      return jsonify(name)

@app.route('/product', methods=['POST'])
def add():
    name_data = request.json['name']
    order_data = request.json['order']
    new = Cart(name = name_data,order=order_data)
    db.session.add(new)
    db.session.commit()
    return product_schema.jsonify(new)

@api.route('/products', methods=['POST'])          #when route is /product swagger not functioning
class adddata(Resource):
 def post(self):
    name_data = request.json['name']
    order_data = request.json['order']
    new = Cart(name = name_data,order=order_data)
    db.session.add(new)
    db.session.commit()
    return product_schema.jsonify(new)



@app.route('/product', methods =['GET'])              
def get_items():
   total_products = Cart.query.all()
   result = products_schema.dump(total_products)
   return jsonify(result)

@api.route('/product', methods =['GET'])
class get_items_test(Resource):
 def get(self):                                                 #do we have to use get or post as corresponding functions and not anh other?
   total_products = Cart.query.all()
   result = products_schema.dump(total_products)
   return jsonify(result)

@app.route('/product/<id>', methods =['GET'])
def get_items_id(id):
   product = Cart.query.get(id)
   return product_schema.jsonify(product)

@api.route('/product/<string:id>', methods =['GET'])   
class get_items_by_id(Resource):
  def get(self,id):
   product = Cart.query.get(id)
   return product_schema.jsonify(product)
   
   
  
  


if __name__ == '__main__':
  app.run(debug=True)


            