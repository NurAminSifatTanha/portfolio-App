from django.db import models


class AboutMyself(models.Model):
    my_name = models.CharField(max_length=30)
    my_profile_pic = models.ImageField(upload_to='profile_pic',blank=False,null=False)
    my_descriptions = models.TextField()

    class Meta:
        verbose_name_plural = 'AboutMyself'

    def __str__(self):
        return self.my_name

class MyProject(models.Model):
    project_name = models.CharField(max_length=255)
    projet_link = models.URLField(max_length=255)
    project_descriptions = models.TextField()

    def __str__(self):
        return self.project_name

class WorkExperience(models.Model):
    experience_name = models.CharField(max_length=255)
    experience_descriptions = models.TextField()

    def __str__(self):
        return self.experience_name

class Skill(models.Model):
    skill_name = models.CharField(max_length=255)
    skill_rate = models.IntegerField()

    def __str__(self):
        return self.skill_name

class Education(models.Model):
    institute_name = models.CharField(max_length=255)
    degree_name = models.CharField(max_length=255)
    session = models.CharField(max_length=150)
    grade = models.CharField(max_length=150)

    def __str__(self):
        return self.institute_name

class Language(models.Model):
    language_name = models.CharField(max_length=150)
    stage = models.CharField(max_length=255)

    def __str__(self):
        return self.language_name

class Interest(models.Model):
    interest_detail = models.TextField()


