from django.shortcuts import render

# Create your views here.

#User Registration

from .forms import RegisterUserForm , EditUserForm
from django.shortcuts import redirect

def basepage(request):
    return render (request, 'blog/base.html',)

def registeruser(request):
    form = RegisterUserForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render (request,'blog/register.html',{'form':form })

from django.contrib.auth.decorators import login_required
@login_required
def profileinfo(request):
    current_user = request.user
    context = {
        'user': current_user,
    }
    return render (request , 'blog/profile.html',context)

@login_required
def editProfile(request):
    if request.method == "POST":
        form = EditUserForm(request.POST , instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render (request,'blog/edit_profile.html',{'form':form })


#Create Djnago Views for each CRUD Operation
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DetailView , DeleteView
from django.urls import reverse_lazy
from .models import Post , Comment
from .forms import PostForm , CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.db.models import Q
#ListView
class PostListiView(LoginRequiredMixin , ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name ='posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | 
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)  # If using django-taggit
            ).distinct()
        return queryset

#DetailView
class PostDetailView(LoginRequiredMixin , DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

#CreateView
class PostCreateView(LoginRequiredMixin , CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        post = form.save(commit=False)  
        post.author = self.request.user 
        post.save()              
        return super().form_valid(form)


#UpdateView
class PostUpdateView(LoginRequiredMixin ,UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()  
        return post.author == self.request.user 


#DeleteView
class PostDeleteView(LoginRequiredMixin , UserPassesTestMixin , DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()  
        return post.author == self.request.user
    


#ListView Comment
class CommentListiView(LoginRequiredMixin , ListView):
    model = Comment
    template_name = 'blog/comment_list.html'
    context_object_name ='comments'

#DetailView Comment
class CommentDetailView(LoginRequiredMixin , DetailView):
    model = Comment
    template_name = 'blog/comment_detail.html'
    context_object_name ='comments'



#CreateView Comment
class CommentCreateView(LoginRequiredMixin , CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_create.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        post = form.save(commit=False)  
        post.author = self.request.user 
        post.save()              
        return super().form_valid(form)
    

#UpdateView Comment
class CommentUpdateView(LoginRequiredMixin ,UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_edit.html'
    success_url = reverse_lazy('posts')
    def test_func(self):
        post = self.get_object()  
        return post.author == self.request.user
    

#DeleteView
class CommentDeleteView(LoginRequiredMixin , UserPassesTestMixin , DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()  
        return post.author == self.request.user
    

from django.shortcuts import render
from .models import Post

def posts_by_tag(request, tag_name):
    posts = Post.objects.filter(post_tag__icontains=tag_name)
    return render(request, 'blog/posts_by_tag.html', {'posts': posts, 'tag': tag_name})


class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/posts_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')
        return Post.objects.filter(post_tag__icontains=tag_slug)
