from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Reader
from .forms import ReaderForm


def index(request):
    title = 'База читателей'
    readers = Reader.objects.all()
    return render(request, 'index.html', {'title': title, 'readers': readers})


def reader_add(request):
    title = 'Создание/Редактирование читателя'
    if request.method == 'POST':
        form = ReaderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = ReaderForm()
        return render(request, 'reader.html', {'form': form, 'title': title})


def reader_edit(request, pk):
    title = 'Создание/Редактирование читателя'

    reader = get_object_or_404(Reader, pk=pk)
    if request.method == 'POST':
        form = ReaderForm(request.POST, instance=reader)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ReaderForm(instance=reader)
        return render(request, 'reader.html', {'form': form, 'title': title})