import datetime

from django.db import models
from django.utils import timezone

'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
'''
class Post(models.Model):
    nick = models.CharField(max_length=50)
    post_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    
    def __str__(self):
        return self.post_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
    def likes(self):
        return Like.objects.filter(post_id=self.id).count()
        
    def comments(self):
        return Comment.objects.filter(post_id=self.id).order_by('-pub_date') 
                
    def comments_count(self):
        return Comment.objects.filter(post_id=self.id).count()        

    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    nick = models.CharField(max_length=50, default="admin")
    comment_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    
    def __str__(self):
        return self.comment_text

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class User(models.Model):
    nick = models.CharField(max_length=256)
    pswd = models.CharField(max_length=256)
    icon = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.nick + " " + self.text
    def comments(self):
        return Message.objects.filter(user_id=self.id).order_by('-pub_date')


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nick = models.CharField(max_length=50, default="Adama")
    text = models.CharField(max_length=1000)
    icon = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.comment_text


class Group(models.Model):
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    def users(self):
        users = []
        for i in Group_users.objects.filter(id=self.id):
            users.append(User.objects.filter(id=i.user_id))

        return users

class Group_users(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    group = Group(models.ForeignKey(Group, on_delete=models.PROTECT))