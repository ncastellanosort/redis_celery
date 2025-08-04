from celery import Celery
import time
from config import REDIS_URL

celery = Celery("tasks", broker=REDIS_URL)

@celery.task
def send_email_task(recipient: str):
    print(f"enviando correo a {recipient}")
    time.sleep(5)
    print(f"correo enviado a {recipient}")

