from django.db import models

# Create your models here.

###
## ノード(Webリンクやタスクなど)
##

class Node(models.Model):
    data = models.TextField(null=True)
    visible = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.data

###
## ノードとノードの依存関係
##

class Relation(models.Model):
    from_node_id = models.IntegerField(null=True)
    to_node_id = models.IntegerField(null=True)
    importance = models.IntegerField(default=0, null=False)
    interval = models.IntegerField(default=0, null=False)

    class Meta:
        indexes = [
            models.Index(fields=['from_node_id']),
            models.Index(fields=['to_node_id']),
        ]


###
## ノードの類似性
##

class Similarity(models.Model):
    node_id = models.IntegerField(null=True)
    tag_id = models.IntegerField(null=True)
    importance = models.IntegerField(default=0, null=False)
    class Meta:
        indexes = [
            models.Index(fields=['node_id']),
            models.Index(fields=['tag_id']),
        ]

###
## タグ(嗜好性につけるタグ)
##

class Tag(models.Model):
# 18/07/30 変更 START #
    # name = models.CharField(max_length=64, null=True)
    # def __str__(self):
    #     return self.name
    tag_name = models.CharField(max_length=64, null=True)    
    def __str__(self):
        return self.tag_name
# 18/07/30 変更 END #

###
## ユーザー
##

class User(models.Model):
    name = models.CharField(max_length=128, null=True)
    mail = models.CharField(max_length=128, null=True)
    password = models.CharField(max_length=128, null=True)
    salt = models.CharField(max_length=512, null=True)

# 18/07/30 追記 START #
    def __str__(self):
        return self.name
# 18/07/30 追記 END #

###
## ユーザーの嗜好
##

class UserPreference(models.Model):
    user_id = models.IntegerField(null=True)
    level = models.IntegerField(null=False, default=0)
    node_id = models.IntegerField(null=True)
    tag_id = models.IntegerField(null=True)
    class Meta:
        indexes = [
            models.Index(fields=['user_id']),
            models.Index(fields=['node_id']),
            models.Index(fields=['tag_id']),
        ]


