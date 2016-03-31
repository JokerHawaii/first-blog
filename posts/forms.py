from django import forms

from pagedown.widgets import PagedownWidget

from .models import Post, Comment

class PostForm(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget(show_preview=False))
	publish = forms.DateField(widget=forms.SelectDateWidget)
	class Meta:
		model = Post
		fields = [
			"title",
			"content",
			"image",
			"draft",
			"publish",
		]

class EmailPostForm(forms.Form):
	your_name = forms.CharField(max_length=25)
	your_email = forms.EmailField()
	send_to = forms.EmailField()
	comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')