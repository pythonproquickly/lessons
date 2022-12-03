import json
import os
import pathlib

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()


class MondayAPIHelper:
    def __init__(self, data):
        self.API_KEY = os.environ.get("API_KEY")
        self.req = requests
        self.API_URL = "https://api.monday.com/v2"
        self.HEADERS = {"Authorization": self.API_KEY}
        self.data = data

    @classmethod
    def build_project_hours_request(cls):
        query = """query {
                boards (ids: 3227946610) {
                  name
                  items {
                    name  
                    column_values {
                        title
                        text
                      }
                    }
                  }
                }"""
        data = {"query": query}
        return cls(data)

    def get_project_normal_business_hours(self):
        request = requests.post(
            url=self.API_URL, json=self.data, headers=self.HEADERS,
            verify=False
        )
        request = request.json()
        return request


j = MondayAPIHelper.build_project_hours_request()
j = j.get_project_normal_business_hours()
with open("board.json", "w") as f:
    f.write(json.dumps(j))


def parse_data(file_path, board_names):
    raw_data = json.loads(file_path.read_text(encoding="utf-8"))

    return {
        name: parse_board(board["items"])
        for board in raw_data["data"]["boards"]
        if (name := board["name"]) in board_names
    }


def parse_board(board_items):
    return [parse_item(board_item) for board_item in board_items]


def parse_item(board_item):
    return {"name": board_item["name"]} | {
        column["title"]: column["text"] for column in
        board_item["column_values"]
    }


data = parse_data(
    pathlib.Path("board.json"),
    board_names=["University of Massachusetts Medical School"],
)
print(pd.DataFrame(data["University of Massachusetts Medical School"]))
