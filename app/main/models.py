# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class CommunityPost(models.Model):
    id = models.AutoField(db_column='ID',primary_key=True)  # Field name made lowercase.
    acceptedanswerts = models.DateTimeField(db_column='AcceptedAnswerTS', blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=50, blank=True, null=True)  # Field name made lowercase.
    avgvote = models.IntegerField(db_column='AvgVote', blank=True, null=True)  # Field name made lowercase.
    commentsamount = models.IntegerField(db_column='CommentsAmount', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    deleted = models.BooleanField(db_column='Deleted', blank=True, null=True)  # Field name made lowercase.
    favscount = models.IntegerField(db_column='FavsCount', blank=True, null=True)  # Field name made lowercase.
    hascorrectanswer = models.BooleanField(db_column='HasCorrectAnswer', blank=True, null=True)  # Field name made lowercase.
    hash = models.CharField(db_column='Hash', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lang = models.CharField(db_column='Lang', max_length=50, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=250, blank=True, null=True)  # Field name made lowercase.
    nid = models.IntegerField(db_column='Nid')  # Field name made lowercase.
    posttype = models.CharField(db_column='PostType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    published = models.BooleanField(db_column='Published', blank=True, null=True)  # Field name made lowercase.
    publisheddate = models.DateTimeField(db_column='PublishedDate', blank=True, null=True)  # Field name made lowercase.
    subscount = models.IntegerField(db_column='SubsCount', blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='Tags', max_length=350, blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=4096, blank=True, null=True)  # Field name made lowercase.
    translated = models.BooleanField(db_column='Translated', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    views = models.IntegerField(db_column='Views', blank=True, null=True)  # Field name made lowercase.
    votesamount = models.IntegerField(db_column='VotesAmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'community.post'


class CommunityComment(models.Model):
    id1 = models.CharField(db_column='ID1', primary_key=True, max_length=62)  # Field name made lowercase.
    acceptedanswerts = models.DateTimeField(db_column='AcceptedAnswerTS', blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=50, blank=True, null=True)  # Field name made lowercase.
    avgvote = models.IntegerField(db_column='AvgVote', blank=True, null=True)  # Field name made lowercase.
    correct = models.BooleanField(db_column='Correct', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    hash = models.CharField(db_column='Hash', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='Id')  # Field name made lowercase.
    post = models.CharField(db_column='Post', max_length=50, blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='Text', max_length=4096, blank=True, null=True)  # Field name made lowercase.
    texthash = models.CharField(db_column='TextHash', max_length=50, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50)  # Field name made lowercase.
    votesamount = models.IntegerField(db_column='VotesAmount', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'community.comment'
        unique_together = (('type', 'id'),)


class CommunityTag(models.Model):
    id = models.CharField(db_column='ID', max_length=4096)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=4096, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', primary_key=True, max_length=4096)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'community.tag'

class IrisDemo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50 ,blank=True, null=True)  # Field name made lowercase.
    stream = models.BinaryField(db_column='Stream', blank=True, null=True, editable=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'iris.demo'