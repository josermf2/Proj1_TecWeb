import json
from database import Database, Note
from utils import load_data

db = Database('bancoProjeto1')
json = load_data('notes.json')

notes = []

identificador = 0
for note in json:
    notes.append(Note(id = identificador, title=note['titulo'], content=note['detalhes']))
    identificador += 1

for note in notes:
    db.add(note)

notes1 = db.get_all()
for note in notes1:
    print(f'Anotação {note.id}:\n  Título: {note.title}\n  Conteúdo: {note.content}\n')



deleted_notesDb = Database('deletedNotes')
json2 = load_data('deleted_notes.json')

notes2 = []

identificador = 0
for note in json2:
    notes2.append(Note(id = identificador, title=note['titulo'], content=note['detalhes']))
    identificador += 1

for note in notes2:
    deleted_notesDb.add(note)

notes3 = deleted_notesDb.get_all()
for note in notes3:
    print(f'Anotação {note.id}:\n  Título: {note.title}\n  Conteúdo: {note.content}\n')