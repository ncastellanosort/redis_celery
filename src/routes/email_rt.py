from fastapi import APIRouter
from app.tasks import send_email_task
import time

email_rt = APIRouter()

@email_rt.get("/send_email/{recipient}")
def send_email(recipient: str):
    send_email_task.delay(recipient) # .delay to make it run by celery
    return {"message": f"correo siendo enviado a {recipient}"}

@email_rt.post("/no_celery")
def no_celery_send_email(recipient: str):
    time.sleep(5)
    return {"status": f"correo enviado a {recipient}"}

