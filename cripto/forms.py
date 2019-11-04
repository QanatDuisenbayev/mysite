from django import forms
from django.contrib.auth import get_user_model
from cripto.models import message
from django.forms import ModelForm

User = get_user_model()

	
class LoginForm(forms.Form):

	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)

	def clean(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']

		if not User.objects.filter(username=username).exists():
			raise forms.ValidationError('login qate!')

		user = User.objects.get(username=username)
		if not user.check_password(password):
			raise forms.ValidationError('password qate!')


class RegistrationForm(forms.ModelForm):
	password_check = forms.CharField(widget=forms.PasswordInput)
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'password_check',
			'first_name',
			'last_name',
			'email',
		]
	def clean(self):
		password = self.cleaned_data['password']
		username = self.cleaned_data['username']
		password_check = self.cleaned_data['password_check']

		if User.objects.filter(username=username).exists():
			raise forms.ValidationError('basqa loging tandanyz')
		if password != password_check:
			raise forms.ValidationError('password saikes emes')


class SendMessageForm(forms.ModelForm):
	class Meta:
		model = message
		fields = [
			'name',
			'title',
			'slug',
			'key',
			'text',
		]
	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()
		if new_slug == 'create':
			raise ValidationError('Slug may not be "Create"')
		return new_slug