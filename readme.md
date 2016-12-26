# secure word container
# startup
```sh
$ docker-compose build
$ docker-compose up
```

## login admin
- username: admin
- password: admin


# maintenance
## delete all
```sh
$ docker rm $(docker ps -a -q)
$ docker volume rm sword_data
```
