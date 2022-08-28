import peewee as pw   #
import sys
import os


DATABASE = 'myname.db'
if os.path.exists(DATABASE):
    os.remove(DATABASE)


database = pw.SqliteDatabase(DATABASE)


class BaseModel(pw.Model):
    class Meta:
        database = database

class XXX(BaseModel):
     = pw.CharField()
     = pw.CharField()
     = pw.CharField()



class YY(BaseModel):
     = pw.ForeignKeyField(Xx, backref='xx')


database.create_tables([XXX, YY])

