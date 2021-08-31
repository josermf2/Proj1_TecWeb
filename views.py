from utils import load_template, add_notes, build_response, load_database, extract_id
import urllib
from database import Note, Database

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    database = Database('bancoProjeto1')

    delete_or_update = False

    if 'deletar' in request:
        detail = extract_id(request)
        print(request)
        database.delete(detail)
        delete_or_update = True
        

    if "Content-Length: 10" in request:
        delete_or_update = True


    if request.startswith('POST') and delete_or_update == False:
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {'title': '', 'content': ''}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            if chave_valor.startswith('titulo'):
                params['title'] = urllib.parse.unquote_plus(chave_valor[chave_valor.find('=')+1:], encoding='utf-8', errors='replace')
            if chave_valor.startswith('detalhes'):
                params['content'] = urllib.parse.unquote_plus(chave_valor[chave_valor.find('=')+1:], encoding='utf-8', errors='replace')
        newNote = Note(title=params['title'], content=params['content'])
        database.add(newNote)

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id=dados.id, title=dados.title, details=dados.content)
        for dados in load_database('bancoProjeto1')
    ]
    notes = '\n'.join(notes_li)

    if request.startswith('POST'):
        response = build_response(code=303, reason='See Other', headers='Location: /')
    else:
        response = build_response()


    return response + load_template('index.html').format(notes=notes).encode()
