from django.shortcuts import render

def get_poem(request):
    return render(request, 'blog/get_poem.html', {})

def post_list(request):
    return render(request, 'blog/post_list.html', {})