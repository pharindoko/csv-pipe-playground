# csv-pipe-playground

## what`s the purpose ?

playground project to get an understanding how processing csv files in an event driven manner using docker-compose and specific frameworks without the use of cloud components.

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
git clone https://github.com/pharindoko/csv-pipe-playground.git
cd csv-pipe-playground
make build
```

## start

```bash
make run
```

## try out

### add a csv file

> you have 2 options to start the process

#### using linux

- Add a csv file into the root directory or a nested directory of the source folder (works recursively).
- This is limited to linux as I`m using Pyinotify which supports IN_CLOSE_WRITE (relies on linux kernel)

#### using macos, windows or linux

1. Open vue application (<http://localhost:3000/>)
1. Drag and drop csv file(s) or select file(s) via file dialog
1. Click on button "Upload"

> data will be written into postgre db

### graphql

Open Graphql Playground  
<http://localhost:5433/graphiql>

> new endpoints will be automagically added by postgraphile when a new csv has been added)

### database

Open a DB Connection
postgres://postgres:postgres@postgres:5432/postgres

> recommendation is to use a db client like dbeaver

## sidenotes

It might be a discussion point if celery and rabbitmq are a bit too much for this solution.

But I really enjoyed how easy it is to implement rabbitmq and celery and how stable this works.

Having IO operations and database connections I guess it`s not that bad to split it up into other processes and keep the event handler process lean.
