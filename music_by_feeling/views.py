# /music_by_feeling/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Music_by_feeling, Category, Comment, Music, Music_by_feelingList, FavoriteMusicList
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
    #artist_url = 'https://open.spotify.com/artist/2dIgFjalVxs4ThymZ67YCE?si=uPwGLt18SOOUbTwi4Cvqow'
    album_url =''
    track_url = ''
    output_filename = 'zep_related_artist.csv' #.csv形式で名前を入力


    #max_energy
    #Spotify.target_energy

    #認証パート
    my_id ='ed4ef8d322064f90b989bedef7c194b4' #client ID
    my_secret = 'dd02269b70424359a84b1ecb14b16df7' #client secret
    ccm = SpotifyClientCredentials(client_id = my_id, client_secret = my_secret)
    spotify = spotipy.Spotify(client_credentials_manager = ccm)

    # プレイリストを取得
    result = spotify.user_playlist('Madoka Sota','7GkvWsIFKewgwTDPBZgpt3')#'JPOP Hits 2022のplaylist'
    #print(result)
    features = []
    id_list = []
    cnt = 0

    for track in result['tracks']['items']:
        cnt += 1
        # プレイリスト内の曲のidを抜き出してリスト化
        id = track['track']['id']
        id_list.append(id)

        #print(id_list)
        if cnt == 50:
            features.extend(spotify.audio_features(id_list))
            cnt = 0
            id_list = []

    cnt = 0

    count = 0
    name = []
    for feature in features:
        if(0.5 <= feature['energy'] <= 0.6 and \
        0.5 <= feature['danceability'] <= 0.6):
           match = spotify.track(feature['id'])
           #print(match['name'], "はenergyが0.5〜0.6、danceabilityが0.5〜0.6の曲です。")

           name.append(match)
           count += 1

    count = 0

    #spotify.artist_related_artists(artist_url)
    #result = results['artists']
    url = []


    for i in range(len(name)): #resuktの数をカウントしてfor文を回す
        url.append('https://open.spotify.com/embed/track/'+name[i]['id']+'?utm_source=generator'),
        #('https://open.spotify.com/embed/artist/'+name[i]['id']+'?utm_source=generator'),


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
    #入力パート
    artist_url = 'https://open.spotify.com/artist/2dIgFjalVxs4ThymZ67YCE?si=uPwGLt18SOOUbTwi4Cvqow'
    album_url =''
    track_url = ''

    #認証パート
    my_id ='ed4ef8d322064f90b989bedef7c194b4' #client ID
    my_secret = 'dd02269b70424359a84b1ecb14b16df7' #client secret
    ccm = SpotifyClientCredentials(client_id = my_id, client_secret = my_secret)
    spotify = spotipy.Spotify(client_credentials_manager = ccm)

    results = spotify.artist_related_artists(artist_url)
    result = results['artists']

    name = []
    genres = []
    images = []
    popularity = []
    external_urls = []
    uri = []
    id = []
    url = []

    for i in range(len(result)): #resultの数をカウントしてfor文を回す
        name.append(result[i]['name']),
        genres.append(result[i]['genres']),
        images.append(result[i]['images'][0]['url']),
        popularity.append(result[i]['popularity']),
        external_urls.append(result[i]['external_urls']['spotify']),
        uri.append(result[i]['uri']),
        id.append(result[i]['id']),
        url.append('https://open.spotify.com/embed/artist/'+result[i]['id']+'?utm_source=generator'),

    url_0 = url[0]

    related_df = pd.DataFrame(index=[], columns=['Name', 'Genres', 'Images_url', 'Popularity', 'URL', 'URI', 'ID'])
    for i in range(len(result)): #resultの数をカウントしてfor文を回す
        related_df= related_df.append({
            'Name' : result[i]['name'],
            'Genres' : result[i]['genres'],
            'Images_url' : result[i]['images'][0]['url'],
            'Popularity' : result[i]['popularity'],
            'URL' : result[i]['external_urls']['spotify'],
            'URI' : result[i]['uri'],
            'ID' : result[i]['id']}, ignore_index=True)

    music_by_feelingList = Music_by_feelingList.objects.order_by('id')
    favoriteMusicList = FavoriteMusicList.objects.order_by('id')

    for relatedData in related_df.itertuples():
        music_by_feelingLists = Music_by_feelingList.objects.update_or_create(genres=relatedData.Genres, images=relatedData.Images_url, popularity=relatedData.Popularity, external_urls=relatedData.URL, uri=relatedData.URI, result1=relatedData.ID, defaults={"name": relatedData.Name})

    fmList = FavoriteMusicList.objects.order_by('id')

    if request.method == 'POST':
        url1 = request.POST['url1']
        num = int(url1)

        newfmList = FavoriteMusicList.objects.create(
         # ユニークな値
          name = name[num],
          genres = genres[num],
          images = images[num],
          popularity = popularity[num],
          external_urls = external_urls[num],
          uri = uri[num],
          result1 = num,
        )
        newfmList.save()

        txt = {
            'num':num,
        }

    txt = {
        'fmList':favoriteMusicList,
        'url':url,
        'url_0':url_0,
    }
    return render(request, 'music_by_feeling/playlist.html', txt)

def spotifyLoad(request):
    #入力パート
    #artist_url = 'https://open.spotify.com/artist/2dIgFjalVxs4ThymZ67YCE?si=uPwGLt18SOOUbTwi4Cvqow'
    album_url =''
    track_url = ''
    output_filename = 'zep_related_artist.csv' #.csv形式で名前を入力

    #認証パート
    my_id ='ed4ef8d322064f90b989bedef7c194b4' #client ID
    my_secret = 'dd02269b70424359a84b1ecb14b16df7' #client secret
    ccm = SpotifyClientCredentials(client_id = my_id, client_secret = my_secret)
    spotify = spotipy.Spotify(client_credentials_manager = ccm)

    #results = spotify.artist_related_artists(artist_url)
    #result = results['artists']

    # プレイリストを取得
    result = spotify.user_playlist('Madoka Sota','7GkvWsIFKewgwTDPBZgpt3')#'JPOP Hits 2022のplaylist'
    #print(result)
    features = []
    id_list = []
    cnt = 0

    for track in result['tracks']['items']:
        cnt += 1
        # プレイリスト内の曲のidを抜き出してリスト化
        id = track['track']['id']
        id_list.append(id)

        #print(id_list)
        if cnt == 50:
            features.extend(spotify.audio_features(id_list))
            cnt = 0
            id_list = []

    cnt = 0

    count = 0
    name = []
    for feature in features:
        if(0.5 <= feature['energy'] <= 0.6 and \
        0.5 <= feature['danceability'] <= 0.6):
           match = spotify.track(feature['id'])
           #print(match['name'], "はenergyが0.5〜0.6、danceabilityが0.5〜0.6の曲です。")

           name.append(match)
           count += 1

    count = 0
    print('処理が終了しました。')



    i = 0
    #for i in range(len(match)): #resultの数をカウントしてfor文を回す
        #name.append(match[i]['name']),#(match[i]['name']),

    name0 = name[0]
    name1 = name[1]



    txt2 = {
        'name0':name[0]['name'],
        'name1':name[1]['name'],


    }
    return render(request, 'music_by_feeling/spotifyLoad.html', txt2)


"""ページ３"""
def page3(request):
    if request.method == "POST":
        form_m = MusicForm(request.POST)
        if form_m.is_valid():
            music = form_m.save(commit=False)
            music.save()
            return redirect('music_by_feeling:page3')
    else:
        form_m = MusicForm()

    return render(request, 'music_by_feeling/page3.html', {'forms':form_m})

"""音楽リストを表示"""
def music_render(request):
    context = {
        'music_list': Music.objects.all(),
    }
    return render(request, 'music_by_feeling/page3.html', context)
