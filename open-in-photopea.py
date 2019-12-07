#!/usr/bin/env python

import urllib.parse
import base64
import webbrowser
import json
import argparse
import sys
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--file", help="The path to the file to be opened in Photopea", type=str)

args = parser.parse_args()
	
with open(args.file, "rb") as file:
	bytes = file.read()
	
extension = Path(args.file).suffix.replace(".","")

with base64.b64encode(bytes) as encoded_bytes
	encoded_str = "".join(chr(x) for x in encoded_bytes)

data_str = 'data:' + extension + ';base64,' + encoded_str

query_dict = {'files': [data_str]}
query_json = json.dumps(query_dict)

encoded_query = urllib.parse.quote(query_json, safe = ":;,/.")

url = 'https://www.photopea.com/#' + encoded_query

webbrowser.open(url, new=1)
