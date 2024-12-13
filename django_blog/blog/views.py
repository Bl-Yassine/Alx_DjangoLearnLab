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
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin

#ListView
class PostListiView(LoginRequiredMixin , ListView):
    model = Post
    template_name = 'blog/postlist.html'
    context_object_name ='posts'

#DetailView
class PostDetailView(LoginRequiredMixin , DetailView):
    model = Post
    template_name = 'blog/postdetail.html'

#CreateView
class PostCreateView(LoginRequiredMixin , CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/postcreate.html'
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
    template_name = 'blog/postedit.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()  
        return post.author == self.request.user 


#DeleteView
class PostDeleteView(LoginRequiredMixin , UserPassesTestMixin , DeleteView):
    model = Post
    template_name = 'blog/postdelete.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()  
        return post.author == self.request.user