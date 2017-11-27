from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserForm,ProfileForm,ProfilePicForm,NewPostForm,NewCommentForm
from .models import Post
# Create your views here.
def index(request):
    current_user=request.user
    if request.method=='POST':
        form=NewPostForm(request.POST,request.FILES)
        # comment_form=NewCommentForm(request.POST)
        print('<><><>half way<><>>')
        if form.is_valid():
            post=form.save(commit=False)
            post.user=current_user
            post.save()
            # new_post=Post(user=current_user,post_image=post)
            # new_post.save()
            print('it will save<><><><<><')
        elif comment_form.is_valid():
            print('<><>> the comment form is working<><><><')
    else:
    
        form=NewPostForm()
        # comment_form=NewCommentForm()
    if current_user.is_authenticated():
        print('LOgged in')
        posts=Post.objects.filter(user=current_user)
    else:
        # print(len(posts))
        posts=[]
    return render(request,'index.html',{'form':form,'posts':posts})

def profile(request):
    profile_pic=ProfilePicForm()
    if request.method == 'POST':
        profile_pic=ProfilePicForm(instance=request.user)
        if profile_pic.is_valid():
            profile_pic.save()

            print('sadfgdafdgdsfgnv')

    return render(request,'profile.html',{'pic':profile_pic})

def update_profile(request):
    # if request.method == 'POST':
    #     user_form = UserForm(request.POST, instance=request.user)
    #     profile_form = ProfileForm(request.POST, instance=request.user.profile)
    #     if user_form.is_valid() and profile_form.is_valid():
    #         user_form.save()
    #         profile_form.save()
    #         messages.success(request, _('Your profile was successfully updated!'))
    #         return redirect('settings:profile')
    #     else:
    #         messages.error(request, _('Please correct the error below.'))
    # else:
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    # return render(request, 'profiles/profile.html', {
    #     'user_form': user_form,
    #     'profile_form': profile_form
    # })

    return render (request,'update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
