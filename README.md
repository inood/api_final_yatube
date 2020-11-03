# API для учебного проекта YA-TUBE

**Документация API: http://localhost:8000/redoc/**


**API начинается с /api/v1/**


Получить JWT-токен
```POST: /token/```

*content-type application/json:*
```
{
"username": "string",
"password": "string"
}
```

Обновить JWT-токен 

```POST: token/refresh/```

*content-type application/json:*

```
{
"refresh": "string"
}
```
