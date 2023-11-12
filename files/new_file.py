import json
def update(id: int, title: str=None, price: int=None, rating: float=None) -> None:
    with open('db.json', 'r') as file:
        list_= json.load(file)
        print(list_)
        id_ = [i['id'] for i in list_]
        print(id_)
        if id not in id_:
            raise ValueError
        list_[id_.index(id)] = {'id': id, 'title': title, 'price': price, 'rating': rating}
    with open('new_db.json', 'w') as file:
        json.dump(list_, file)
    
update(1, 'product1',  1500, 4.6)