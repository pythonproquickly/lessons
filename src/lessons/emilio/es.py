import json


def get_current(event_data):
    latest = {}
    for event in event_data:
        for event_id, payload in event.items():
            if event_id not in latest:
                latest[event_id] = {}
            for k, v in payload.items():
                latest[event_id][k] = v
    return latest


def write(data, file):
    json_object = json.dumps(data, indent=4)
    with open(file, "w") as outfile:
        outfile.write(json_object)


def read(file):
    with open(file, 'r') as openfile:
        json_object = json.load(openfile)
    return json_object


def get_data():
    return [
        {1435: {
            'date': '01/02/2022',
            'customer': 'Andy',
            'product': 'widget',
            'price': 10.12}
        },
        {2001: {
            'date': '01/03/2022',
            'customer': 'Fred',
            'product': 'box',
            'price': 200.45}
        },
        {1435: {
            'date': '01/05/2022',
            'price': 9.20,
            'discount': True}
        },
        {1446: {
            'date': '01/02/2022',
            'customer': 'Sue',
            'product': 'ball',
            'price': 15.10}
        },
    ]


def main():
    events = get_data()
    write(events, "orders.json")
    # time passes...
    events = read("orders.json")
    current = get_current(events)
    write(current, "latest_orders.json")


if __name__ == "__main__":
    main()
