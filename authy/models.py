from django.db import models
from django.contrib.auth.models import User
from post.models import Post

from django.db.models.signals import post_save

from PIL import Image
from django.conf import settings
import os

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    profile_pic_name = 'user_{0}/profile.jpg'.format(instance.user.id)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
    	os.remove(full_path)

    return profile_pic_name

