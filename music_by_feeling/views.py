# /music_by_feeling/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Music_by_feeling, Category, Comment, AllMusic, Music, Music_by_feelingList, FavoriteMusicList
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

    url = []

    ##########追加####################################################################
    mbfl = Music_by_feelingList.objects.order_by('id')

    for msc in mbfl:
        url.append('https://open.spotify.com/embed/track/' + msc.track_id + '?utm_source=generator')
    ################################################################################

    url_0 = url[0]
    l = len(url)

    txt = {
        'music_by_feelings' : music_by_feelings,
        'commentsmodel': commentsmodel,
        'form': form,
        'url_0':url_0,
        'url':url,
        'mbfCount':l,
    }

    return render(request, 'music_by_feeling/videoplayback.html',txt)

def playlist(request):

    favoriteMusicList = FavoriteMusicList.objects.order_by('id')
    music_by_feelingList = Music_by_feelingList.objects.order_by('id')

    url = []
    name1 = []
    for msc in music_by_feelingList:
        name1.append( msc.tracks),
        url.append('https://open.spotify.com/embed/track/' + msc.track_id),

    url_0 = url[0]

    if request.method == 'POST':
        url1 = request.POST['url1']
        num = int(url1)

        print("playlist:")
        cnt = 0
        for msc in music_by_feelingList:
            if cnt == num:
                print(num)

                newfmList = FavoriteMusicList.objects.create(
                    tracks = msc.tracks,
                    artist = msc.artist,
                    danceability = msc.danceability,
                    energy = msc.energy,
                    key = msc.key,
                    loudness = msc.loudness,
                    mode = msc.mode,
                    speechiness = msc.speechiness,
                    acousticness = msc.acousticness,
                    instrumentalness = msc.instrumentalness,
                    liveness = msc.liveness,
                    valence = msc.valence,
                    tempo = msc.tempo,
                    type = msc.type,
                    url =msc.url,
                    track_id = msc.track_id,
                    uri = msc.uri,
                    track_href = msc.track_href,
                    analysis_url = msc.analysis_url,
                    duration_ms = msc.duration_ms,
                    time_signature = msc.time_signature,
                    artist_url = msc.artist_url,
                    genres = msc.genres,
                    popularity = msc.popularity,
                    track_url =  msc.track_url,
                    created_year =  msc.created_year,
                    rank =  msc.rank,
                    order =  cnt,
                )
                break
            cnt = cnt + 1

        newfmList.save()

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

    result = '' #'JPOP Hits 2022のplaylist'
    select_year = []
    if request.method == 'POST':
        select_year = request.POST['select_year']

        if select_year[0] == '2022':
            # プレイリストを取得
            result = spotify.user_playlist('Madoka Sota','7GkvWsIFKewgwTDPBZgpt3')#'JPOP Hits 2022のplaylist'
        elif select_year[0] == '2021':
            result = spotify.user_playlist('Madoka Sota','6uszFyxWd5Jt3z0lTZG3AO?si=1c68012b5f094018')#'JPOP Hits 2021のplaylist'
        elif select_year[0] == '2020':
            result = spotify.user_playlist('Madoka Sota','19pd98k52F2lQYnwvyWIRy?si=128dd502b1a14b70')#'JPOP Hits 2020のplaylist'
        else:
            result = spotify.user_playlist('Madoka Sota','7GkvWsIFKewgwTDPBZgpt3')#'JPOP Hits 2022のplaylist'
    else:
        result = spotify.user_playlist('Madoka Sota','6uszFyxWd5Jt3z0lTZG3AO?si=1c68012b5f094018')#'JPOP Hits 2022のplaylist'

    list_data = result['tracks']
    track_num = list_data['total']
    urls_list =[]
    artist_url =[]
    genres =[]
    results =[]
    features = []
    id_list = []
    cnt = 0
    tracks = []
    artist = []
    danceability = []
    energy = []
    key = []
    loudness = []
    mode = []
    speechiness = []
    acousticness = []
    instrumentalness = []
    liveness = []
    valence = []
    tempo = []
    type = []
    url = []
    track_id = []
    uri = []
    track_href = []
    analysis_url = []
    duration_ms = []
    time_signature = []
    popularity = []

    for i in range(len(list_data['items'])):
        track_url = list_data['items'][i]['track']['external_urls']['spotify']
        urls_list.append(track_url)

    for i in range(len(urls_list)):
        track_data = spotify.track(urls_list[i])
        track_feature = spotify.audio_features(urls_list[i])[0]
        artist_url.append(track_data['album']['artists'][0]['external_urls']['spotify']),

        results.append(spotify.artist(artist_url[i])),
        genres.append(results[i]['genres']),
        popularity.append(results[i]['popularity']),
        tracks.append(track_data['name']),
        artist.append(track_data['album']['artists'][0]['name']),
        danceability.append(track_feature['danceability']),
        energy.append(track_feature['energy']),
        key.append(track_feature['key']),
        loudness.append(track_feature['loudness']),
        mode.append(track_feature['mode']),
        speechiness.append(track_feature['speechiness']),
        acousticness.append(track_feature['acousticness']),
        instrumentalness.append(track_feature['instrumentalness']),
        liveness.append(track_feature['liveness']),
        valence.append(track_feature['valence']),
        tempo.append(track_feature['tempo']),
        type.append(track_feature['type']),
        url.append(urls_list[i]),
        track_id.append(track_feature['id']),
        uri.append(track_feature['uri']),
        track_href.append(track_feature['track_href']),
        analysis_url.append(track_feature['analysis_url']),
        duration_ms.append(track_feature['duration_ms']),
        time_signature.append(track_feature['time_signature']),

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

    name = []

#################################################################################

    select_year = []
    if request.method == 'POST':
        select_year = request.POST['select_year']
            # プレイリストを取得
        print('POST')
    else:
        select_year = '2022'
        print('GET')



    count = 0
    Music_by_feelingList.objects.all().delete()
    allMusics = AllMusic.objects.order_by('id')

    for msc in allMusics:
        #select_yearには"2022,"のように最後に","が入っているようなので","を除外する処理追加
        s = select_year[0:len(select_year) - 1]
        if msc.created_year == int(s):
            if(0.5 <= msc.energy <= 0.6 and \
            0.5 <= msc.danceability <= 0.6):

                newmbfList = Music_by_feelingList.objects.create(
                    # ユニークな値
                    tracks = msc.tracks,
                    artist = msc.artist,
                    danceability = msc.danceability,
                    energy = msc.energy,
                    key = msc.key,
                    loudness = msc.loudness,
                    mode = msc.mode,
                    speechiness = msc.speechiness,
                    acousticness = msc.acousticness,
                    instrumentalness = msc.instrumentalness,
                    liveness = msc.liveness,
                    valence = msc.valence,
                    tempo = msc.tempo,
                    type = msc.type,
                    url =msc.url,
                    track_id = msc.track_id,
                    uri = msc.uri,
                    track_href = msc.track_href,
                    analysis_url = msc.analysis_url,
                    duration_ms = msc.duration_ms,
                    time_signature = msc.time_signature,
                    artist_url = msc.artist_url,
                    genres = msc.genres,
                    popularity = msc.popularity,
                    track_url =  msc.track_url,
                    created_year =  msc.created_year,
                    rank =  msc.rank,
                    order =  count,
                )
                newmbfList.save()

                count += 1
                if count == 50:
                   break

    mbfl = Music_by_feelingList.objects.order_by('id')

#################################################################################


    for feature in features:
        if(0.5 <= feature['energy'] <= 0.6 and \
        0.5 <= feature['danceability'] <= 0.6):
           match = spotify.track(feature['id'])

           name.append(match)
           count += 1

    count = 0
    print('処理が終了しました。')

    i = 0

    name0 = name[0]
    name1 = name[1]

    txt2 = {
        'name0':name[0]['name'],
        'name1':name[1]['name'],
        'mbfl':mbfl,
        'select_year':select_year,
        'Track' : tracks,
        'Artist' : artist,
        'danceability' : danceability,
        'energy' : energy,
        'key' : track_feature['key'],
        'loudness' : track_feature['loudness'],
        'mode' : track_feature['mode'],
        'speechiness' : track_feature['speechiness'],
        'acousticness' : track_feature['acousticness'],
        'instrumentalness' : track_feature['instrumentalness'],
        'liveness' : track_feature['liveness'],
        'valence' : track_feature['valence'],
        'tempo' : track_feature['tempo'],
        'type' : track_feature['type'],
        'URL' : url,
        'track_data' : track_data,
        'urls_list' : urls_list,
        'list_data_items' : list_data['items'][0],
        'genres' : genres,
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


"""メンテナンス：音楽データダウンロード"""
def maintenance(request):

    #認証パート
    my_id ='ed4ef8d322064f90b989bedef7c194b4' #client ID
    my_secret = 'dd02269b70424359a84b1ecb14b16df7' #client secret
    ccm = SpotifyClientCredentials(client_id = my_id, client_secret = my_secret)
    spotify = spotipy.Spotify(client_credentials_manager = ccm)

    result = '' #'JPOP Hits 2022のplaylist'
    select_year = []
    if request.method == 'POST':
        select_year = request.POST['select_year']

        if select_year == '2022':
            # プレイリストを取得
            result = spotify.user_playlist('Madoka Sota','7GkvWsIFKewgwTDPBZgpt3')#'JPOP Hits 2022のplaylist'
        elif select_year == '2021':
            result = spotify.user_playlist('Madoka Sota','6uszFyxWd5Jt3z0lTZG3AO?si=1c68012b5f094018')#'JPOP Hits 2021のplaylist'
        elif select_year == '2020':
            result = spotify.user_playlist('Madoka Sota','19pd98k52F2lQYnwvyWIRy?si=128dd502b1a14b70')#'JPOP Hits 2020のplaylist'
        else:
            result = spotify.user_playlist('Madoka Sota','7GkvWsIFKewgwTDPBZgpt3')#'JPOP Hits 2022のplaylist'

        list_data = result['tracks']
        urls_list =[]

        artist_url =[]
        genres =[]
        results =[]

        tracks = []
        artist = []
        danceability = []
        energy = []
        key = []
        loudness = []
        mode = []
        speechiness = []
        acousticness = []
        instrumentalness = []
        liveness = []
        valence = []
        tempo = []
        type = []
        url = []
        track_id = []
        uri = []
        track_href = []
        analysis_url = []
        duration_ms = []
        time_signature = []
        popularity = []

        for i in range(len(list_data['items'])):
            track_url = list_data['items'][i]['track']['external_urls']['spotify']
            urls_list.append(track_url)

        for i in range(len(urls_list)):
            track_data = spotify.track(urls_list[i])
            track_feature = spotify.audio_features(urls_list[i])[0]

            artist_url.append(track_data['album']['artists'][0]['external_urls']['spotify']),
            results.append(spotify.artist(artist_url[i])),

            #追加
            newMusic = AllMusic.objects.create(
             # ユニークな値
              tracks = track_data['name'],
              artist = track_data['album']['artists'][0]['name'],
              danceability = track_feature['danceability'],
              energy = track_feature['energy'],
              key = track_feature['key'],
              loudness = track_feature['loudness'],
              mode = track_feature['mode'],
              speechiness = track_feature['speechiness'],
              acousticness = track_feature['acousticness'],
              instrumentalness = track_feature['instrumentalness'],
              liveness = track_feature['liveness'],
              valence = track_feature['valence'],
              tempo = track_feature['tempo'],
              type = track_feature['type'],
              url = urls_list[i],
              track_id = track_feature['id'],
              uri = track_feature['uri'],
              track_href = track_feature['track_href'],
              analysis_url = track_feature['analysis_url'],
              duration_ms = track_feature['duration_ms'],
              time_signature = track_feature['time_signature'],
              artist_url = track_data['album']['artists'][0]['external_urls']['spotify'],
              genres = results[i]['genres'],
              popularity = results[i]['popularity'],
              track_url = 'https://open.spotify.com/embed/track/' + track_feature['id'],
              created_year = select_year,
              rank = i + 1,
            )
            newMusic.save()

    txt = {

    }


    return render(request, 'music_by_feeling/maintenance.html', txt)
