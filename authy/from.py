from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from authy.models import Profile

def ForbiddenUsers(value):
	forbidden_users = ['admin', 'css', 'js', 'authenticate', 'login', 'logout', 'administrator', 'root',
	'email', 'user', 'join', 'sql', 'static', 'python', 'delete']
	if value.lower() in forbidden_users:
		raise ValidationError('Invalid name for user, this is a reserverd word.')
def InvalidUser(value):
	if '@' in value or '+' in value or '-' in value:
		raise ValidationError('This is an Invalid user, Do not user these chars: @ , - , + ')
