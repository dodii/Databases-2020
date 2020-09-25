from django.shortcuts import render
from django.http import HttpResponse
from prueba.models import Unit
from prueba.models import Player
from prueba.models import Item
from prueba.models import Game
from prueba.models import Equipped
from django.db import connection
from collections import namedtuple
from django.shortcuts import render
from .forms import EloForm
from .forms import PopularItemForm


# Create your views here.
def index(request):
        champ_form = EloForm(prefix="champ_form")
        winrate_form = EloForm(prefix="winrate_form")
        item_form = EloForm(prefix="item_form")
        popular_item_form = PopularItemForm(prefix="popular_item_form")
        return render(request, "index.html", {'champ_form': champ_form, 'winrate_form': winrate_form, 
                        'item_form': item_form, 'popular_item_form': popular_item_form})

def champ_output(request):
        if request.method == 'POST':
                champ_form = EloForm(request.POST, prefix="champ_form")
                if champ_form.is_valid():
                        #aqui van los campeones mas populares con la consulta
                        #adecuada, consultar_champ con el elo del post
                        elo = champ_form.cleaned_data['elo']
                        sql_res = consultar_champs(elo)
                        #entregar un array con el output
                        res =  sql_res
                        return render(request, "champ_output.html", {'res_champs': res})
                else:
                        res = 'No existe ese elo para consultar en la base'
                        return render(request, "champ_output.html", {'res_champs': res})
        else:
                champ_form = EloForm(prefix="champ_form")
                comb_form = EloForm(prefix="comb_form")
                third_form = EloForm(prefix="third_form")
        return render(request, "index.html", {'champ_form': champ_form, 'winrate_form': winrate_form, 
                        'item_form': item_form})

def winrate_output(request):
        if request.method == 'POST':
                winrate_form = EloForm(request.POST, prefix="winrate_form")
                if winrate_form.is_valid():
                        #aqui van los champs con mayor winrate segun la consulta adecuada
                        elo = winrate_form.cleaned_data['elo']
                        sql_res = consultar_winrate(elo)
                        #entregar un array con el output
                        res = sql_res
                        return render(request, "winrate_output.html", {'winrate_res': res})
                else:
                        res = 'Ese elo no existe en la base'
                        return render(request, "winrate_output.html", {'winrate_res': res})
        else:
                champ_form = EloForm(prefix="champ_form")
                winrate_form = EloForm(prefix="winrate_form")
                item_form = EloForm(prefix="item_form")
        return render(request, "index.html", {'champ_form': champ_form, 'winrate_form': winrate_form, 
                'item_form': item_form})

def item_output(request):
        if request.method == 'POST':
                item_form = EloForm(request.POST, prefix="item_form")
                if item_form.is_valid():
                        #aqui van los items mas usados segun la consulta
                        elo = item_form.cleaned_data['elo']
                        sql_res = consultar_items(elo)
                        #entregar array output
                        res = sql_res
                        return render(request, "item_output.html", {'item_res': res})
                else:
                        res = 'Ese elo no existe en la base de datos'
                        return render(request, "item_output.html", {'item_res': res})
        else:
                champ_form = EloForm(prefix="champ_form")
                winrate_form = EloForm(prefix="winrate_form")
                item_form = EloForm(prefix="item_form")
        return render(request, "index.html", {'champ_form': champ_form, 'winrate_form': winrate_form, 
                'item_form': item_form})

def popular_item_output(request):
	if request.method == 'POST':
		popular_item_form = PopularItemForm(request.POST, prefix="popular_item_form")
		if popular_item_form.is_valid():
			item_champ = popular_item_form.cleaned_data['form_champ']
			sql_res = consultar_popular_item(item_champ)
			res = sql_res[0][0]
			return render(request, "popular_item_output.html", {'popular_item_res': res})
		else:
			res = 'Ese champ no existe en la base de datos'
			return render(request, "popular_item_output", {"popular_item_res": res})
	else:
		champ_form = EloForm(prefix="champ_form")
		winrate_form = EloForm(prefix="winrate_form")
		item_form = EloForm(prefix="item_form")
		popular_item_form = PopularItemForm(request.POST, prefix="popular_item_form")
		return render(request, "index.html", {'champ_form': champ_form, 'winrate_form': winrate_form, 
				'item_form': item_form, 'popular_item_form': popular_item_form})

def consultar_champs(elo):
        with connection.cursor() as cursor:
                cursor.execute("SELECT c_name AS champion, COUNT(*) AS cantidad FROM tft.equipped WHERE g_id IN (SELECT gameId FROM tft.game WHERE division = %s) GROUP BY c_name ORDER BY cantidad DESC", [elo])
                results = cursor.fetchall()
        return results

def consultar_winrate(elo):
        with connection.cursor() as cursor:
                cursor.execute("SELECT c_name AS champion, COUNT(*) AS cantidad FROM tft.equipped WHERE g_id IN (SELECT gameId FROM tft.game WHERE division = %s)AND p_position = 1 GROUP BY c_name ORDER BY cantidad DESC", [elo])
                results = cursor.fetchall()
        return results

def consultar_items(elo):
        with connection.cursor() as cursor:
                cursor.execute("SELECT i_id AS itemId, COUNT(*) AS cantidad FROM tft.equipped, tft.game WHERE g_id = gameId AND i_id <> 0 AND division = %s GROUP BY i_id ORDER BY cantidad DESC LIMIT 5", [elo])
                results = cursor.fetchall()
        return results

def consultar_popular_item(form_champ):
	with connection.cursor() as cursor:
		cursor.execute("SELECT i_id FROM PopularItem WHERE c_name = %s LIMIT 1", [form_champ])
		results = cursor.fetchall()
	return results

def namedtuplefetchall(cursor):
        "Return all rows from a cursor as a namedtuple"
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]

