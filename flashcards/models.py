from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    is_admin = models.BooleanField(default=False)

class FlashcardSet(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Flashcard(models.Model):
    question = models.TextField()
    answer = models.TextField()
    difficulty = models.CharField(
        max_length=50,
        choices=[
            ('easy', 'Easy'),
            ('medium', 'Medium'),
            ('hard', 'Hard'),
        ],
    )
    set = models.ForeignKey(FlashcardSet, on_delete=models.CASCADE, related_name="cards")

class Comment(models.Model):
    comment = models.TextField()
    set = models.ForeignKey(FlashcardSet, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
