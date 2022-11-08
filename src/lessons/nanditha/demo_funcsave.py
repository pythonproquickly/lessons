import json

info_dict = {
    '001':
        {
            'name': 'calculation',
            'f':
                """def calculate(x, y):
                   return 4 * (x + y) / 10""",
        }
}


def write(data, file):
    json_object = json.dumps(data, indent=4)
    with open(file, "w") as outfile:
        outfile.write(json_object)


def read(file):
    with open(file, 'r') as openfile:
        json_object = json.load(openfile)
    return json_object


write(info_dict, 'with_func.json')
info_dict_from_json = read('with_func.json')
exec(info_dict_from_json['001']['f'])
answer = calculate(10, 20)
print(answer)
