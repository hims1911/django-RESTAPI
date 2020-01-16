from django.shortcuts import render, redirect , get_object_or_404
from .forms import PostForm
from .models import Post
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post

#Home view for post
class PostView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class IndexView(ListView):
    template_name = 'Crud1/index.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        return Post.objects.all()

#Detail view(view Post Detail)

class PostDetailView(DetailView):
    model = Post
    template_name = 'Crud1/post-detail.html'

#new Post View(Create new Post)
def postView(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = PostForm()
    return render(request,'Crud1/post.html',{'form':form})

#Edit a Post
def edit(request, pk, template_name='Crud1/edit.html'):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance = post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

#Delete post

def delete(request, pk, template_name = 'Crud1/confirm_delete.html'):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    return render(request, template_name, {'object': post})

