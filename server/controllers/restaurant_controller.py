from flask import Blueprint, jsonify, request
from server import db
from server.models.restaurant import Restaurant

restaurant_bp = Blueprint('restaurants', __name__)

# GET /restaurants - Retrieve a list of all restaurants
@restaurant_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants]), 200

# GET /restaurants/<int:id> - Retrieve a single restaurant with its pizzas
@restaurant_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    return jsonify(restaurant.to_dict()), 200

# DELETE /restaurants/<int:id> - Delete a restaurant and its associated RestaurantPizzas
@restaurant_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return '', 204
