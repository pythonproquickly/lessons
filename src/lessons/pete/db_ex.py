#pip install peewee

from datetime import date
import os
import peewee as pw

os.remove("wine.db")

db = pw.SqliteDatabase('wine.db')


class Bottle(pw.Model):
    name = pw.CharField()
    color = pw.CharField()

    class Meta:
        database = db


db.create_tables([Bottle])

bottle = Bottle()
bottle.name = "Merlot"
bottle.color = "Red"
bottle.save()
