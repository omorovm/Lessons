import json
def search(name: str) -> list[dict]:
    with open('db.json', 'r') as file:
        list_ = json.load(file)
        dict_ = []
        for i in list_:
            if name in i['title']:
                dict_ += [i]
    return dict_
print(search('as'))