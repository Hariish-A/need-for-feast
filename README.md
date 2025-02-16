# need-for-feast
## Introduction
A food delivery web application where customers order food from various restaurants that are within their vicinity. 

Role based interfaces are provided for Customer, Shop owners and Deliverer. 

Used `django` for backend, django templates with `CSS` for frontend and `sqlite3` for the database.

## ERD
![ERD of the food delivery system](https://github.com/hajay180505/need-for-feast/blob/main/ERD-nff.png)

## Installation
1. Clone the repository
```bash
git clone https://github.com/hajay180505/need-for-feast.git
```
2. Set up a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate # In windows .venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Set up the database
```bash
cd needForFeast
python manage.py makemigrations
python manage.py migrate
```
5. Run the server
```bash
python manage.py runserver
```
6. View the application by visiting `http://127.0.0.1:8000/`
