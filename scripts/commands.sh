#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e



collectstatic.sh
makemigrations.sh
migrate.sh
runserver.sh
wait_psql.sh