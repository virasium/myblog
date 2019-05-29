from django.shortcuts import render,redirect
from django.views.generic import View
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *

# Create your views here.
class PostsList(View):
    def get(self,request):
        posts = Post.objects.all()
        return render(request,'blog/post/posts_list.html',{'posts':posts})

class PostDetail(View):
    def get(self,request,slug):
        post = Post.objects.get(slug = slug)
        form = CommentForm()
        return render(request,'blog/post/post_detail.html',{'post':post,'form':form})

    def post(self,request,slug):
        post = Post.objects.get(slug = slug)
        form = CommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.author = request.user
            new_form.post = post
            new_form.save()
            return redirect(post)
        return render(request,'blog/post/post_detail.html',{'post':post,'form':form})

class PostCreate(LoginRequiredMixin,View):
    def get(self,request):
        formP = FormCreatePost()
        return render(request,'blog/post/post_create.html',{'formP':formP})

    def post(self,request):
        formP = FormCreatePost(request.POST)
        if formP.is_valid():
            new_post = formP.save()
            new_post.author = request.user
            new_post.save()
            return redirect(reverse('posts_list_url'))
        return render(request,'blog/post/post_create.html',{'formP':formP})
    raise_exception = True

class PostUpdate(LoginRequiredMixin,View):
    def get(self,request,slug):
        post = Post.objects.get(slug = slug)
        formP = FormCreatePost(instance = post)
        return render(request,'blog/post/post_update.html',{'formP':formP,'post':post})
    def post(self,request,slug):
        post = Post.objects.get(slug = slug)
        formP = FormCreatePost(request.POST,instance = post)
        if formP.is_valid():
            formP.save()
            return redirect(post)
        return render(request,'blog/post/post_update.html',{'formP':formP,'post':post})
    raise_exception = True

class PostDelete(LoginRequiredMixin,View):
    def get(self,request,slug):
        post = Post.objects.get(slug = slug)
        return render(request,'blog/post/post_delete.html',{'post':post})
    def post(self,request,slug):
        post = Post.objects.get(slug = slug)
        post.delete()
        return redirect(reverse('posts_list_url'))

class TagsList(View):
    def get(self,request):
        tags = Tag.objects.all()
        return render(request,'blog/tag/tags_list.html',{'tags':tags})

class TagDetail(View):
    def get(self,request,slug):
        tag = Tag.objects.get(slug = slug)
        return render(request,'blog/tag/tag_detail.html',{'tag':tag})

class TagCreate(LoginRequiredMixin,View):
    def get(self,request):
        form = FormCreateTag()
        return render(request,'blog/tag/tag_create.html',{'form':form})
    def post(self,request):
        form = FormCreateTag(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('post_create_url'))
        return render(request,'blog/tag/tag_create.html',{'form':form})
    raise_exception = True


def comm_delete(request,id):
    comm = Comment.objects.get(id = id)
    post = comm.post
    comm.delete()
    return redirect(post)
