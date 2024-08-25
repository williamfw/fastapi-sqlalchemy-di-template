from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from infrastructure.model.base_model import BaseModel
from domain.database.models.customer_model import Customer
from domain.database.models.job_model import Job

from infrastructure.settings.settings import settings

async_engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
session_factory = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
    autoflush=False,
    future=True
)

async def dispose_database() -> None:
    await async_engine.dispose()
    session_factory = None

async def init_database() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)

def get_sync_session() -> AsyncSession:
    return session_factory()

#TODO analisar a injecao de session asincrono e com contextmanager futuramente!
# engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
# sync_session = sessionmaker(
#     engine,
#     expire_on_commit=False,
#     autoflush=False,
#     future=True
# )

# def dispose_database() -> None:
#     engine.dispose()
#     session = None

# def init_database() -> None:
#     BaseModel.metadata.create_all(bind=engine)

# @contextmanager
# def get_db_session() -> Generator[Session, Any, Any]:
#     session: Session = sync_session()
#     with session as session:
#         try:
#             session.begin()
#             yield session
#         except IntegrityError as exception:
#             # Log the exception or handle it appropriately here
#             session.rollback()
#         finally:
#             session.close()