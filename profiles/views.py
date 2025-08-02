from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from profiles.models import Profile

# profiles/views.py


@login_required
def edit_profile(request):
    profile = request.user.profile  # Get the profile linked to current user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile) 

                    #instance=profile is for editing or updating existing one instead of creating new profile, 
                    # without instance=profile its creating a new profile
        
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileForm(instance=profile)
       
    
    return render(request, 'profiles/edit_profile.html', {'form': form})




def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile

    is_following = False
    if request.user.is_authenticated:
        is_following = profile.followers.filter(id=request.user.id).exists() 

                       #or alternavtive way below

        #is_following = False
        #if request.user.is_authenticated and request.user in profile.followers.all():
        #   is_following = True 

        # the both line does are same thing

    followers_count = profile.followers.count()
    following_count = user.following.count()

    context = {
        'profile_user': user,
        'profile': profile,
        'is_following': is_following,
        'followers_count': followers_count,
        'following_count': following_count,
    }
    return render(request, 'profiles/profile.html', context)



from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

@login_required
def follow_unfollow_view(request, username):
    target_user = get_object_or_404(User, username=username)
    target_profile = get_object_or_404(Profile, user=target_user)

    if target_user != request.user:
        if request.user in target_profile.followers.all():
            target_profile.followers.remove(request.user)
        else:
            target_profile.followers.add(request.user)

    return redirect('profile', username=username)


from django.contrib.auth.models import User

def followers_list(request, username):
    user = get_object_or_404(User, username=username)
    followers = user.profile.followers.all()

    context = {
        'title': f"{user.username}'s Followers",
        'users': followers,
    }
    return render(request, 'profiles/follow_list.html', context)

def following_list(request, username):
    user = get_object_or_404(User, username=username)
    following = Profile.objects.filter(followers=user)

    context = {
        'title': f"{user.username} is Following",
        'users': following,
    }
    return render(request, 'profiles/follow_list.html', context)

