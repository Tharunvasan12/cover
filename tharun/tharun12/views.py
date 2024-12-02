from django.shortcuts import render

def cover_page(request):
    return render(request,'book.html')
