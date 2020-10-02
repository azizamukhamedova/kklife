from django.db import models

# Create your models here.

class User(models.Model):
    # for names and emails we usually use models.CharField insted of TextField
    # no need to write blank=False, null=False, they are False by default
    # if you want to make some text optional, in this case you can write null=True, blank=True

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    ph_no = models.IntegerField()

    any_message = models.TextField()

    # this is code that shows the name of user in the admin page
    def __str__(self):
        return f"{self.name}"


class Blog(models.Model):
    # author should not be a TextField
    # we usually specify a author of blog by models.ForeignKey

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    published_date = models.DateTimeField(auto_now=True)
    blog_content = models.TextField()

    # this is code that shows the title of blog in the admin page
    def __str__(self):
        return f"{self.title}"

    

