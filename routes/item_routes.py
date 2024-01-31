# routes/item_routes.py
from fastapi import APIRouter
from models.base_model import Item
from services.item_service import ItemService

router = APIRouter()

@router.post("/items/")
def create_item(item: Item):
    return ItemService.create_item(item.dict())

@router.get("/items/{item_id}")
def read_item(item_id: int):
    return ItemService.get_item(item_id)