from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Message

def post_list(request, residence):
    if not request.user.is_authenticated:
        return redirect('login')
    posts = Post.objects.filter(residence=residence).order_by('-created_at')
    residence_names = {
        '1': 'إقامة 1',
        '2': 'إقامة 2',
        '3': 'إقامة 3',
        'outside': 'خارج الإقامة',
    }
    residence_name = residence_names.get(residence, 'إقامة')
    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'residence': residence,
        'residence_name': residence_name,
    })
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == 'POST' and request.user.is_authenticated:
        Comment.objects.create(
            post=post,
            author=request.user,
            content=request.POST['content']
        )
        return redirect('post_detail', pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
    })

@login_required
def add_post(request):
    if request.method == 'POST':
        Post.objects.create(
            author=request.user,
            content=request.POST['content'],
            residence=request.POST['residence'],
            image=request.FILES.get('image'),
        )
        return redirect('post_list', residence=request.POST['residence'])
    return render(request, 'blog/add_post.html')

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    residence = post.residence
    if post.author == request.user:
        post.delete()
    return redirect('post_list', residence=residence)

@login_required
def send_message(request, pk):
    receiver = get_object_or_404(request.user.__class__, pk=pk)
    if request.method == 'POST':
        Message.objects.create(
            sender=request.user,
            receiver=receiver,
            content=request.POST['content']
        )
        return redirect('post_list', residence='1')
    return redirect('post_list', residence='1')