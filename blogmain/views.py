from django.shortcuts import redirect


def redir_blog(request):
    return redirect('posts_list_url')
