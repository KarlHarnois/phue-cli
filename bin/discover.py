import json
import urllib.request

with urllib.request.urlopen("https://discovery.meethue.com", timeout=5) as r:
    bridges = json.load(r)

if not bridges:
    raise SystemExit("No Hue bridges found")

for b in bridges:
    print(b["internalipaddress"])
