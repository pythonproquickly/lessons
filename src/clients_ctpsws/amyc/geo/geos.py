import json
import math

R = 3960.8


def get_input():
    input_data = []

    for line in range(6):
        data = input()
        key_ends = data.find(" ")
        key = data[:key_ends]
        value = data[key_ends + 1 :]
        input_data.append([key, value])

    """input_data = [
        ["CENTER", "NOMINATIM Bren Hall, Irvine, CA"],
        ["RANGE", "30"],
        ["THRESHOLD", "100"],
        ["MAX", "5"],
        ["AQI", "PURPLEAIR"],
        ["REVERSE", "NOMINATIM"],
    ]  """  # delete me
    d = "/home/andy/ws/andykmiles/clients-ctpsws/src/clients_ctpsws/amyc/geo/"
    input_data = [
        ["CENTER", f"FILE {d}nominatim_center.json"],
        ["RANGE", "30"],
        ["THRESHOLD", "100"],
        ["MAX", "5"],
        ["AQI", f"FILE {d}purpleair.json"],
        [
            "REVERSE",
            "FILES ",
            [
                f"{d}nominatim_reverse1.json",
                f"{d}nominatim_reverse2.json",
                f"{d}nominatim_reverse3.json",
            ],
        ],
    ]  # delete me

    input_data = {
        input_data[0][0]
        + " "
        + input_data[0][1].split()[0]: input_data[0][1].split()[1],
        input_data[1][0]: int(input_data[1][1]),
        input_data[2][0]: int(input_data[2][1]),
        input_data[3][0]: int(input_data[3][1]),
        input_data[4][0]
        + " "
        + input_data[4][1].split()[0]: " ".join(input_data[4][1].split()[1:]),
        input_data[5][0]
        + " "
        + input_data[5][1].split()[0]: " ".join(input_data[5][1].split()[1:]),
    }
    print(input_data)
    input()
    return input_data


def generate_report():
    pass


def calculate_value(concentration, min_aqi, max_aqi, bottom, top):
    return concentration / (max_aqi - min_aqi) * (top - bottom)


def calculate_AQI(concentration):
    if 0 <= concentration < 12.1:
        return calculate_value(concentration, 0, 12, 0, 50)
    if concentration < 35.5:
        return calculate_value(concentration, 12.1, 35.4, 50, 100)
    if concentration < 55.5:
        return calculate_value(concentration, 35.5, 55.4, 101, 150)
    if concentration < 150.5:
        return calculate_value(concentration, 55.5, 150.4, 151, 200)
    if concentration < 250.5:
        return calculate_value(concentration, 150.5, 250.4, 201, 300)
    if concentration < 50.5:
        return calculate_value(concentration, 250.5, 350.4, 301, 400)
    if concentration < 500.5:
        return calculate_value(concentration, 350.5, 500.4, 401, 500)
    return 500


def calculate_distance(point1, point2):
    dlat = point1.latitude - point2.latitude
    dlon = point1.longitde - point2.longitude
    alat = (point1.latitude + point2.latitude) / 2
    x = dlon * math.cos(alat)
    return math.sqrt(x**2 + dlat**2) * R


def handle_input(input_data):
    if input_data.get("CENTER FILE", None) is not None:
        with open(input_data["CENTER FILE"], "r", encoding="utf-8") as f:
            input_data["CENTER FILE"] = json.load(f)
    if input_data.get("CENTER NOMINATIM", None) is not None:
        # get from api
        pass
    if input_data.get("AQI FILE", None) is not None:
        with open(input_data["AQI FILE"], "r", encoding="utf-8") as f:
            input_data["AQI FILE"] = json.load(f)
    if input_data.get("AQI PURPLE_AIR", None) is not None:
        # get from API
        pass
    if input_data.get("REVERSE FILES", None) is not None:
        for file in input_data["REVERSE FILES"]:
            with open(file, "r", encoding="utf-8") as f:
                input_data["REVERSE FILES"][1].append(list(json.load(f).items()))
    if input_data.get("REVERSE NOMINATIM", None) is not None:
        # get from API
        pass

    return input_data


def parse_sensor_data(json_data):
    return json_data["data"]


def main():
    input_data = get_input()
    json_data = handle_input(input_data)
    print(json_data)
    input()
    aqi = parse_sensor_data(json_data["AQI FILE"])
    print(aqi)


if __name__ == "__main__":
    main()
