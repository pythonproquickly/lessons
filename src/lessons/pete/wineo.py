import peewee as pw
import sys

DATABASE = 'wineo.db'
database = pw.SqliteDatabase(DATABASE)


class BaseModel(pw.Model):
    class Meta:
        database = database


class Grapes(BaseModel):
    #  http://docs.peewee-orm.com/en/latest/peewee/models.html
    grape_name = pw.CharField(30)
    clipped_date = pw.DateField()
    ava = pw.CharField(30)
    clipped_weight_lbs = pw.FloatField(9, 2)

def db_create():
    try:
        database.create_tables([Grapes, ], safe=True)
    except DBCreate as e:
        print(f"Whoops something went wrong creating db: {e}")
    else:
        print("DB created")


def main():
    pass


class DBCreate(Exception):
    pass


if __name__ == "__main__":
    parms = sys.argv[1:]
    if parms[0] == "create":
        db_create()
    main()
