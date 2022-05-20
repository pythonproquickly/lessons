import json
import pprint

pp = pprint.PrettyPrinter(indent=2, compact=True)

FILE_PATH = "/home/andy/data/json/"

with open(f"{FILE_PATH}sample.json") as f:
    document = json.load(f)
pp.pprint(document)
print()

document_string = json.dumps(document)
pp.pprint(document_string)
