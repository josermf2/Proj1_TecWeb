from types import resolve_bases
from utils import load_template, add_notes, build_response, load_database, extract_id
import urllib
from database import Note, Database

def create_Note(request):
    request = request.replace('\r', '')  # Remove caracteres indesejados
    partes = request.split('\n\n')
    corpo = partes[1]
    params = {'id':'', 'title': '', 'content': ''}
    for chave_valor in corpo.split('&'):
        if chave_valor.startswith('titulo'):
            params['title'] = urllib.parse.unquote_plus(chave_valor[chave_valor.find('=')+1:], encoding='utf-8', errors='replace')
        if chave_valor.startswith('detalhes'):
            params['content'] = urllib.parse.unquote_plus(chave_valor[chave_valor.find('=')+1:], encoding='utf-8', errors='replace')
    
    if params ==  {'id':'', 'title': '', 'content': ''}:
        for chave_valor in corpo.split('%26'):
            if chave_valor.startswith('atualizar'):
                params['id'] = chave_valor.split("%3D")[1]
            if chave_valor.startswith('title'):
                params['title'] = urllib.parse.unquote_plus(chave_valor.split("%3D")[1], encoding='utf-8', errors='replace')
            if chave_valor.startswith('details'):
                params['content'] = urllib.parse.unquote_plus(chave_valor.split("%3D")[1], encoding='utf-8', errors='replace')
        return Note(id=params['id'], title=params['title'], content=params['content'])
    
    return Note(title=params['title'], content=params['content'])

def recreate_Note(request):
    print(request)
    request = request.replace('\r', '')  # Remove caracteres indesejados
    partes = request.split('\n\n')
    corpo = partes[1]
    params = {'id':'', 'title': '', 'content': ''}
    for chave_valor in corpo.split('%26'):
        if chave_valor.startswith('atualizar'):
            params['id'] = chave_valor.split("%3D")[1]
        if chave_valor.startswith('title'):
            params['title'] = urllib.parse.unquote_plus(chave_valor.split("%3D")[1], encoding='utf-8', errors='replace')
        if chave_valor.startswith('details'):
            params['content'] = urllib.parse.unquote_plus(chave_valor.split("%3D")[1], encoding='utf-8', errors='replace')
            print(chave_valor.split("%3D"))

    return Note(title=params['title'], content=params['content'])

def index(request):
    # A string de request sempre come??a com o tipo da requisi????o (ex: GET, POST)
    database = Database('bancoProjeto1')
    deletedDatabase = Database('deletedNotes')
    delete_or_update = False
        

    if "atualizar" in request:
        newNote = create_Note(request)
        database.update(newNote)
        delete_or_update = True

    if "deleted" in request:
        detail = extract_id(request)
        deletedDatabase.delete(detail)
        delete_or_update = True    


    if request.startswith('POST') and delete_or_update == False:
        if "restaurar" in request:
            newNote = recreate_Note(request)
            detail = extract_id(request)
            deletedDatabase.delete(detail)
            database.add(newNote)
        elif 'deletar' in request:
            newNote = recreate_Note(request)
            detail = extract_id(request)
            database.delete(detail)
            deletedDatabase.add(newNote)
        else:
            newNote = create_Note(request)
            database.add(newNote)
        

    # Cria uma lista de <li>'s para cada anota????o
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id=dados.id, title=dados.title, details=dados.content)
        for dados in load_database('bancoProjeto1')
    ]
    
    deleted_note_template = load_template('components/deleted_note.html')
    deleted_notes_li = [
        deleted_note_template.format(id=dados.id, title=dados.title, details=dados.content)
        for dados in load_database('deletedNotes')
    ]

    notes = '\n'.join(notes_li)

    deleted_notes = '\n'.join(deleted_notes_li)

    if request.startswith('POST'):
        response = build_response(code=303, reason='See Other', headers='Location: /')
    else:
        response = build_response()


    return response + load_template('index.html').format(notes=notes, deleted_notes=deleted_notes, id=1).encode()
