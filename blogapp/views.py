from textwrap import fill
from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import Blogform, BlogModelForm, CommentForm
# Create your views here.
def home(request):
    # To show all the posts in home. 
    # posts = Blog.objects.all()
    posts = Blog.objects.filter.order_by('-date') # code to filter, this one is by order of date 
    return render(request, 'index.html', {'posts':posts})

# html to show for a user to write a new post
def new(request):
    return render(request, 'new.html')

# function to save a post
def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()

    return redirect('home')


# function to get an input using django form.
# can handle with both GET (=입력값을 받을수 있는 html을 갖다 줘야함) request and \
# POST (=입력한 내용을 데이터베이스에 저장. form 에서 입력한 내용을 처리) request. 
def formcreate(request):
    if request.method == 'POST':
        #입력 내용을 DB에 저장
        form = Blogform(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        #입력을 받을 수 있는 html을 갖다주기.
        form = Blogform()
    return render(request, 'form_create.html', {'form':form})

def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form':form})

def detail(request, blog_id):
    # blog_id 번째 블로그 글을 데이터베이스로부터 갖고와서
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    # blog_id 번째 블로그 글을 detial.html로 띄우는 코드

    comment_form = CommentForm()
    return render(request, 'detail.html', {'blog_detail':blog_detail, 'comment_form':comment_form})

def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save()

    return redirect('detail', blog_id)