from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment, Contact
from .forms import CommentForm


class PostList(generic.ListView):
    """
    Postlist class.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    """
    Postdetail class.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Get method.
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Post method.
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

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
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )


class ContactPage(View):
    """
    Contact class.
    """
    def contact_us(self, request, slug, *args, **kwargs):
        """
        Contact.
        """
        if request.method == 'POST':
            contact = Contact()
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            contact.name = name
            contact.email = email
            contact.subject = subject
            contact.message = message
            contact.save()
            return HttpResponseRedirect("<h1>Thanks for contacting us!</h1>")
        return render(request, 'contact_us.html')


class PostLike(View):
    """
    Postlike class.
    """
    def post(self, request, slug):
        """
        Post method.
        """
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def delete_own_comment(request, id=None):
    """
    Delete own comment.
    """
    comment = get_object_or_404(Comment, id=id)
    r = request.user
    if (
        comment.name == r.username and r.is_authenticated
    ):
        comment.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Your comment is deleted',
        )
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        messages.add_message(request, messages.ERROR, 'An error occurred')
