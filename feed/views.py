from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.shortcuts import render


class HomePage(ListView):
    http_method_names= ["get"]
    model = Post
    template_name = "feed/homepage.html"
    context_object_name = "posts"
    queryset = Post.objects.all().order_by('-id')[0:12]


class PostDetailView(DetailView):
    http_method_names= ["get"]
    model = Post
    template_name = "feed/detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "feed/new-post.html"
    fields = ['text']
    success_url = "/"

    
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.author=self.request.user
        obj.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):

        post = Post.objects.create(
            text=request.POST.get("text"),
            author=request.user,
        )
        return render(
            request,
            "includes/post.html",
            {
                "post": post,
                "show_detail_link": True,
            },
            content_type="application/html"
        )