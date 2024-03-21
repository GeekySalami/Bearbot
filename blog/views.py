from django.shortcuts import render,redirect
from .models import Post
from .forms import PostCreationForm
# Create your views here.
def blg(request):
    posts = Post.objects.all().order_by('-date_posted')

    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog')
    else:
        form = PostCreationForm()

    return render(request,'blog/blog_home.html', {'posts':posts,'forms':form})