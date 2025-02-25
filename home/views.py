from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from home.models import Posts, Category
from django.contrib.auth.forms import UserCreationForm


def home(request):
    papers = Posts.objects.all().order_by('-post_time')
    categories = Category.objects.all()
    recent_posts = Posts.objects.all().order_by('-post_time')
    paper_Data = {
        'papers': papers,
        'categories': categories,
        'recent_posts': recent_posts
    }
    return render(request, 'turnup/index.html', paper_Data)


def about(request):
    categories = Category.objects.all()
    return render(request, 'turnup/about.html', {'categories': categories})


def paper(request, url):
    single_post = Posts.objects.get(url=url)
    related_posts = Posts.objects.filter(cat=single_post.cat).exclude(url=url)
    categories = Category.objects.all()

    return render(
        request, 'turnup/paper.html', {
            'single_post': single_post,
            'categories': categories,
            'related_posts': related_posts
        })


def category(request, url):
    cat = Category.objects.get(url=url)
    categories = Category.objects.all()
    posts = Posts.objects.filter(cat=cat)
    return render(request, 'turnup/categoy.html', {
        'cat': cat,
        'categories': categories,
        'posts': posts
    })


def categorypage(request):
    categories = Category.objects.all()
    papers = Posts.objects.all()
    cat_Data = {'papers': papers, 'categories': categories}
    return render(request, 'turnup/allcategory.html', cat_Data)


def loginpage(request):
    return render(request, 'turnup/login.html')


def registerpage(request):
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'turnup/register.html', context)
