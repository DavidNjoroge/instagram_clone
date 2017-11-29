from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserForm,ProfileForm,ProfilePicForm,NewPostForm,NewCommentForm
from .models import Post,Comment
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    current_user=request.user
    # comments=Comment.objects.filter(post_id=post_id)
    
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
        # elif comment_form.is_valid():
        #     print('<><>> the comment form is working<><><><')
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
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render (request,'update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
def post(request,post_id):
    comments=Comment.objects.filter(post_id=post_id)
    
    try:
        post=Post.objects.get(id=post_id)
    except DoesNotExist:
        raise Http404()
    current_user=request.user
    if request.method=='POST':
        comment_form=NewCommentForm(request.POST)
        print('<><><>half way<><>>')
        if comment_form.is_valid():
            print('it will save<><><><<><')
            comment=comment_form.save(commit=False)
            comment.user=current_user
            comment.post=post
            comment.save()
            # new_post=Post(user=current_user,post_image=post)
            # new_post.save()
    else:
        comment_form=NewCommentForm()
        print(len(comments))
    return render(request,'post.html',{'post':post,'comments':comments,'comment_form':comment_form})

def search(request):
    if 'search' in request.GET and not request.GET['search']==None:
        search_term=request.GET['search']
        print(search_term)
        users=User.objects.filter(username__icontains=search_term)
        print(len(users))
    return render (request,'search.html',{'users':users})