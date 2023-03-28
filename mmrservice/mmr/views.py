from django.shortcuts import render
import requests
from django.http import HttpResponse


# Create your views here.


def calculate_mmr(request):
    if 'summoner_name' in request.GET:
        summoner_name = request.GET.get('summoner_name')
        api_key = 'RGAPI-4d3e2c05-cec0-48a0-9bd7-a2bab72d033e'
        url = f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}'
        response = requests.get(url)
        summoner_data = response.json()
        summoner_id = summoner_data['id']
        url = f'https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}?api_key={api_key}'
        response = requests.get(url)
        league_data = response.json()[1]
        mmr = (league_data['leaguePoints'] - 1000) / 10
        tier = (league_data['tier']) + ' ' + (league_data['rank'])
        points = (league_data['leaguePoints'])
        return HttpResponse(f'{summoner_name} 님의 SOLO RANK 티어는 {tier}' + ' ' +f'{points} 점 입니다.')
    else:
        return render(request, 'index.html')