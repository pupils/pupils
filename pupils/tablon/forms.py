from django.forms import ModelForm

from tablon.models import Post

class PostHijosForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('hijo', 'published_by')