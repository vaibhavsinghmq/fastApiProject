# services/item_service.py
# from database.db_connector import get_db_connection

class ItemService:
    @staticmethod
    def get_item(item_id):
        return [{"name":"Hello World","Age":"30"}]

    @staticmethod
    def create_item(item_data):
        return [{"name":"Hello World 2","Age":"31"}]