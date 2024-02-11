from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import create_tables, Shop, Stock, Sale, Book, Publisher

pw = 'Liza-26052008'
lg = 'postgres'
name_db = 'books_db'
DSN = f'postgresql://{lg}:{pw}@localhost:5432/{name_db}'
engine = create_engine(DSN)
# сессия
Session = sessionmaker(bind=engine)
session = Session()
create_tables(engine)
# создание объектов
# publisher1 = Publisher(name="Академия")
# publisher2 = Publisher(name="Питер")
# publisher3 = Publisher(name="Эксмо")
# publisher4 = Publisher(name="АСТ")
# session.add(publisher4)
# session.add_all([publisher1, publisher2, publisher3])

# book1 = Book(title="Гарри Поттер и философский камень", id_publisher=1)
# book2 = Book(title="Гарри Поттер и Кубок огня", id_publisher=1)
# book3 = Book(title="Гарри Поттер и Орден феникса", id_publisher=1)
# book4 = Book(title="Гарри Поттер и узник Азкабана", id_publisher=1)
# book5 = Book(title="Гарри Поттер и Колокол", id_publisher=1)
# book6 = Book(title="Гарри Поттер и принц-полукровка", id_publisher=1)
# book7 = Book(title="Граф монтекристо", id_publisher=4)
# book8 = Book(title="Три мушкетера", id_publisher=5)
# book9 = Book(title="Властелин Колец", id_publisher=7)
# book10 = Book(title="Хроники Нарни", id_publisher=7)
# session.add_all([book1, book2, book3, book4, book5, book6, book7, book8, book9, book10])

# shop1 = Shop(name="Магазин 1")
# shop2 = Shop(name="Магазин 2")
# shop3 = Shop(name="Магазин 3")
# session.add_all([shop1, shop2, shop3])

# stock1 = Stock(id_shop=1, id_book=1, count=10)
# stock2 = Stock(id_shop=1, id_book=2, count=15)
# stock3 = Stock(id_shop=1, id_book=3, count=20)
# stock4 = Stock(id_shop=1, id_book=4, count=25)
# stock5 = Stock(id_shop=1, id_book=5, count=30)
# stock6 = Stock(id_shop=1, id_book=6, count=35)
# stock7 = Stock(id_shop=2, id_book=7, count=40)
# stock8 = Stock(id_shop=2, id_book=8, count=45)
# stock9 = Stock(id_shop=2, id_book=9, count=50)
# stock10 = Stock(id_shop=3, id_book=10, count=55)
# session.add_all([stock1, stock2, stock3, stock4, stock5, stock6])
# session.add_all([stock7, stock8, stock9, stock10])

# sale1 = Sale(price=100, date_sale="2022-01-01", id_stock=1, count=5)
# sale2 = Sale(price=200, date_sale="2022-01-02", id_stock=2, count=10)
# sale3 = Sale(price=300, date_sale="2022-01-03", id_stock=3, count=15)
# sale4 = Sale(price=400, date_sale="2022-01-04", id_stock=4, count=20)
# sale5 = Sale(price=500, date_sale="2022-01-05", id_stock=5, count=25)
# sale6 = Sale(price=600, date_sale="2022-01-06", id_stock=6, count=30)
# sale7 = Sale(price=700, date_sale="2022-01-07", id_stock=7, count=35)
# sale8 = Sale(price=800, date_sale="2022-01-08", id_stock=8, count=40)
# sale9 = Sale(price=900, date_sale="2022-01-09", id_stock=9, count=45)
# sale10 = Sale(price=1000, date_sale="2022-01-10", id_stock=10, count=50)
#
# session.add_all([sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8, sale9, sale10])

session.commit()
