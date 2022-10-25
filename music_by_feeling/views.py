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

###################################################
    # プレイリストを取得
#    result = spotify.user_playlist('Madoka Sota','7GkvWsIFKewgwTDPBZgpt3')#'JPOP Hits 2022のplaylist'


    result = '' #'JPOP Hits 2022のplaylist'
    select_year = ''

    select_year = Music.select_year
    if select_year == '2022':
        # プレイリストを取得
        result = spotify.user_playlist('Madoka Sota','7GkvWsIFKewgwTDPBZgpt3')#'JPOP Hits 2022のplaylist'
    elif select_year == '2021':
        result = spotify.user_playlist('Madoka Sota','6uszFyxWd5Jt3z0lTZG3AO?si=1c68012b5f094018')#'JPOP Hits 2021のplaylist'
    elif select_year == '2020':
        result = spotify.user_playlist('Madoka Sota','19pd98k52F2lQYnwvyWIRy?si=128dd502b1a14b70')#'JPOP Hits 2020のplaylist'
    else:
        result = spotify.user_playlist('Madoka Sota','7GkvWsIFKewgwTDPBZgpt3')#'JPOP Hits 2022のplaylist'


    Music.select_year = select_year
#####################################################


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
    #############################################################################
    playlist_url = 'https://open.spotify.com/playlist/54WBnoUJ9oAFo5OCes3SVg?si=a81f6fc93f734a34'
    #list_data = spotify.playlist_tracks(playlist_url)
    list_data = spotify.playlist_tracks(playlist_url)
    track_num = list_data['total']
    urls_list =[]
    track_name =[]
    artist_name =[]
    album_name =[]
    artist_url =[]
    genres =[]
    results =[]

    for i in range(track_num):
        track_url = list_data['items'][i]['track']['external_urls']['spotify']
        urls_list.append(track_url)

    #track_df = pd.DataFrame(index=[],
    #                        columns=['Track', 'Artist', 'danceability', 'energy',
    #                        'key', 'loudness', 'mode', 'speechiness', 'acousticness',
    #                        'instrumentalness', 'liveness', 'valence','tempo', 'type', 'URL'])
    #track_df = track_df.append({
    #    'Track' : track_data['name'],
    #    'Artist' : track_data['album']['artists'][0]['name']}, ignore_index=True)
    for i in range(len(urls_list)):
        track_data = spotify.track(urls_list[i])
        track_feature = spotify.audio_features(urls_list[i])[0]
        track_name.append(track_data['name']),
        artist_name.append(track_data['album']['artists'][0]['name']),
        #album_name.append(track_data['album']['id']),
        #album_name.append(track_data['album']),
        #artist_url.append(track_data['album']['external_urls']['spotify']),
        artist_url.append(track_data['album']['artists'][0]['external_urls']['spotify']),

    #for i in range(len(urls_list)):
        #results = spotify.album(artist_url[i])
        #results = spotify.artist(artist_url[i])
        results.append(spotify.artist(artist_url[i])),
        #result = results['artists'],

    #for i in range(len(results)):
        genres.append(results[i]['genres']),

    #############################################################################

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
    l = len(name)

    txt = {
        'music_by_feelings' : music_by_feelings,
        'commentsmodel': commentsmodel,
        'form': form,
        'url_0':url_0,
        'url':url,
        'mbfCount':l,
        'track_name':track_name,
        'artist_name':artist_name,
        'album_name':album_name,
        'artist_url':artist_url,
        'genres':genres,
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



###################################################
    # プレイリストを取得
#    result = spotify.user_playlist('Madoka Sota','7GkvWsIFKewgwTDPBZgpt3')#'JPOP Hits 2022のplaylist'


    result = '' #'JPOP Hits 2022のplaylist'
    select_year = ''

    select_year = Music.select_year
    if select_year == '2022':
        # プレイリストを取得
        result = spotify.user_playlist('Madoka Sota','7GkvWsIFKewgwTDPBZgpt3')#'JPOP Hits 2022のplaylist'
    elif select_year == '2021':
        result = spotify.user_playlist('Madoka Sota','6uszFyxWd5Jt3z0lTZG3AO?si=1c68012b5f094018')#'JPOP Hits 2021のplaylist'
    elif select_year == '2020':
        result = spotify.user_playlist('Madoka Sota','19pd98k52F2lQYnwvyWIRy?si=128dd502b1a14b70')#'JPOP Hits 2020のplaylist'
    else:
        result = spotify.user_playlist('Madoka Sota','7GkvWsIFKewgwTDPBZgpt3')#'JPOP Hits 2022のplaylist'


    Music.select_year = select_year
#####################################################




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










    name1 = []
    genres = []
    images = []
    popularity = []
    external_urls = []
    uri = []
    id = []
    url = []

    for i in range(len(name)): #resultの数をカウントしてfor文を回す
        name1.append(name[i]['name']),
#        genres.append(name[i]['genres']),
#        images.append(name[i]['images'][0]['url']),
        popularity.append(name[i]['popularity']),
        external_urls.append(name[i]['external_urls']['spotify']),
        uri.append(name[i]['uri']),
        id.append(name[i]['id']),
        url.append('https://open.spotify.com/embed/track/'+name[i]['id']),
#        url.append('https://open.spotify.com/embed/artist/'+name[i]['id']+'?utm_source=generator'),

    url_0 = url[0]

    '''
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
            '''

    music_by_feelingList = Music_by_feelingList.objects.order_by('id')
    favoriteMusicList = FavoriteMusicList.objects.order_by('id')

#    mbf = get_object_or_404(Music_by_feelingList,pk=1)
#    mbf = Music_by_feelingList.objects.get(id=1)
#    mbf1 = Music_by_feelingList.objects.get(name='Shukumei')


#    for relatedData in related_df.itertuples():
#        music_by_feelingLists = Music_by_feelingList.objects.update_or_create(genres=relatedData.Genres, images=relatedData.Images_url, popularity=relatedData.Popularity, external_urls=relatedData.URL, uri=relatedData.URI, result1=relatedData.ID, defaults={"name": relatedData.Name})

#    fmList = FavoriteMusicList.objects.order_by('id')

    if request.method == 'POST':
        url1 = request.POST['url1']
        num = int(url1)

        newfmList = FavoriteMusicList.objects.create(
         # ユニークな値
          name = name1[num],
#          genres = genres[num],
#          images = images[num],
          popularity = popularity[num],
          external_urls = external_urls[num],
          uri = uri[num],
          result1 = url[num],
        )
        newfmList.save()

        txt = {
            'num':num,
        }

    name0 = name1[0]
    name1 = name1[1]
    name2 = name[0]['id']
    name3 = name[0]['name']
#    name4 = mbf1

    txt = {
        'fmList':favoriteMusicList,
        'mbfList':music_by_feelingList,
        'url':url,
        'url_0':url_0,
        'name0':name0,
        'name1':name1,
        'name2':name2,
        'name3':name3,
#        'name4':name4,
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

    #result = spotify.user_playlist('Madoka Sota','7GkvWsIFKewgwTDPBZgpt3')#'JPOP Hits 2022のplaylist'


    result = '' #'JPOP Hits 2022のplaylist'
    select_year = []
    if request.method == 'POST':
        select_year = request.POST['select_year']
        #select_year1 = int(select_year)

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

    Music.select_year = select_year

    #playlist_url = 'https://open.spotify.com/playlist/54WBnoUJ9oAFo5OCes3SVg?si=a81f6fc93f734a34'
    #list_data = spotify.playlist_tracks(playlist_url)
    list_data = result['tracks']
    track_num = list_data['total']
    urls_list =[]
    #track_name =[]
    #artist_name =[]
    #album_name =[]
    artist_url =[]
    genres =[]
    results =[]

    #print(result)
    features = []
    id_list = []
    cnt = 0
    #name = []

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

    for i in range(track_num):
        track_url = list_data['items'][i]['track']['external_urls']['spotify']
        urls_list.append(track_url)

    for i in range(len(urls_list)):
        track_data = spotify.track(urls_list[i])
        track_feature = spotify.audio_features(urls_list[i])[0]
        #track_name.append(track_data['name']),
        #artist_name.append(track_data['album']['artists'][0]['name']),
        artist_url.append(track_data['album']['artists'][0]['external_urls']['spotify']),

        results.append(spotify.artist(artist_url[i])),
        #genres.append(results[i]['genres']),

        #track = track_data['name']
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

        #追加
        newmbfList = Music_by_feelingList.objects.create(
         # ユニークな値
          name = track_data['name'],
    #          genres = nm['genres'],
    #          images = nm['images'],
          popularity = 100,
    #      external_urls = nm['external_urls'],
          uri = urls_list[i],
    #          result1 = nm['url'],
    #      result1 = nm['id'],
        )
        newmbfList.save()


        '''
        track.append(track_data['name']),
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

        if select_year[0] == results[0]['genres']:

            cnt += 1
            # プレイリスト内の曲のidを抜き出してリスト化
            id = result['tracks']['items'][i]['track']['id']
            id_list.append(id)

            #print(id_list)
            if cnt == 50:
                features.extend(spotify.audio_features(id_list))
                cnt = 0
                id_list = []
            for track in result['tracks']['items']:
                cnt += 1
                if cnt == i:
                    # プレイリスト内の曲のidを抜き出してリスト化
                    id = track['track']['id']
                    id_list.append(id)

                    #print(id_list)
                    if cnt == 50:
                        features.extend(spotify.audio_features(id_list))
                        cnt = 0
                        id_list = []
        '''

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

    #追加
    for nm in name:
        newmbfList = Music_by_feelingList.objects.create(
         # ユニークな値
          name = nm['name'],
    #          genres = nm['genres'],
    #          images = nm['images'],
          popularity = nm['popularity'],
          external_urls = nm['external_urls'],
          uri = nm['uri'],
    #          result1 = nm['url'],
          result1 = nm['id'],
        )
        newmbfList.save()


    txt2 = {
        'name0':name[0]['name'],
        'name1':name[1]['name'],

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
        #'list_data' : list_data,
        'list_data_items' : list_data['items'][0]
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
