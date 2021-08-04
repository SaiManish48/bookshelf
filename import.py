import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Book
import csv


engine= create_engine("postgresql://udnpjoquxnflrh:ccce64fa91aff8e1fd26de90072d7190029c06682f87f6e5ef593f46b5227304@ec2-34-197-105-186.compute-1.amazonaws.com:5432/d6r011f98q6p85")
db_session = scoped_session(sessionmaker(bind=engine))
with open('books.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    for row in readCSV:
        new_book=Book(isbn=row[0],name=row[1],author=row[2], year=row[3])
        db_session.add(new_book)
db_session.commit()
db_session.close()
