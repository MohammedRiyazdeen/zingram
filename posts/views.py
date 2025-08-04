from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm

@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # include FILES for image
        if form.is_valid():
            post = form.save(commit=False) #its is not actually save yet
            post.author = request.user  # set the logged-in user as author
            post.save()
            return redirect('profile', username=request.user.username)  # redirect as you wish
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})
