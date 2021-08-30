import json
from database import Database

def extract_route(string):
    inicialIndex = string.find('GET') + 5 
    finalIndex = string.find('HTTP') -1
    return string[inicialIndex:finalIndex]

def read_file(argument):
    extensions = ['html', 'txt', 'css', 'js']

    if str(argument).split('.')[-1] in extensions:
        with open(argument, 'r', encoding='utf-8') as file:
            content = file.read()
        return content.encode()
    else:
        with open(argument, 'rb') as file:
            content = file.read()
        return content  

def load_data(jsonName):
    with open('data/'+jsonName, 'r', encoding='utf-8') as file:
        conteudo = json.loads(file.read())
    return conteudo

def load_database(dbName):
    notes = Database(dbName).get_all()
    return notes

def load_template(templateName):
    with open('templates/'+templateName, 'r', encoding='utf-8') as file:
        conteudo = file.read()
    return conteudo

def add_notes(newDict):
    conteudo = load_data('notes.json')
    conteudo.append(newDict)
    newDict = json.dumps(conteudo)
    with open('data/notes.json', 'w', encoding='utf-8') as file:
        file.write(newDict)

def build_response(body = '', code = 200, reason = 'OK', headers = ''):
    if headers != '':
        return ('HTTP/1.1 ' + str(code) + ' ' + reason + '\n'+ headers  + '\n\n' + body).encode()
    else:
        return ('HTTP/1.1 ' + str(code) + ' ' + reason + '\n\n'  + body).encode()