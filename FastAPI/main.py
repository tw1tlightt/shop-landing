# Запуск сайта через консоль
# uvicorn main:app --reload
# uvicorn путь_к_файлу:класс --параметр


from fastapi import FastAPI

from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles  #Библиотеки для работы с html css js
from fastapi.templating import Jinja2Templates

#Инициализация сайта
app = FastAPI() 


app.mount("/static", StaticFiles(directory="static"), name="static")
#Прикрепляем папку static для того, чтобы html мог обращатся к css js


templates = Jinja2Templates(directory="html")
# Поиск html файлов в папке html


# @app.get("/")
# def read_root():
#     return 'Hello'

# @app.get("/{num}")
# def nums(num: str | None = None):
#     return num
# @программа_получение("Ссылка")
# def название(входная_переменная: стока |(или) None = None(значение_по_умолчанию)):
#     return num'




@app.get("/", response_class=HTMLResponse) # Доп параметр для html
async def main(request: Request):  # request ужен для работы Jinja2
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"message": "Добро пожаловать в FastAPI + HTML!"}
    )