from django.shortcuts import render, redirect, get_object_or_404
from BookApp.models import Book
from BookApp.forms import BookForm

def records_view(request):
    books = Book.objects.filter(status='active')
    context = {"books": books}
    return render(request, "records.html", context)

def add_record(request):
    if request.method == "GET":
        form = BookForm()
        print(form)
        return render(request, "add_record.html", {"form": form})
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            book = Book.objects.create(author=form.cleaned_data.get('author'),
                                       email=form.cleaned_data.get('email'),
                                       text=form.cleaned_data.get('text'))
            return redirect('records_view')
        else:
            print(form.errors)
            return render(request, "records.html", {"form": form})

def edit_record(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "GET":
        form = BookForm(initial={
            "author": book.author,
            "email": book.email,
            "text": book.text
        })
        return render(request, "edit.html", {"form": form})
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            book.author = request.POST.get('author')
            book.email = request.POST.get("email")
            book.text = request.POST.get("text")
            book.save()
            return redirect("records_view")
        else:
            return render(request, "edit.html", {"form": form})

def delete_record(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == "GET":
        return render(request, "delete.html", {"book": book})
    else:
        book.delete()
        return redirect("records_view")