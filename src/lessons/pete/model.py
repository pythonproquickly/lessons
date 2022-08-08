import peewee as pw   #
import sys
import os


DATABASE = 'wineo.db'
if os.path.exists(DATABASE):
    os.remove(DATABASE)


database = pw.SqliteDatabase(DATABASE)


class BaseModel(pw.Model):
    class Meta:
        database = database

class Making(BaseModel):
    """This is a making which represents creating onw batch of wine for a harvest of grapes"""
    making_name = pw.CharField()
    initial_grape_weight = pw.CharField()
    crush_date = pw.CharField()
        

class Bin(BaseModel):
    """THis represents a bin where wine is fermented for a single making. Note there may be several bins for a making"""
    making = pw.ForeignKeyField(Making, backref='bins')
    gallons = pw.CharField()
    ph_level = pw.CharField() # moved from msmt - Making?


class MakingBinMeasurment(BaseModel):
    """This records key daily measurements for a bin a who made them."""
    bin = pw.ForeignKeyField(Bin, backref='msmt') # fk
    measurement_date = pw.CharField()
    temperature = pw.CharField()

    birx = pw.CharField()
    ta = pw.CharField()
    measured_by_name = pw.CharField()

class Mix(BaseModel):
    """This records how wines in a bin are mixed the date, and who did the mixing."""
    from_bin = pw.ForeignKeyField(Bin, backref='frombin') # fk
    to_bin = pw.ForeignKeyField(Bin, backref='tobin') # fk
    mixed_changed_date = pw.CharField()
    quantity_mixed_in = pw.CharField()
    mixed_by_name = pw.CharField()


database.create_tables([Making, Bin, MakingBinMeasurment, Mix])
makings = []
for _ in range(3): # must be exact lenght
    makings.append(Making())

makings[0].making_name = "chardonnay"
makings[0].initial_grape_weight = "99"
makings[0].crush_date = "11/11/3333"

makings[1].making_name = "merlot"
makings[1].initial_grape_weight = "1"
makings[1].crush_date = "11/11/57575"

makings[2].making_name = "gsm"
makings[2].initial_grape_weight = "3"
makings[2].crush_date = "11/11/"
for making in makings:
    making.save()

bins = []
for _ in range(2):
    bins.append(Bin())

bins[0].making = makings[0]
bins[0].gallons = "10"
bins[1].making = makings[0]
bins[1].gallons = "5"
print(bins)
for a_bin in bins: # prevent clash with bin intrnal!!
    a_bin.save()

making_bin_measurements = [MakingBinMeasurment() for _ in range(1)]

making_bin_measurements[0].bin = bins[0]
making_bin_measurements[0].measurement_date = "12/25/2017"
making_bin_measurements[0].temperature = "62f, 16c"
making_bin_measurements[0].ph_level = "33"
making_bin_measurements[0].birx = "44"
making_bin_measurements[0].ta = "11"
making_bin_measurements[0].measured_by_name = "Sandy"

for making_bin_measurement in making_bin_measurements:
    making_bin_measurement.save()

fusions = [Mix() for _ in range(1)]

fusions[0].to_bin = bins[0]
fusions[0].from_bin = bins[1]
fusions[0].mixed_changed_date = "05/10/2018"
fusions[0].quantity_mixed_in = "105gal"
fusions[0].mixed_by_name = "Salvador"

for x in fusions:
    x.save()
