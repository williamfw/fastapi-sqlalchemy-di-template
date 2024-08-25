from fastapi import FastAPI
from contextlib import asynccontextmanager

from api.controllers.customers.customer_controller import CustomerController
from api.controllers.customers.job_controller import JobController
from infrastructure.ioc.ioc import IoC

import uvicorn
import infrastructure.database.database_session_manager as database_session_manager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database_session_manager.init_database()
    yield
    await database_session_manager.dispose_database()

app = FastAPI(lifespan=lifespan)

IoC().register_ioc()

app.include_router(CustomerController()._router)
app.include_router(JobController()._router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
