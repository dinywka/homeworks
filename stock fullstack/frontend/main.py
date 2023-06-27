import asyncio
import sys
from PyQt6 import QtWidgets, uic
import aiohttp

app = QtWidgets.QApplication(sys.argv)


def get_text():
    data = {}
    text_le = window.lineEdit.text()
    data['title'] = text_le
    asyncio.run(send_data_to_server(data))


async def send_data_to_server(form_data):
    async with aiohttp.ClientSession() as session:
        async with session.post('http://127.0.0.1:8000/insert', data=form_data) as response:
            if response.status == 200:
                print("Success")
            else:
                print("Error sending data")


window = uic.loadUi("temp.ui")
window.pushButton.clicked.connect(get_text)
window.show()
app.exec()
