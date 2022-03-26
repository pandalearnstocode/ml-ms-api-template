from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter
from app.core import auth
from app.routes import views
from app.crud import crud

app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(views.router)
app.include_router(
    CRUDRouter(
        schema=crud.MMM,
        create_schema=crud.CreateMMM,
        update_schema=crud.UpdateMMM,
    )
)
