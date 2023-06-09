import logging
from fastapi import FastAPI

from routers import users, items

from dependencies import get_today_with_underscores

app = FastAPI()

logging.basicConfig(
    filename=f"logs/api_log_{get_today_with_underscores()}.log",
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s'
)

app.include_router(users.router)
app.include_router(items.router)


