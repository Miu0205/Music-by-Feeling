# /music_by_feeling/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Music_by_feeling, Category, Comment, Music
from .forms import CommentForm, MusicForm
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import csv

"""一覧表示"""
def index(request):
    music_by_feeling = Music_by_feeling.objects.order_by('title')
    return render(request, 'music_by_feeling/index.html', {'music_by_feeling': music_by_feeling})


"""削除機能"""
def delete(request, id):
    music_by_feeling = get_object_or_404(Music_by_feeling,pk=id)
    music_by_feeling.delete()
    return redirect('music_by_feeling:index')


"""カテゴリ"""
def music_by_feeling_category(request, category):
    category = Category.objects.get(title=category)
    """カテゴリで絞り込む"""
    music_by_feeling = Music_by_feeling.objects.filter(category=category).order_by('title')
    return render(request, 'music_by_feeling/index.html', {'music_by_feeling': music_by_feeling, 'category': category})

"""コメント表示"""
def videoplayback(request):
    music_by_feelings = Music_by_feeling.objects.order_by('title')
    commentsmodel = Comment.objects.order_by('created_date')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('music_by_feeling:videoplayback')
    else:
        form = CommentForm()

    #入力パート
    artist_url = 'https://open.spotify.com/artist/2dIgFjalVxs4ThymZ67YCE?si=uPwGLt18SOOUbTwi4Cvqow'
    album_url =''
    track_url = ''
    output_filename = 'zep_related_artist.csv' #.csv形式で名前を入力

    #認証パート
    my_id ='ed4ef8d322064f90b989bedef7c194b4' #client ID
    my_secret = 'dd02269b70424359a84b1ecb14b16df7' #client secret
    ccm = SpotifyClientCredentials(client_id = my_id, client_secret = my_secret)
    spotify = spotipy.Spotify(client_credentials_manager = ccm)

    results = spotify.artist_related_artists(artist_url)
    result = results['artists']
    url = []

    for i in range(len(result)): #resuktの数をカウントしてfor文を回す
        url.append('https://open.spotify.com/embed/artist/'+result[i]['id']+'?utm_source=generator'),

    url_0 = url[0]

    txt = {
        'music_by_feelings' : music_by_feelings,
        'commentsmodel': commentsmodel,
        'form': form,
        'url_0':url_0,
        'url':url,
    }

    return render(request, 'music_by_feeling/videoplayback.html',txt)

def playlist(request):
    txt = {
    }
    return render(request, 'music_by_feeling/playlist.html', txt)

def spotifyLoad(request):
    #入力パート
    artist_url = 'https://open.spotify.com/artist/2dIgFjalVxs4ThymZ67YCE?si=uPwGLt18SOOUbTwi4Cvqow'
    album_url =''
    track_url = ''
    output_filename = 'zep_related_artist.csv' #.csv形式で名前を入力

    #認証パート
    my_id ='ed4ef8d322064f90b989bedef7c194b4' #client ID
    my_secret = 'dd02269b70424359a84b1ecb14b16df7' #client secret
    ccm = SpotifyClientCredentials(client_id = my_id, client_secret = my_secret)
    spotify = spotipy.Spotify(client_credentials_manager = ccm)

    results = spotify.artist_related_artists(artist_url)
    result = results['artists']

    name = []

    for i in range(len(result)): #resultの数をカウントしてfor文を回す
        name.append(result[i]['name']),

    name0 = name[0]
    name1 = name[1]
    name2 = name[2]
    name3 = name[3]
    name4 = name[4]
    name5 = name[5]
    name6 = name[6]
    name7 = name[7]
    name8 = name[8]
    name9 = name[9]
    name10 = name[10]
    name11 = name[11]
    name12 = name[12]
    name13 = name[13]
    name14 = name[14]
    name15 = name[15]
    name16 = name[16]
    name17 = name[17]
    name18 = name[18]
    name19 = name[19]

    txt2 = {
        'name0':name[0],
        'name1':name[1],
        'name2':name[2],
        'name3':name[3],
        'name4':name[4],
        'name5':name[5],
        'name6':name[6],
        'name7':name[7],
        'name8':name[8],
        'name9':name[9],
        'name10':name[10],
        'name11':name[11],
        'name12':name[12],
        'name13':name[13],
        'name14':name[14],
        'name15':name[15],
        'name16':name[16],
        'name17':name[17],
        'name18':name[18],
        'name19':name[19],
    }
    return render(request, 'music_by_feeling/spotifyLoad.html', txt2)






"""ページ３"""
def page3(request):
    if request.method == "POST":
        form_m = MusicForm(request.POST)
        if form_c.is_valid():
            music = form_c.save(commit=False)
            music.save()
            return redirect('music_by_feeling:page3')
    else:
        form_m = MusicForm()

    return render(request, 'music_by_feeling/page3.html', {'forms':form_m})
