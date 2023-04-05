
from flask import Flask, render_template, request, redirect, url_for
# import psycopg2

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

@app.route("/", methods=['GET'])
def home():

    return render_template('pages/home.html')

@app.route('/create', methods=['GET', 'POST'])  # TODO Create (POST) [INSERT] Страница формой для создания книг
def create():
    if request.method == "GET":
        return render_template('pages/book_create.html')
    elif request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        author = request.form['author']
        with open("database.txt", mode="a", encoding="utf-8") as file:
            file.write(f"{title}_!_{description}_!_{author}\n")
        return redirect(url_for('book_list'))
    else:
        return redirect(url_for('home'))

@app.route('/list', methods=['GET', "POST"])  # TODO Read (GET) [SELECT] Общий список книг (сокращённый формат)
def book_list():
    with open("database.txt", mode="r", encoding="utf-8") as file:
        lines = file.readlines()
        new_lines = []
        for line in lines:
            if len(str(line)) > 3:
                new_lines.append(line)
        # lines = list(filter(lambda x: len(str(line)) > 3, lines))

        new_dictionaries = []
        for idx, line in enumerate(new_lines, 1):
            data = line.split("_!_")
            new_dict = {
                "id": idx,
                "title": data[0].strip(),
                "description": data[1].strip(),
                "author": data[2].strip()
            }
            new_dictionaries.append(new_dict)
        # new_dictionaries = [
        #     {"id": idx, "title": line.split("_!_")[0].strip(), "description": line.split("_!_")[1].strip(), "author": line.split("_!_")[2].strip()}
        #     for idx, line in enumerate(new_lines, 1)
        # ]
        print(new_dictionaries)
    return render_template('pages/book_list.html', books=new_dictionaries)
