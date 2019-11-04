from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse, HttpResponseRedirect
from cripto.models import message, UserAccount
from django.contrib.auth import get_user_model, authenticate, login, logout
from cripto.forms import RegistrationForm, LoginForm, SendMessageForm

User = get_user_model()

class MainList(ListView):

	model = message
	template_name = 'index.html'

	def get_context_data(self, *args, **kwargs):
		context = super(MainList, self).get_context_data(*args, **kwargs)
		context['messages'] = self.model.objects.all()
		return context

class MessageView(ListView):

	model = message
	template_name = 'message.html'

	def get_context_data(self, *args, **kwargs):
		user = self.kwargs.get('user')
		context = super(MessageView, self).get_context_data(*args, **kwargs)
		context['messages'] = self.model.objects.all()
		context['current_user'] = UserAccount.objects.get(user=self.request.user)
		return context
		


class MessageDetailView(DetailView):
	model = message
	template_name = "message-detail.html"
	def get_context_data(self, *args, **kwargs):
		context = super(MessageDetailView, self).get_context_data(*args, **kwargs)
		user = self.kwargs.get('user')
		context['messages'] = self.model.objects.all()
		context['message'] = self.get_object()
		#ontext['form'] = CommentForm()
		context['current_user'] = UserAccount.objects.get(user=self.request.user)
		return context


class RegistrationView(View):

	template_name = 'registration.html'

	def get(self, request, *args, **kwargs):

		form = RegistrationForm(request.POST or None)
		context = {
			'form': form
		}
		return render(self.request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		form = RegistrationForm(request.POST or None)
		if form.is_valid():
			new_user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			new_user.set_password(password)
			password_check = form.cleaned_data['password_check']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			new_user.save()
			UserAccount.objects.create(user=User.objects.get(username=new_user.username),
									   first_name=new_user.first_name,
									   last_name = new_user.last_name,
									   email= new_user.email,)
			return HttpResponseRedirect('/')
		context = {
			'form': form
		}
		return render(self.request, self.template_name, context)



class LoginView(View):

	template_name = 'login.html'

	def get(self, request, *args, **kwargs):

		form = LoginForm(request.POST or None)
		context = {
			'form': form
		}
		return render(self.request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		form = LoginForm(request.POST or None)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user:
				login(self.request, user)
				return HttpResponseRedirect('/')
		context = {
			'form': form
		}
		return render(self.request, self.template_name, context)

class UserAccountView(DetailView):

	template_name = 'user_account.html'

	def get(self, request, *args, **kwargs):
		user = self.kwargs.get('user')
		current_user = UserAccount.objects.get(user=User.objects.get(username=user))
		context = {
			'current_user' : current_user
		}
		return render(self.request, self.template_name, context)

"""
class Send_Message(View):

	template_name = 'send_message.html'

	def get(self, request, *args, **kwargs):
		form = SendMessageForm(request.POST or None)
		context = {
			'form': form
		}
		return render(self.request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		form = SendMessageForm(request.POST or None)
		if form.is_valid():
			new_article = form.save(commit=False)
			name = form.cleaned_data['name']
			title = form.cleaned_data['title']
			slug = form.cleaned_data['slug']
			key = form.cleaned_data['key']
			text = form.cleaned_data['text']
			new_article.save()

			arr=['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
			def switch(n):
				while n<33:
					arr.append(arr[0])
					arr.remove(arr[0])
					n+=1
			switch(0)


			m= new_article.text
			k= new_article.key
			k*=len(m)//len(k)+1 
			c=""
			for i,j in enumerate(m): 
				gg=(ord(j)+ord(k[i])) 
				c+=chr(gg%33+65) 

			message.objects.create(	   name = new_article.name,
									   title = new_article.title,
									   slug = new_article.slug,
									   key = new_article.key,
									   text = new_article.text,
									   text2 = c)
			return HttpResponseRedirect('/')
		context = {
			'form': form
		}
		return render(self.request, self.template_name, context)  """
def post_new(request):

    if request.method == "POST":
        form = SendMessageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            arr=['А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
            def switch(n):
            	while n<33:
            		arr.append(arr[0])
            		arr.remove(arr[0])
            		n+=1
            switch(0)
            m= post.text
            k= post.key
            k*=len(m)//len(k)+1 
            c=""
            for i,j in enumerate(m):
            	gg=(ord(j)+ord(k[i]))
            	c+=chr(gg%33+65)
            post.text2 = c             

            post.save()
            return redirect('base_view')
    else:
        form = SendMessageForm()
    return render(request, 'send_message.html', {'form': form})