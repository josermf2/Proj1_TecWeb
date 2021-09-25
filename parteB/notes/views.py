from django.shortcuts import render, redirect
from .models import Note, Tag

def delete(request, delete_id):
    tag = Note.objects.get(id=delete_id).tag

    Note.objects.get(id=delete_id).delete()

    if Note.objects.filter(tag=tag).count() > 0:
        pass
    else:
        Tag.objects.get(tag=tag).delete()

    return redirect('index')

def post(request):     
    title = request.POST.get('titulo')
    content = request.POST.get('detalhes')
    tag  = request.POST.get('tag')

    if Tag.objects.filter(tag=tag).exists():    
        newNote = Note(title=title, content=content, tag=Tag.objects.get(tag=tag))
        newNote.save()

    elif not Tag.objects.filter(tag=tag).exists():
        newTag = Tag(tag=tag)
        newTag.save()
        newNote = Note(title=title, content=content, tag=Tag.objects.get(tag=newTag))
        newNote.save()
    
    return redirect('index')

def update(request, update_id='', title='', content='', tag=''):
    note = Note.objects.get(id=update_id)
    note.title = title
    note.content = content
    note.save()
    
    if Tag.objects.filter(tag=tag).exists():
        note.tag = Tag.objects.get(tag=tag)
        note.save()

    elif not Tag.objects.filter(tag=tag).exists():
        newTag = Tag(tag=tag)
        newTag.save()
        note.tag = Tag.objects.get(tag=tag)
        note.save()

    return redirect('index')

def index(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/notes.html', {'notes': all_notes})

def tags(request):
    all_tags = Tag.objects.all()
    return render(request, 'notes/tags.html', {'tags': all_tags})

def specific_tag(request, tag):
    all_notes = Note.objects.all().filter(tag=Tag.objects.get(tag=tag))
    return render(request, 'notes/specific_tag.html', {'notes': all_notes, 'tag_name':tag})
