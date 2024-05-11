from typing import List, Optional
from uuid import UUID
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
import pymongo

from store.core.exceptions import BadRequestException, NotFoundException
from store.db.mongo import db_client
from store.models.base import datetime_now
from store.models.product import ProductModel
from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut


class ProductUsecase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        product_model = ProductModel(**body.model_dump())
        product_model.created_at = datetime_now()
        product_model.updated_at = datetime_now()
        await self.collection.insert_one(product_model.model_dump())

        return ProductOut(**product_model.model_dump())

    async def get(self, id: UUID) -> ProductOut:
        result = await self.collection.find_one({"id": id})

        if not result:
            raise NotFoundException(message=f"Product not found with filter: ID={id}")

        return ProductOut(**result)

    async def query(self, filter: Optional[dict] = None) -> List[ProductOut]:
        if filter is None:
            filter = {}
        return [ProductOut(**item) async for item in self.collection.find(filter)]

    async def update(self, id: UUID, body: ProductUpdate) -> ProductUpdateOut:
        update_body = body.model_dump(exclude_none=True)
        update_body["updated_at"] = datetime_now()
        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": update_body},
            return_document=pymongo.ReturnDocument.AFTER,
        )
        if not result:
            raise BadRequestException(message=f"Product not found with filter: ID={id}")

        return ProductUpdateOut(**result)

    async def delete(self, id: UUID) -> bool:
        product = await self.collection.find_one({"id": id})

        if not product:
            raise NotFoundException(message=f"Product not found with filter: ID={id}")

        result = await self.collection.delete_one({"id": id})

        return True if result.deleted_count > 0 else False


product_usecase = ProductUsecase()
