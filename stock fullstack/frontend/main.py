import asyncio
import sys
from PyQt6 import QtWidgets, uic
import aiohttp

app = QtWidgets.QApplication(sys.argv)

#
# def get_text():
#     data = {}
#     text_le = window.lineEdit.text()
#     data['title'] = text_le
#     asyncio.run(send_data_to_server(data))

def get_text():
    data = {}
    text_le = window.lineEdit.text()
    data['title'] = text_le
    asyncio.run(send_data_to_server(data))
    asyncio.run(fetch_data_from_server())

async def send_data_to_server(form_data):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://127.0.0.1:8000/insert', data=form_data) as response:
            if response.status == 200:
                print("Success")
            else:
                print("Error sending data")


async def fetch_data_from_server():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://127.0.0.1:8000/ideas') as response:
            if response.status == 200:
                data = await response.json()
                display_data_in_table(data)
            else:
                print("Error fetching data")


def display_data_in_table(data):
    window.tableWidget.setRowCount(len(data))
    window.tableWidget.setColumnCount(1)
    for row, item in enumerate(data):
        title = item.get('title')
        print(title)
        table_item = QtWidgets.QTableWidgetItem(title)
        window.tableWidget.setItem(row, 0, table_item)







window = uic.loadUi("temp.ui")
window.pushButton.clicked.connect(get_text)
window.show()
app.exec()
