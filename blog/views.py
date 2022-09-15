from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Rating
from .forms import CommentForm


class Home(generic.TemplateView):
    template_name = 'index.html'


class Success(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    queryset = queryset = Post.objects.filter(tag=1)
    template_name = 'success.html'
    paginate_by = 6


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    queryset = Post.objects.filter(tag=0)
    template_name = 'blog.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        rating = post.rating.filter(score=0)

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm(),
                "rating": rating,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": CommentForm()
            },
        )
