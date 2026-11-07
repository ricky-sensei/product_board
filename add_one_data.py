from app import Product, db

apple = Product(name="りんご（ふじ）", price=300, producer_name="高橋農園")
db.session.add(apple)
db.session.commit()
apple.id
