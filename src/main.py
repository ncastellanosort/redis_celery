from fastapi import FastAPI
from routes.email_rt import email_rt
import config

app = FastAPI()

app.include_router(email_rt)

