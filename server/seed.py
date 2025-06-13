from server import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()
app.app_context().push()

# Reset the database (Warning: This drops all tables)
db.drop_all()
db.create_all()

# Create sample Restaurants
r1 = Restaurant(name="Pizzeria Uno", address="29 E Ohio St")
r2 = Restaurant(name="Bella Napoli", address="123 Main St")
db.session.add_all([r1, r2])
db.session.commit()

# Create sample Pizzas
p1 = Pizza(name="Margherita", ingredients="Dough, Tomato, Mozzarella, Basil")
p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Pepperoni, Cheese")
db.session.add_all([p1, p2])
db.session.commit()

# Create sample RestaurantPizzas (ensure prices are within 1-30)
rp1 = RestaurantPizza(price=12, pizza_id=p1.id, restaurant_id=r1.id)
rp2 = RestaurantPizza(price=15, pizza_id=p2.id, restaurant_id=r1.id)
db.session.add_all([rp1, rp2])
db.session.commit()

print("Seeding complete!")
