from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class PostsList(View):
    def get(self,request):
        return render(request,'blog/posts_list.html')
