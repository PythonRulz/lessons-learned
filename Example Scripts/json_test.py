import json

d = '{ "topic": "eog.cc.v1", "ts": 1684246362, "payload": {"connected":"true","device":{"cellular":{"valid":"false"},"cid":"PSI_BX_3","location":{"valid":"false"},"status":"okay"},"timestamp":"2023-05-16T14:12:43.000Z"}}'
# json_acceptable_string = d.replace("'", "\"")
diction = json.loads(d)
# print(diction)
print(len(d))
