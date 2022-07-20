import pymongo
from pprint import pprint
from sqlite_example import connect_to_sqlite, execute_query
import queries


def connect_to_mongo(collection_name='test_db'):
    client = pymongo.MongoClient("mongodb+srv://:@cluster0.wxpufv4.mongodb.net/?retryWrites=true&w=majority")    
    db = client[collection_name]
    return db


def create_character_doc(character_tuple):
    """
    Take a character tuple and return a dict
    """
    sqlite_conn = connect_to_sqlite()
    query = f"""
SELECT i.item_id, i.name, i.value, i.weight
FROM charactercreator_character_inventory as ci
JOIN armory_item as i
	ON i.item_id = ci.item_id
WHERE ci.character_id = {character_tuple[0]}"""
    item_tuples = execute_query(sqlite_conn, query)
    items = []
    for row in item_tuples:
        item_dict = {
            'item_id': row[0],
            'name': row[1],
            'value': row[2],
            'weight': row[3]
        }
        items.append(item_dict)

    return {
        'character_id': character_tuple[0],
        'name': character_tuple[1],
        'level': character_tuple[2],
        'exp': character_tuple[3],
        'hp': character_tuple[4],
        'stength': character_tuple[5],
        'intelligence': character_tuple[6],
        'dexterity': character_tuple[7],
        'wisdom': character_tuple[8],
        'items': items
    }


def create_character_docs(character_list):
    docs = []
    for character_tuple in character_list:
        character_dict = create_character_doc(character_tuple)
        docs.append(character_dict)
    return docs



if __name__ == '__main__':
    db = connect_to_mongo('rpg_data')
    # db.characters.delete_many({})
    sqlite_conn = connect_to_sqlite()
    character_data = execute_query(sqlite_conn, queries.select_all_characters)
    docs = create_character_docs(character_data)
    db.characters.insert_many(docs)





# data = {
#     'name': 'joe',
#     'age': 30,
#     'fave color': 'red'
# }

# db.test_collection.insert_one(data)
# count = db.test_collection.count_documents({'name': 'joe'})
# print(count)
# doc = db.test_collection.find_one({'name': 'joe'})
# cursor = db.test_collection.find({})
# pprint(list(cursor))
# pprint(doc)
# db.test_collection.delete_one({'name': 'ben'})

# result = db.test_collection.update_one({'name': 'joe'}, {'$inc': {'age': 1}})
# pprint(result)