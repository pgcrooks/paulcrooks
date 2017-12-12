from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post

def index(request):
    """
    Display the index page
    """
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    template = loader.get_template('pages/index.html')
    context = {
        'latest_post_list': latest_post_list,
    }
    return HttpResponse(template.render(context, request))

def latest(request):
    """
    View the latest blog post titles
    Future API
    """
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.title for p in latest_post_list])
    return HttpResponse(output)

def detail(request, post_id):
    """
    View a blog Post
    Future API
    """
    return HttpResponse('This will show post %d' % post_id)
