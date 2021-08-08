# csv-pipe-playground

## what the purpose ?

playground project to get an understanding how processing csv files in an event driven manner can work using python and specific frameworks.

![csv pipe playground](/image/csv-pipe-playground.png)

## steps

1. Insert **csv** to root directory of solution
2. Filewatcher event will be triggered
3. Worker will be created via Rabbit MQ / Celery

   - Read CSV via Pandas
   - Store content in database

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