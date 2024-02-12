import json
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import create_tables, Shop, Stock, Sale, Book, Publisher

load_dotenv()

password = os.getenv('DB_PASSWORD')
login = os.getenv('DB_LOGIN')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
name_db = os.getenv('DB_NAME')
DSN = f'postgresql://{login}:{password}@{host}:{port}/{name_db}'

engine = create_engine(DSN)
create_tables(engine)
# сессия
Session = sessionmaker(bind=engine)
db_session = Session()


def data_file_to_table():
    with open('fixtures/tests_data.json', 'r') as fd:
        data = json.load(fd)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        db_session.add(model(id=record.get('pk'), **record.get('fields')))
    db_session.commit()

    return "Данные успешно внесены в базу данных"

def data_input_to_table():

    publisher1 = Publisher(name="Академия")
    publisher2 = Publisher(name="Питер")
    publisher3 = Publisher(name="Эксмо")
    publisher4 = Publisher(name="АСТ")
    db_session.add_all([publisher1, publisher2, publisher3, publisher4])
    db_session.commit()

    book1 = Book(title="Гарри Поттер и философский камень", id_publisher=1)
    book2 = Book(title="Гарри Поттер и Кубок огня", id_publisher=1)
    book3 = Book(title="Гарри Поттер и Орден феникса", id_publisher=1)
    book4 = Book(title="Гарри Поттер и узник Азкабана", id_publisher=1)
    book5 = Book(title="Гарри Поттер и Колокол", id_publisher=1)
    book6 = Book(title="Гарри Поттер и принц-полукровка", id_publisher=1)
    book7 = Book(title="Граф монтекристо", id_publisher=2)
    book8 = Book(title="Три мушкетера", id_publisher=3)
    book9 = Book(title="Властелин Колец", id_publisher=4)
    book10 = Book(title="Хроники Нарни", id_publisher=4)
    db_session.add_all([book1, book2, book3, book4, book5, book6, book7, book8, book9, book10])
    db_session.commit()

    shop1 = Shop(name="Магазин 1")
    shop2 = Shop(name="Магазин 2")
    shop3 = Shop(name="Магазин 3")
    db_session.add_all([shop1, shop2, shop3])
    db_session.commit()

    stock1 = Stock(id_shop=1, id_book=1, count=10)
    stock2 = Stock(id_shop=1, id_book=2, count=15)
    stock3 = Stock(id_shop=1, id_book=3, count=20)
    stock4 = Stock(id_shop=1, id_book=4, count=25)
    stock5 = Stock(id_shop=1, id_book=5, count=30)
    stock6 = Stock(id_shop=1, id_book=6, count=35)
    stock7 = Stock(id_shop=2, id_book=7, count=40)
    stock8 = Stock(id_shop=2, id_book=8, count=45)
    stock9 = Stock(id_shop=2, id_book=9, count=50)
    stock10 = Stock(id_shop=3, id_book=10, count=55)
    db_session.add_all([stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8, stock9, stock10])
    db_session.commit()

    sale1 = Sale(price=100, date_sale="2022-01-01", id_stock=1, count=5)
    sale2 = Sale(price=200, date_sale="2022-01-02", id_stock=2, count=10)
    sale3 = Sale(price=300, date_sale="2022-01-03", id_stock=3, count=15)
    sale4 = Sale(price=400, date_sale="2022-01-04", id_stock=4, count=20)
    sale5 = Sale(price=500, date_sale="2022-01-05", id_stock=5, count=25)
    sale6 = Sale(price=600, date_sale="2022-01-06", id_stock=6, count=30)
    sale7 = Sale(price=700, date_sale="2022-01-07", id_stock=7, count=35)
    sale8 = Sale(price=800, date_sale="2022-01-08", id_stock=8, count=40)
    sale9 = Sale(price=900, date_sale="2022-01-09", id_stock=9, count=45)
    sale10 = Sale(price=1000, date_sale="2022-01-10", id_stock=10, count=50)
    db_session.add_all([sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8, sale9, sale10])
    db_session.commit()

    return 'Данные успешно внесены в БД'

def get_spops(idx_publisher):

    publisher_list = db_session.query(Publisher).all()
    publisher_list_id = [str(item.id) for item in publisher_list]
    publisher_list_name = [item.name for item in publisher_list]

    results = db_session.query(Book)\
        .with_entities(Book.title, Shop.name, Sale.price, Sale.date_sale)\
            .join(Publisher, Publisher.id == Book.id_publisher)\
            .join(Stock, Stock.id_book == Book.id)\
            .join(Shop, Shop.id == Stock.id_shop)\
            .join(Sale, Sale.id_stock == Stock.id)\

    # results = db_session.query(Book.title, Shop.name, Sale.price, Sale.date_sale) \
    #     .join(Publisher, Publisher.id == Book.id_publisher) \
    #     .join(Stock, Stock.id_book == Book.id) \
    #     .join(Shop, Shop.id == Stock.id_shop) \
    #     .join(Sale, Sale.id_stock == Stock.id)

    if idx_publisher.isdigit() == True:
        if idx_publisher not in publisher_list_id:
            [print(item.id, item.name) for item in publisher_list]
            idx_publisher = str(input('Издательства с таким id нет в БД. '
                                      'Введите id из приведенного выше списка: '))
        results = results.filter(Publisher.id == idx_publisher).all()
    else:
        if idx_publisher not in publisher_list_name:
            [print(item.id, item.name) for item in publisher_list]
            idx_publisher = str(input('Издательства с таким названием нет в БД. '
                                      'Введите название из приведенного выше списка: '))
        results = results.filter(Publisher.name == idx_publisher).all()

    for title, name, price, date_sale in results:
        print(f"{title: <33} | {name: <10} | {price: <8} | {date_sale.strftime('%d-%m-%Y')}")

db_session.close()


if __name__ == '__main__':
    #print(data_file_to_table())
    print(data_input_to_table())
    idx_publisher = str(input('Введите id или наименование издательства: '))
    get_spops(idx_publisher)


# select b.title, p.name, sa.price, sa.date_sale from book b
# join publisher p on p.id = b.id_publisher
# join stock s on s.id_book = b.id
# join shop sp on sp.id = s.id_shop
# join sale sa on sa.id_stock  = s.id
# where b.id_publisher = 1
