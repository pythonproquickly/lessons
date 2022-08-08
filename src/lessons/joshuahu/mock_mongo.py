# need to install mongomock pymongo
# https://github.com/mongomock/mongomock

import mongomock
import pymongo

def test_increase_votes():
    collection = mongomock.MongoClient().db.collection
    objects = [dict(votes=1), dict(votes=2), ...]
    for obj in objects:
        obj['_id'] = collection.insert_one(obj).inserted_id
    increase_votes(collection)
    for obj in objects:
        stored_obj = collection.find_one({'_id': obj['_id']})
        stored_obj['votes'] -= 1
        assert stored_obj == obj # by comparing all fields we make sure only votes changed


@mongomock.patch(servers=(('server.example.com', 27017),))
def test_increate_votes_endpoint():
    objects = [dict(votes=1), dict(votes=2), ...]
    client = pymongo.MongoClient('server.example.com')
    client.db.collection.insert_many(objects)
    call_endpoint('/votes')
    ... verify client.db.collection
