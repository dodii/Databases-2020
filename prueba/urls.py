from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('champ_output.html', views.champ_output, name='champ_output'),
	path('winrate_output.html', views.winrate_output, name='winrate_output'),
	path('item_output.html', views.item_output, name='item_output'),
	path('popular_item_output.html', views.popular_item_output, name='popular_item_output'),
]

