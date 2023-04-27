
from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')


@app.route("/", methods=['GET'])
def home():

    with psycopg2.connect(
            user="postgres",
            password="28031989",
            host="127.0.0.1",
            port="5432",
            database="exam"
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                    "SELECT id, description FROM public.todo ORDER BY id ASC;"
                )
            records = cursor.fetchall()


    products = []
    for record in records:
        product = {
            "id": record[0],
            "description": record[1]
        }
        products.append(product)

    return render_template('pages/home.html', products=products)


@app.route('/create', methods=['GET', 'POST'])  # TODO Create (POST) [INSERT] Страница формой для создания книг
def create():
    if request.method == "GET":
        return render_template('pages/book_create.html')
    elif request.method == "POST":
        description = request.form['description']

        with psycopg2.connect(
                user="postgres",
                password="28031989",
                host="127.0.0.1",
                port="5432",
                database="exam"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO public.todo (description) VALUES (%s);",
                    (description, )
                )

        return redirect(url_for('home'))

