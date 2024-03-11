from application import db, Drink

db.create_all()

# Create some drinks
drink1 = Drink(name="Grape soda",
              description = "Soda that tastes like grapes")

drink2 = Drink(name="Orange juice",
              description = "Freshly squeezed orange juice")

db.session.add(drink1)
db.session.add(drink2)

db.session.commit()

# Print all drinks in the db
print(Drink.query.all())