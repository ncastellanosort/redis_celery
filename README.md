# Redis & Celery example

## Redis
```
docker run -d -p 6379:6379 redis
```

## Celery
```
celery -A src.app.tasks worker --loglevel=info
```
