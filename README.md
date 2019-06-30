# Book Rest API

这是我练习 flask 的 Repo

## 说明：


### Endpoints

- /books: GET, get all books
- /book/<title>: GET, get a book
- /book/<title>: POST, add a book. `price` is required.
- /book/<title>: PUT, update or insert a book. `price` is required.
- /book/<title>: DELETE, delete a book

### 测试
在 Postman 中进行

## 任务1: vanilla flask

- 只使用 flask 框架
- 数据直接保存在 app.py 里。

## 任务2：Flask-RESTful

- 改为使用 Flask-RESTful 框架

## 任务3：Flask-sqlalchemy

- 使用 SQLite3，数据保存在 'data.db'
- 使用 Flask-sqlalchemy
