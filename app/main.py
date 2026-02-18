from fastapi import FastAPI
from app.logger import logger
from app.config import load_config

app = FastAPI()

config = load_config()

if config.debug:
    app.debug = True
else:
    app.debug = False

@app.get("/db")
def get_db_info():
    logger.info(f"Connecting to database: {config.db.database_url}")
    return {"database_url": config.db.database_url}

@app.get("/")
def read_root():
    logger.info("Handling request to root endpoint")
    return {"message": "Hello MIREA!"}


@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}