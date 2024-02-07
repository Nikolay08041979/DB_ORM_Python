import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from My_projects.models import create_tables, Shop, Stock, Sale, Book, Publisher

DSN = 'postgresql://postgres:12345@localhost:5432/book_sales_db'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

# сессия
Session = sessionmaker(bind=engine)
session = Session()
session.commit()

# создание объектов
publisher1 = Publisher(name="Академия")
session.add(publisher1)
session.commit()
print(publisher1)

session.close()
# hw1 = Homework(number=1, description="первое задание", course=js)
# hw2 = Homework(number=2, description="второе задание (сложное)", course=js)
#
# session.add(js)
# print(js.id)
# session.add_all([hw1, hw2])
# session.commit()  # фиксируем изменения
# print(js.id)
#
#
# # запросы
# q = session.query(Course).join(Homework.course).filter(Homework.number == 1)
# print(q)
# for s in q.all():
#     print(s.id, s.name)
#     for hw in s.homeworks:
#         print("\t", hw.id, hw.number, hw.description)
#
# # вложенный запрос
# subq = session.query(Homework).filter(Homework.description.like("%сложн%")).subquery("simple_hw")
# q = session.query(Course).join(subq, Course.id == subq.c.course_id)
# print(q)
# for s in q.all():
#     print(s.id, s.name)
#     for hw in s.homeworks:
#         print("\t", hw.id, hw.number, hw.description)
#
#
# # обновление объектов
# session.query(Course).filter(Course.name == "JavaScript").update({"name": "NEW JavaScript"})
# session.commit()  # фиксируем изменения
#
#
# # удаление объектов
# session.query(Homework).filter(Homework.number > 1).delete()
# session.commit()  # фиксируем изменения