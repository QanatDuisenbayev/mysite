from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from cripto import views
from cripto.views import (MainList,
						  RegistrationView,
						  LoginView,
						  UserAccountView,
						  MessageView,
						  MessageDetailView,
						  post_new,
						)

urlpatterns = [
	url(r'^$', MainList.as_view(), name = 'base_view'),
	url(r'^registration/$', RegistrationView.as_view(), name='registration'),
	url(r'^login_view/$', LoginView.as_view(), name = 'login_view'),
	url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('base_view')), name='logout_view'),
	url(r'^user_account/(?P<user>[-\w]+)/$', UserAccountView.as_view(), name='account_view'),
	url(r'^message/$', MessageView.as_view(), name='message'),
	url(r'^message-detail/(?P<slug>[-\w]+)/$', MessageDetailView.as_view(), name='message-detail'),
	url(r'^send_message/$', views.post_new, name='send_message'),
]
