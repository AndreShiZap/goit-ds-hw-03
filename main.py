from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(
    "mongodb+srv://andreshizap:567234@cluster0.pqxcf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    server_api=ServerApi('1')
)

db = client.book

def add_all():
    db.cats.insert_many(
        [
            {
                "name": "barsik",
                "age": 3,
                "features": ["ходить в капці", "дає себе гладити", "рудий"],
            },
            {
                "name": "Lama",
                "age": 2,
                "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
            },
            {
                "name": "Liza",
                "age": 4,
                "features": ["ходить в лоток", "дає себе гладити", "білий"],
            },
        ]
    )


def read_all():
    result = db.cats.find({})
    for el in result:
        print(el)

def read_one(cat):
    result = db.cats.find_one({'name': cat})
    if result:
        print(result)
    else:
        print(f'Cat with name {cat} not found.')


def update_age(cat: str, age_cat: int):
    result = db.cats.find_one({'name': cat})
    if result:
        db.cats.update_one({"name": cat}, {"$set": {"age": age_cat}})
        result = db.cats.find_one({'name': cat})
        print(result)
    else:
        print(f'Cat with name {cat} not found.')

def add_features(cat: str, feature: list):
    result = db.cats.find_one({'name': cat})
    if result:
        db.cats.update_one({"name": cat}, {"$push": {"features": {"$each": feature}}})
        result = db.cats.find_one({'name': cat})
        print(result)
    else:
        print(f'Cat with name {cat} not found.')


def delete_one(cat):
    result = db.cats.find_one({"name": cat})
    if result:
        db.cats.delete_one({"name": cat})
        print(f'Cat with name {cat} was deleted')
    else:
        print(f'Cat with name {cat} not found.')


def delete_all():
    result = db.cats.delete_many({})
    print(f"Видалено записів: {result.deleted_count}")


if __name__ == '__main__':
    read_all() # читання всіх записів
    read_one('barsik') # читання одного запису
    # update_age('barsik', 4) # обновлення запису
    # add_features('barsik', ['хропить', 'злий']) # додавання нових властивостей
    # delete_one('barsik') # видалення запису
    # delete_all() # видалення всіх записів
    # add_all() # додавання записів до БД