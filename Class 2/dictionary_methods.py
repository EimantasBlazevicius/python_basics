import json

sample_dict = {
    "name": "Eimantas",
    "age": 30,
    "city": "Vilnius",
    "cats": [
        "Yoda",
        "Obi"
    ]
}
# appending dictionary
sample_dict["color"] = "Blue"

# get values
print(sample_dict["name"])
print(sample_dict.get("city"))
print(sample_dict.get("potato", "Default Value"))

# deleting values from dictionary
del sample_dict["color"]
deleted_item = sample_dict.pop('age')
print(deleted_item)

print(json.dumps(sample_dict, indent=4))
