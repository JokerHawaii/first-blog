from django.test import TestCase
from django.utils import timezone
from posts.models import Post
# Create your tests here.
class PostTest(TestCase):
	def test_create_post(self):
		# Create the post
		post = Post()
		# Set the attributes
		post.title = 'My first post'
		post.content = 'This is my first blog post'
		post.publish = timezone.now()
		# Save it
		post.save()

		# Check we can find it
		all_posts = Post.objects.all()
		self.assertEquals(len(all_posts), 1)
		only_post = all_posts[0]
		self.assertEquals(only_post, post)

		# Check attribute
		self.assertEquals(only_post.title, 'My first post')
		self.assertEquals(only_post.content, 'This is my first blog post')
