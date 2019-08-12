from flask_restful import Resource, reqparse
from models.store import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found!'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'A store with name {} does exists'.format(store)}

        store = StoreModel(name)
        store.save_to_db()
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': 'Store deleted!'}


class Stores(Resource):

    @staticmethod
    def get():
        return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}