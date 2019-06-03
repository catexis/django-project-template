import json
import pickle

import requests

# URL as global variable
URL = "https://www.cbr-xml-daily.ru/daily_json.js"


def get_external_data():
    req = requests.get(URL)
    if req.status_code == 200:
        ret = json.loads(req.text)
        with open("debug_obj.dbg", "wb") as outf:
            pickle.dump(req, outf)
    else:
        ret = dict()
    return ret


if __name__ == "__main__":
    # Run first as call function for object save
    get_external_data()
    # Comment line with func call to work with saved object
    # with open("debug_obj.dbg", "wb") as inpf:
    #     old_obj = pickle.load(inpf)
    # print(old_obj.text)
