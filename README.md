# Redis & Celery example

## Docker Compose:
```
docker-compose up --build
```

## Local:
### Redis
```
docker run -d -p 6379:6379 redis
```

### Celery
```
PYTHONPATH=./src celery -A app.tasks worker --loglevel=info
```
