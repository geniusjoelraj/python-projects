#!/usr/bin/env python3
import argparse
import requests
import json


parser = argparse.ArgumentParser(description="Description of your script.")
parser.add_argument("arg1", type=str, help="Name of anime")

args = parser.parse_args().arg1
ss_path = "./anime-ss/" + args

# args = "anime-img.png"



res = requests.post("https://api.trace.moe/search",
  data=open(ss_path, "rb"),
  headers={"Content-Type": "image/jpeg"}
).json()

name = res["result"][0]["filename"]

# print(res)
print(name)
