# csv-processing

## what the purpose ?

process csv files in an event driven manner.

![csv-processing](/image/csv-processing.png)

## steps

1. Insert **csv** to root directory of solution
2. Filewatcher event will be triggered
3. Worker will be created via Rabbit MQ / Celery

- Read CSV via Pandas
- Store content as json in database

## requirements

- docker
- docker-compose
- linux (pyinotify)

## install

```bash
make build
```

## start

```bash
make run
```