from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)

    def __str__(self):
        return f'{self.pk}: {self.title}'


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts")
    group = models.ForeignKey(Group, verbose_name='Группа',
                              on_delete=models.SET_NULL,
                              related_name='group_posts',
                              blank=True, null=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    text = models.TextField()
    created = models.DateTimeField("Дата добавления",
                                   auto_now_add=True, db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="follower")
    following = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name="following")

    def save(self, *args, **kwargs):
        if not Follow.objects.filter(user=self.user,
                                     following=self.following).exists():
            return super(Follow, self).save(*args, **kwargs)
