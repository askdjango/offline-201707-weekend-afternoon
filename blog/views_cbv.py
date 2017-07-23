from django.views.generic import CreateView, UpdateView
from .models import Post
from .forms import PostForm

post_new = CreateView.as_view(model=Post, form_class=PostForm)

post_edit = UpdateView.as_view(model=Post, form_class=PostForm)

