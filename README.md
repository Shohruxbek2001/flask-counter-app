# flask-counter-app

## Загрузка проекта
```bash
git clone <project_url>
cd flask-counter-app
```
## Запуск
```bash
docker-compose build
docker-compose up -d
docker exec -it flask_app python db.py
```
## тестирование
```sh
curl -X POST http://localhost:5000/count
```
