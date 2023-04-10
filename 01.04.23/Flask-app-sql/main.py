
from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

# @app.route("/", methods=['GET'])
# def home():
#     with psycopg2.connect(
#             user="postgres",
#             password="28031989",
#             host="127.0.0.1",
#             port="5432",
#             database="hw01.04.23"
#     ) as connection:
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 "SELECT id, title, description, price, count FROM public.store_db ORDER BY id ASC;"
#             )
#             records = cursor.fetchall()
#
#     products = []
#     for record in records:
#         product = {
#             "id": record[0],
#             "title": record[1],
#             "description": record[2][:15:1] + "..." if len(record[2]) > 15 else record[2],
#             "price": record[3],
#             "count": record[4]
#         }
#         products.append(product)
#
#     return render_template('pages/home.html', products=products)


@app.route("/", methods=['GET'])
def home():
    search_query = request.args.get('search', '')

    with psycopg2.connect(
            user="postgres",
            password="28031989",
            host="127.0.0.1",
            port="5432",
            database="hw01.04.23"
    ) as connection:
        with connection.cursor() as cursor:
            if search_query:
                cursor.execute(
                    "SELECT id, title, description, price, count FROM public.store_db WHERE title ILIKE %s ORDER BY id ASC;",
                    ('%' + search_query + '%',)
                )
            else:
                cursor.execute(
                    "SELECT id, title, description, price, count FROM public.store_db ORDER BY id ASC;"
                )
            records = cursor.fetchall()

    products = []
    for record in records:
        product = {
            "id": record[0],
            "title": record[1],
            "description": record[2][:15:1] + "..." if len(record[2]) > 15 else record[2],
            "price": record[3],
            "count": record[4]
        }
        products.append(product)

    return render_template('pages/home.html', products=products, search_query=search_query)


@app.route('/create', methods=['GET', 'POST'])  # TODO Create (POST) [INSERT] Страница формой для создания книг
def create():
    if request.method == "GET":
        return render_template('pages/book_create.html')
    elif request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        count = request.form['count']

        with psycopg2.connect(
                user="postgres",
                password="28031989",
                host="127.0.0.1",
                port="5432",
                database="hw01.04.23"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO public.store_db (title, description, price, count) VALUES (%s, %s, %s, %s);",
                    (title, description, price, count)
                )

        return redirect(url_for('home'))

# @app.route('/list', methods=['GET', "POST"])  # TODO Read (GET) [SELECT] Общий список книг (сокращённый формат)
# def book_list():
#     title = request.form.get("title", "")
#
#     with psycopg2.connect(
#             user="postgres",
#             password="28031989",
#             host="127.0.0.1",
#             port="5432",
#             database="hw01.04.23"
#     ) as connection:
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 "SELECT id, title, description, price, count FROM public.store_db  WHERE title LIKE %s ORDER BY id ASC;",
#                 (f"%{title}%",)
#             )
#             records = cursor.fetchall()
#
#     print("records: ", records)
#     _products = []
#     for record in records:
#         new_dict = {
#             "id": record[0],
#             "title": record[1],
#             "description": record[2][:15:1] + "..." if len(record[2]) > 15 else record[2],
#             "price": record[3],
#             "count": record[4]
#         }
#         _books.append(new_dict)
#
