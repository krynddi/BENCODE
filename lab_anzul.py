import bencode # 
import json # готовое решение из пакета Python 

while True:
    request = input("BJ - перевод из Bencode в JSON\nJB - перевод из JSON в Bencode\n")
    if request == "BJ" or request == "JB":
        break

if request == "BJ":

    text = input("Введите текст в формате Bencode: ")
    py_data = bencode.DecodeBencode(text).start()
    print(json.dumps(py_data, indent=4))

if request == "JB":

    path = input("Введите путь до файла JSON: \n")
    with open(path, "r") as file:
        data = [line.rstrip() for line in file.readlines()]

    text = ""
    for i in data:
        text += i

    py_data = json.loads(text)
    print(bencode.EncodeBencode([py_data]).start())