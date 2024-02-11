from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import create_tables, Shop, Stock, Sale, Book, Publisher

pw = '12345'
lg = 'postgres'
name_db = 'books_db'
DSN = f'postgresql://{lg}:{pw}@localhost:5432/{name_db}'
engine = create_engine(DSN)

# сессия
Session = sessionmaker(bind=engine)
session = Session()
create_tables(engine)


# запросы
publisher_list = session.query(Publisher).all()
for item in publisher_list:
    print(item.id, item.name)

id_publisher = str(input("Введите id Издательства из приведенного выше списка: "))

results = session.query(Book)\
    .with_entities(Book.title, Shop.name, Sale.price, Sale.date_sale)\
        .join(Publisher, Publisher.id == Book.id_publisher)\
        .join(Stock, Stock.id_book == Book.id)\
        .join(Shop, Shop.id == Stock.id_shop)\
        .join(Sale, Sale.id_stock == Stock.id)\
        .filter(Publisher.id == id_publisher).all()

for title, name, price, date_sale in results:
    print(title.ljust(33), name, str(price).ljust(8), date_sale,  sep = " | ")

session.close()

# select b.title, p.name, sa.price, sa.date_sale from book b
# join publisher p on p.id = b.id_publisher
# join stock s on s.id_book = b.id
# join shop sp on sp.id = s.id_shop
# join sale sa on sa.id_stock  = s.id
# where b.id_publisher = 1
