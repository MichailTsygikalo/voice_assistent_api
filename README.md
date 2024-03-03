# voice_assistent_api
## Клонировать репу 
```sh
git clone https://github.com/MichailTsygikalo/voice_assistent_api.git
```
## Запуск приложения
```sh
cd voice_assistent_api
docker-compose -f infra/docker-compose.yaml up --build -d
```
Приложение работает на `localhost:8080`  

Документация `localhost:8080/docs`

## Миграции
```sh
alembic upgrade head    
```
