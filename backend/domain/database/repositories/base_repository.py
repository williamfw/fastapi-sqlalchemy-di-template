from doctest import FAIL_FAST
import stat
from typing import Generic, List, TypeVar
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from infrastructure.model.base_model import BaseModel

import inject

Model = TypeVar("Model", bound=BaseModel)

class BaseRepository(Generic[Model]):
    __abstract__ = True

    @inject.autoparams('session')
    def __init__(self, model: Model, session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def get(self, id: int) -> Model | None:
        async with self.session as session:
            return await session.get(self.model, id)
        
    async def get_all(self, skip: int, limit: int) -> List[Model] | None:
        async with self.session as session:
            statement = select(self.model).offset(skip).limit(limit)
            result = await session.execute(statement)
            return result.scalars().all()

    async def create(self, data: dict) -> Model:
        instance = self.model(**data)
        async with self.session as session:
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            
        return instance
    
    async def delete(self, id: int) -> bool | None:
        async with self.session as session:
            instance = await session.get(self.model, id)
            if instance:
                await session.delete(instance)
                await session.commit()
            else:
                return False
        
        return True
    
    async def update(self, data: dict) -> Model | bool:
        updating_model = self.model(**data)
        async with self.session as session:
            instance = await session.get(self.model, updating_model.id)
            if not instance:
                return False

            statement = update(self.model).where(self.model.id == updating_model.id).values(**data)
            await session.execute(statement)
            await session.commit()
            await session.refresh(instance)
        
        return instance
