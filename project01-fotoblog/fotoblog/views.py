from django.shortcuts import render,get_object_or_404,redirect
from fotoblog.models import Page , Post
from forms.forms import PageForm , PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login , logout
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.paginator import Paginator




def page_views (request,page_slug=None):
    if page_slug == "login":
        return login_views (request)
    if page_slug == "logout":
        return logout_views (request)
    if page_slug == "register":
        return register (request)
    if page_slug == "post-share":
        return post_share (request)
    if page_slug and not page_slug =="home":
        page = get_object_or_404 (Page,slug=page_slug,is_active=True)
        if page_slug == "add-page":
            if request.user.is_authenticated and request.user.is_superuser:
                return add_page (request,page_slug)
            else:
                return redirect ("fotoblog:home_views")
    elif page_slug == None or page_slug == "home":
        p_posts = Post.objects.filter (is_active=True).order_by("-id")
        set_posts = Paginator (p_posts,3)
        page_number = request.GET.get ("page")
        posts = set_posts.get_page(page_number)
        title = "Home"
        page = get_object_or_404 (Page,slug="home",is_active=True)
        context = dict(posts=posts,page=page,)
        return render (request,"pages/page-views.html",context)
    context = dict(
        page=page,
    )
    return render (request,"pages/page-views.html",context)



def add_page (request,page_slug):
    if request.method == "POST":
        page_form = PageForm (request.POST,request.FILES)
        if page_form.is_valid():
            form_title = request.POST.get ("title")
            is_page = Page.objects.filter (title__icontains=form_title).exists()
            if not is_page:
                page_form.save()
                messages.success(request, "The page has been successfully added!")
            else:
                messages.warning(request, "Already exists!")
            return redirect("fotoblog:home_views")
    else:
        page_form = PageForm ()
    context = dict (page_form=page_form,page=get_object_or_404(Page,slug=page_slug))
    return render (request,"pages/page-views.html",context)


def login_views (request):
    title = "Login"
    if request.method == "POST":
        username = request.POST.get ("username")
        password = request.POST.get ("password")
        login_user = authenticate(username=username,password=password)
        if login_user is not None:
            auth_login(request,login_user)
            messages.info (request,"Logged in successfuly!")
            return redirect ("fotoblog:home_views")
        else:
            messages.warning (request,"Invalid username or password!")
    context = dict (
        page_title=title,
    )
    return render (request,"pages/login-page.html",context)
    

def logout_views (request):
    logout (request)
    messages.success (request,"Logged out successfuly!")
    return redirect ("fotoblog:home_views")



def register (request):
    title = "Register"
    if request.method == "POST":
        username = request.POST.get ("username")
        password = request.POST.get ("password")
        confirm_password = request.POST.get ("confirm_password")
        if password == confirm_password:
            register_user = authenticate (username=username,password=password)
            if register_user is not None:
                auth_login(request,register_user)
                messages.warning (request,"User is already exists!")
                return redirect ("fotoblog:home_views")
            else:
                User.objects.create_user (username=username,password=password)
                messages.success (request,"The user has been successfully registered!")
                return redirect ("fotoblog:home_views")
            
    context = dict (page_title=title,)
    return render (request,"pages/register-page.html",context)
    


def post_share (request):
    if request.method == "POST":
        post_form = PostForm (request.POST,request.FILES)
        if post_form.is_valid ():
            post_form.save(commit=False)
            title = post_form.cleaned_data.get ("title")
            slug = slugify (title)
            post = Post.objects.filter (slug=slug).exists()
            if post:
                print (post_form)
                messages.warning (request, "Post is already exists!")
            else:
                post_form.save()
                messages.info (request,"Post is saved!")
                return redirect ("fotoblog:home_views")
    else:
        post_form = PostForm ()
            
    context = dict (
        post_form=post_form,
    )
    return render (request, "pages/post-share.html", context)
