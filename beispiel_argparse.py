#!/usr/bin/env python3
#Usage:
#/home/codespace/.python/current/bin/python /workspaces/python-grundkurs-2685000/beispiel_argparse.py 5 --optional_int=3 --optional_str="Text" --wahl="a"

import argparse

parser=argparse.ArgumentParser(description="Beispiel für Argparse")
parser.add_argument("pflicht_int", help="Integer der erforderlich ist", type = int)
parser.add_argument("--optional_int", help="Integer der nicht erforderlich ist", type = int)
parser.add_argument("--optional_str", help="Optionaler String")
parser.add_argument("--wahl", help="Meine Wahl", choices=["a", "b","c","d"])
args = parser.parse_args()

print("Integer:", args.pflicht_int, "-Typ:", type(args.pflicht_int))
print("Optionaler Integer:", args.optional_int, "-Typ:", type(args.optional_int))
print("String:", args.optional_str, "-Typ:", type(args.optional_str))
print("Optionaler Integer:", args.wahl, "-Typ:", type(args.wahl))
