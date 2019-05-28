from django.shortcuts import render,redirect
from django.views.generic import View
from django.urls import reverse

from .models import *
from .forms import *

# Create your views here.
class PostsList(View):
    def get(self,request):
        posts = Post.objects.all()
        return render(request,'blog/posts_list.html',{'posts':posts})

class PostDetail(View):
    def get(self,request,slug):
        post = Post.objects.get(slug = slug)
        form = CommentForm()
        return render(request,'blog/post_detail.html',{'post':post,'form':form})

    def post(self,request,slug):
        post = Post.objects.get(slug = slug)
        form = CommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.author = request.user
            new_form.post = post
            new_form.save()
            return redirect(post)
        return render(request,'blog/post_detail.html',{'post':post,'form':form})


class TagsList(View):
    def get(self,request):
        tags = Tag.objects.all()
        return render(request,'blog/tags_list.html',{'tags':tags})

class TagDetail(View):
    def get(self,request,slug):
        tag = Tag.objects.get(slug = slug)
        return render(request,'blog/tag_detail.html',{'tag':tag})
