from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def homepage(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]
    context = {'posts': posts}
    return render(request, 'index/index.html', context)


def posts(request):
    posts = Post.objects.filter(active=True)
    context = {'posts': posts}
    page = request.GET.get('page')
    paginator = Paginator(posts, 3)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'index/posts.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'index/post.html', context)


def profile(request):
    return render(request, 'index/profile.html')


@login_required(login_url='home')
def createpost(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('posts')

    context = {'form': form}
    return render(request, 'index/post_form.html', context)


@login_required(login_url='home')
def Updatepost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('posts')

    context = {'form': form}
    return render(request, 'index/post_form.html', context)


login_required(login_url='home')

def deletepost(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    context = {'post': post}
    return render(request, 'index/delete.html', context)

# email view

def sendEmail(request):
    if request.method == 'POST':

        template = render_to_string('index/email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })
        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['nathamutinda1@gmail.com']
        )
        email.fail_silently = False
        email.send()
    return render(request, 'index/email_send.html')

