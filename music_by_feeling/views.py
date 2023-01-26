# /music_by_feeling/views.py

from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Music_by_feeling, Category, Comment, AllMusic, Music, Music_by_feelingList, Music_by_feeling_History, Music_by_feeling_Selection_History, FavoriteMusicList, History, Account
from .forms import CommentForm, MusicForm, AccountForm, AddAccountForm
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import csv

from django.utils import timezone
import numpy as np
#from scipy.spatial.distance import pdist, squareform



from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

from tkinter import messagebox
import tkinter as tk

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
def videoplayback(request, id):
    music_by_feelings = Music_by_feeling.objects.order_by('title')
    commentsmodel = Comment.objects.order_by('created_date')
    
    music_by_feelingList = Music_by_feelingList.objects.order_by('id') 
    
    print("request.method=",request.method)
    print("request.POST=",request.POST)
#    print("select_music_button=",select_music_button)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('music_by_feeling:videoplayback')

        #再生用選択曲をHistoryへ追加
#        if 'select_music_button' in request.POST.keys() == True:
        select_music_button = request.POST['select_music_button']
        print("select_music_button=",select_music_button)

        num = int(select_music_button)
        for msc in music_by_feelingList:
            if msc.display_order == num:

                newHistory = History.objects.create(
                    #ログイン中のユーザ情報の取得
                    user=request.user,

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
                    order =  msc.order,
                    display_order =  msc.display_order,
                    dance_up =  msc.dance_up,
                    dance_down =  msc.dance_down,
                    energy_up =  msc.energy_up,
                    energy_down =  msc.energy_down,
                    image_url = msc.image_url,
                )

                break

        newHistory.save()

        # if form.is_valid():
        #     comment = form.save(commit=False)
        #     comment.save()
        #     return redirect('music_by_feeling:videoplayback')
    else:
        form = CommentForm()

    url = []

    ##########追加####################################################################
    mbfl = Music_by_feelingList.objects.order_by('id')

    for msc in mbfl:
        url.append('https://open.spotify.com/embed/track/' + msc.track_id + '?utm_source=generator')

    #################################################################################
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

def playlist(request, id):

    favoriteMusicList = FavoriteMusicList.objects.filter(user=request.user).order_by('id','user')
    music_by_feelingList = Music_by_feelingList.objects.order_by('id','user')

    url = []
    name1 = []

    for mbl in music_by_feelingList:
        name1.append( mbl.tracks),
        url.append('https://open.spotify.com/embed/track/' + mbl.track_id),

    # if favoriteMusicList.first() is None:
    #     return render(request, 'music_by_feeling/playlist_null.html')


    url_0 = url[0]

    if request.method == 'POST':
        url1 = request.POST['url1']
        num = int(url1)
        cnt = 0
        for msc in music_by_feelingList:
            if cnt == num:

                newfmList = FavoriteMusicList.objects.create(
                    #ログイン中のユーザ情報の取得
                    user=request.user,

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
                    display_order =  cnt + 1,
                    dance_up =  msc.dance_up,
                    dance_down =  msc.dance_down,
                    energy_up =  msc.energy_up,
                    energy_down =  msc.energy_down,
                    image_url = msc.image_url,
                )

                break
            cnt = cnt + 1

        newfmList.save()

    if favoriteMusicList.first() is None:
        return render(request, 'music_by_feeling/playlist_null.html')

    txt = {
        'fmList':favoriteMusicList,
        'url':url,
        'url_0':url_0,
    }
    return render(request, 'music_by_feeling/playlist.html', txt)

def playlistNull(request, id):
    return render(request, 'music_by_feeling/playlist_null.html')

def spotifyLoad(request, id): 

    select_year = ''
    if request.method == 'POST':
        selects = request.POST['select_list']
        select_list = selects.split(',')
        
        #何をしているのか
        select_year = select_list[0]
        select_genre = select_list[1]
        select_name = select_list[2]
        select_scales = select_list[3]
        
        ##追加
        feeling_1 = request.POST['feeling_1']
        feeling_2 = request.POST['feeling_2']
        
    else:
        select_year = '2022'
        feeling_1 = request.POST['feeling_1']
        feeling_2 = request.POST['feeling_2']

    count = 0
    Music_by_feelingList.objects.all().delete()
    allMusics = AllMusic.objects.order_by('id')

    #select_yearが選択なしの時はselect_year=0とする（select_yearは整数のため）
    if select_year == "":
        select_year = 0

    ##追加
    ##feeling_1 = ''
    ##feeling_2 = ''

    date_f = timezone.now()
    music_feeling = Music.objects.create(
       user=request.user,
       feeling_1 = feeling_1,
       feeling_2 = feeling_2,
       artist = select_name,
       era = select_year,
       genre = select_genre,
       famous = bool(select_scales),
       #genre = request.POST['genre'],
       #era =select_year[0:len(select_year) - 1],
       date = date_f,
    )
    music_feeling.save()


    arr = []#dancealibity, energy, uri, 指定した感情とのdistanceの4つが入った配列

    for msc in allMusics:
        flg = 0
        if select_year == 0:
            flg = 1
        else:
            if msc.created_year == int(select_year):
                flg = 1

        if flg == 1:
            flg1 = 0
            if select_genre == "":
                flg1 = 1
            else:
                genres_wk = msc.genres.strip()
                genres_wk = genres_wk.replace('[', '')
                genres_wk = genres_wk.replace(']', '')
                genres_wk = genres_wk.replace("'", '')
                genres_list = genres_wk.split(',')
                genres_list = [s.strip() for s in genres_list]

                for gnr in genres_list:
                    if gnr == select_genre:
                        flg1 = 1
            if flg1 == 1:

                flg2 = 0
                if select_name != "":
                    if msc.artist == select_name:
                        flg2 = 1
                else:
                    flg2 = 1

                if flg2 == 1:
                    #元のままのenergy,danceabilityに、評価されたup,down分を反映して調整したenergy,danceabilityを作成
                    adjustEnergy = msc.energy + (msc.energy_up - msc.energy_down) * 0.05
                    adjustDanceability = msc.danceability + (msc.dance_up - msc.dance_down) * 0.05
                    if select_scales == "true":
                        if msc.popularity >= 60:
#                            arr.append([msc.energy, msc.danceability, msc.uri, 0])
                            flg3 = 0
                            for arr_m in arr:
#                                print("msc.uri=",msc.uri,"arr_m[2]=",arr_m[2])
                                if msc.uri == arr_m[2]:
#                                    print("#########msc.uri= ",msc.tracks," ",msc.uri," ","##########arr_m[2]=",arr_m[2])
                                    flg3 = 1
                                    break
                            if flg3 == 0:
#                                print("#########msc.uri= ",msc.tracks," ",msc.uri," ","##########arr_m[2]=",arr_m[2])
                                arr.append([adjustEnergy, adjustDanceability, msc.uri, 0])#distanceを0と置いて場所を作った
                    else:
#                        arr.append([msc.energy, msc.danceability, msc.uri, 0])
                        flg3 = 0
                        for arr_m in arr:
                            if msc.uri == arr_m[2]:
#                                print("#########msc.uri=",msc.tracks," ",msc.uri," ","##########arr_m[2]=",arr_m[2])
                                flg3 = 1
                                break
                        if flg3 == 0:
#                            print("#########msc.uri= ",msc.tracks," ",msc.uri," ","##########arr_m[2]=",arr_m[2])
                            arr.append([adjustEnergy, adjustDanceability, msc.uri, 0])#distanceを0と置いて場所を作った

    point = np.array([float(feeling_1),float(feeling_2)])#指定した感情

    for daen_i, daen in enumerate(arr):
        distance = np.linalg.norm(point-(daen[0],daen[1]))#二点間の距離
        arr[daen_i][3] = distance

    arr.sort(key = lambda x:x[3])#4番目の要素(distance)をキーにして小さい順に並べ替え

    #########################################
    cnt = 10             #繰り返し回数10回
    print(101)
    if len(arr) >= 1:  #選曲した曲数が1以上の場合は実施（0の場合は何もせずメッセージ表示）
        print(102)
        if len(arr) < cnt:  #選曲した曲数が5回より少なければ曲数分のみ繰り返し
            cnt = len(arr)

        #for i in range(5):#5回繰り返す
        for i in range(cnt):#繰り返す（5回または選曲数分）
          for msc in allMusics:
            if(arr[i][2] == msc.uri):

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
                    display_order =  count + 1,
                    dance_up =  msc.dance_up,
                    dance_down =  msc.dance_down,
                    energy_up =  msc.energy_up,
                    energy_down =  msc.energy_down,
                    image_url = msc.image_url,
#                    image_url = 'https://open.spotify.com/embed/track/' + msc.track_id + '?utm_source=generator',
                )
                newmbfList.save()
                newmbfh = Music_by_feeling_History.objects.create(
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
                    display_order =  count + 1,
                    dance_up =  msc.dance_up,
                    dance_down =  msc.dance_down,
                    energy_up =  msc.energy_up,
                    energy_down =  msc.energy_down,
                    image_url = msc.image_url,
#                    image_url = 'https://open.spotify.com/embed/track/' + msc.track_id + '?utm_source=generator',
                )
                newmbfh.save()
                count += 1
                break
    else:                                   #選択した曲数が0の時メッセージのみ表示
        root = tk.Tk()
        root.attributes('-topmost', True)
        root.withdraw()
        root.lift()
        root.focus_force()
        messagebox.showinfo('メッセージ','選択した内容にあう曲が見つかりませんでした。再度入力し直してください。')
        root.destroy()

    newmbfsh = Music_by_feeling_Selection_History.objects.create(
        # ユニークな値
        danceability = float(feeling_1),
        energy = float(feeling_2),
        artist = select_name,
        period = select_year,
        genres = select_genre,
        popularity = bool(select_scales),
    )
    newmbfsh.save()

    output_filename = 'track_data.csv' #.csv形式で名前を入力

    allMusics = Music_by_feelingList.objects.order_by('id')

    track_df = pd.DataFrame(index=[],
                            columns=['tracks', 'artist', 'danceability', 'energy',
                            'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                            'instrumentalness', 'liveness', 'valence','tempo', 'type',
                            'url', 'track_id', 'uri', 'track_href', 'analysis_url',
                            'duration_ms', 'time_signature', 'artist_url', 'genres',
                            'popularity', 'track_url', 'created_year', 'rank'])

    for msc in allMusics:
        #time.sleep(1) #1sec stop
        track_df = track_df.append({

            'tracks' : msc.tracks,
            'artist' : msc.artist,
            'danceability' : msc.danceability,
            'energy' : msc.energy,
            'key' : msc.key,
            'loudness' : msc.loudness,
            'mode' : msc.mode,
            'speechiness' : msc.speechiness,
            'acousticness' : msc.acousticness,
            'instrumentalness' : msc.instrumentalness,
            'liveness' : msc.liveness,
            'valence' : msc.valence,
            'tempo' : msc.tempo,
            'type' : msc.type,
            'url' : msc.url,
            'track_id' : msc.track_id,
            'uri' : msc.uri,
            'track_href' : msc.track_href,
            'analysis_url' : msc.analysis_url,
            'duration_ms' : msc.duration_ms,
            'time_signature' : msc.time_signature,
            'artist_url' : msc.artist_url,
            'genres' : msc.genres,
            'popularity' : msc.popularity,
            'track_url' : msc.track_url,
            'created_year' : msc.created_year,
            'rank' : msc.rank}, ignore_index=True)

    track_df.to_csv(output_filename, encoding='utf-8') #csvファイル出力
    with open(output_filename, 'a', newline='') as f:
        writer = csv.writer(f)

    mbfl = Music_by_feelingList.objects.order_by('id')
    txt2 = {
        'mbfl':mbfl,
    }
    return render(request, 'music_by_feeling/spotifyLoad.html', txt2)

def feedback(request, id):

    allMusics = AllMusic.objects.order_by('id')
    favoriteMusicList = FavoriteMusicList.objects.order_by('id')
    music_by_feelingList = Music_by_feelingList.objects.order_by('id')
    music_by_feeling_History = Music_by_feeling_History.objects.order_by('id')
    history = History.objects.order_by('id')

    if request.method == 'POST':
#        url2 = request.POST['url2']
#        num = int(url2)
        cnt = 0
        selects = request.POST['select_feedback2']
        select_feedback = selects.split(',')

        print(1000)
        print(selects)
        print(select_feedback[0])
        print(select_feedback[1])
        print(select_feedback[2])
        print(select_feedback[3])
        print(select_feedback[4])
        print(select_feedback[5])
        print(select_feedback[6])
        print(select_feedback[7])
        print(select_feedback[8])
        print(1001)

        #0-3:システムの評価、4-7:曲の評価、8:music_by_feelingList内での今回聞いた曲順
        select_feedback_1 = select_feedback[0]
        select_feedback_2 = select_feedback[1]
        select_feedback_3 = select_feedback[2]
        select_feedback_4 = select_feedback[3]
        select_feedback_5 = select_feedback[4]
        select_feedback_6 = select_feedback[5]
        select_feedback_7 = select_feedback[6]
        select_feedback_8 = select_feedback[7]
        select_feedback_9 = int(select_feedback[8])
        print(select_feedback[0])
        print(select_feedback[1])
        print(select_feedback[2])
        print(select_feedback[3])
        print(select_feedback[4])
        print(select_feedback[5])
        print(select_feedback[6])
        print(select_feedback[7])
        print(select_feedback_9)
        print(10)
        #music_by_feelingListに選曲された曲の何番目かをチェック、一致した曲の要素変更
        for msc in music_by_feelingList:
            if cnt == select_feedback_9:
                if select_feedback_5 == "true":
                    msc.dance_down += 1
                    print(11)
                elif select_feedback_6 == "true":
                    msc.dance_up += 1
                    print(12)
                if select_feedback_7 == "true":
                    msc.energy_down += 1
                    print(13)
                elif select_feedback_8 == "true":
                    msc.energy_up += 1
                    print(14)
                msc.save()
                break
            cnt += 1
        #music_by_feelingList側で一致した曲とアーティスト名、曲名が一致した曲は同じ曲と判断
        for msc2 in allMusics:
            #print(999)
            if msc2.artist == msc.artist:
                if msc2.tracks == msc.tracks:
                    #print(msc2.danceability)
                    #print(msc2.energy)
                    #print(msc2.tracks)

                    if select_feedback_5 == "true":
                        msc2.dance_down += 1
                    elif select_feedback_6 == "true":
                        msc2.dance_up += 1
                    if select_feedback_7 == "true":
                        msc2.energy_down += 1
                    elif select_feedback_8 == "true":
                        msc2.energy_up += 1
                    msc2.save()
        #music_by_feelingList側で一致した曲とアーティスト名、曲名が一致した曲は同じ曲と判断
        for msc3 in favoriteMusicList:
            #print(999)
            if msc3.artist == msc.artist:
                if msc3.tracks == msc.tracks:
                    print(msc3.danceability)
                    print(msc3.energy)
                    print(msc3.tracks)

                    if select_feedback_5 == "true":
                        msc3.dance_down += 1
                    elif select_feedback_6 == "true":
                        msc3.dance_up += 1
                    if select_feedback_7 == "true":
                        msc3.energy_down += 1
                    elif select_feedback_8 == "true":
                        msc3.energy_up += 1
                    msc3.save()
        #music_by_feelingList側で一致した曲とアーティスト名、曲名が一致した曲は同じ曲と判断
        for msc4 in music_by_feeling_History:
            if msc4.artist == msc.artist:
                if msc4.tracks == msc.tracks:
                    #print(msc4.danceability)
                    #print(msc4.energy)
                    #print(msc4.tracks)

                    if select_feedback_5 == "true":
                        msc4.dance_down += 1
                    elif select_feedback_6 == "true":
                        msc4.dance_up += 1
                    if select_feedback_7 == "true":
                        msc4.energy_down += 1
                    elif select_feedback_8 == "true":
                        msc4.energy_up += 1
                    msc4.save()
        #music_by_feelingList側で一致した曲とアーティスト名、曲名が一致した曲は同じ曲と判断
        for msc5 in history:
            if msc5.artist == msc.artist:
                if msc5.tracks == msc.tracks:
                    print(msc5.danceability)
                    print(msc5.energy)
                    print(msc5.tracks)

                    if select_feedback_5 == "true":
                        msc5.dance_down += 1
                    elif select_feedback_6 == "true":
                        msc5.dance_up += 1
                    if select_feedback_7 == "true":
                        msc5.energy_down += 1
                    elif select_feedback_8 == "true":
                        msc5.energy_up += 1
                    msc5.save()


    txt = {
        #'fmList':favoriteMusicList,
        #'url':url,
        #'url_0':url_0,
    }
    return render(request, 'music_by_feeling/feedback.html', txt)

"""音楽リストを表示"""
#↓ログインしないとこのページに移れない。
#ログイン画面に遷移する。
@login_required(login_url="/login/")
def music_render(request, id):
    if request.method == "POST":
        form_m = MusicForm(request.POST)
        if form_m.is_valid():
            music = form_m.save(commit=False)
            #ログイン中のユーザ情報の取得
            music.user=request.user
            music_db=Music.objects.create(**music.cleaned_data)
            music_db.save()
            music.save()
            return redirect('music_by_feeling:page3') #1/25
    else:
        form_m = MusicForm()

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

        elif select_year == '2010':
            result = spotify.user_playlist('Madoka Sota','5GPeulW5qPJ48iXHGWiVyM')#2010年代ヒットリスト
        elif select_year == '11111':
            result = spotify.user_playlist('Madoka Sota','4pXAr4qIBBEgMOQ95myqwc')#kpop 人気曲　１００曲
        elif select_year == '1990':
            result = spotify.user_playlist('Madoka Sota', '7IGNg8tfbTYKZYkz4ti0sB?utm_source=generator')#JPOP 90年代
        elif select_year == '2000':
            result = spotify.user_playlist('Madoka Sota', '4zgLoxulQZBRCsFwUCnyhe?utm_source=generator')#JPOP 2000年代
        elif select_year == '10000':
            result = spotify.user_playlist('Madoka Sota', '37i9dQZF1DWT8aqnwgRt92?utm_source=generator')#アニメ 75曲

        else:
            result = spotify.user_playlist('Madoka Sota','7GkvWsIFKewgwTDPBZgpt3')#'JPOP Hits 2022のplaylist'
            AllMusic.objects.order_by('url').distinct().values_list('url')#重複をクリアする操作

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
            #track_url_1 = 'https://open.spotify.com/embed/track/' + track_feature['id']
            #results1 = spotify.track(track_url_1)

            #追加
            try:
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
                  image_url = results[i]['images'][0]['url'],
                )
                newMusic.save()
            except:
                pass


    txt = {
    }

    return render(request, 'music_by_feeling/maintenance.html', txt)

def HistoryList(request,id):

    #favoriteMusicList = FavoriteMusicList.objects.order_by('id')
    HistoryList=History.objects.filter(user=request.user).order_by('id','user')

    url = []
    name1 = []

    for hl in HistoryList:
        name1.append( hl.tracks),
        url.append('https://open.spotify.com/embed/track/' + hl.track_id),

    if not url:
        return render(request, 'music_by_feeling/History_null.html')
    url_0 = url[0]



    if request.method == 'POST':
        url1 = request.POST['url1']
        num = int(url1)
        cnt = 0
        for hl in HistoryList:
            if cnt == num:

                newhlList = HistoryList.objects.create(
                    #ログイン中のユーザ情報の取得
                    user=request.user,

                    tracks = hl.tracks,
                    artist = hl.artist,
                    danceability = hl.danceability,
                    energy = hl.energy,
                    key = hl.key,
                    loudness = hl.loudness,
                    mode = hl.mode,
                    speechiness = hl.speechiness,
                    acousticness = hl.acousticness,
                    instrumentalness = hl.instrumentalness,
                    liveness = hl.liveness,
                    valence = hl.valence,
                    tempo = hl.tempo,
                    type = hl.type,
                    url = hl.url,
                    track_id = hl.track_id,
                    uri = hl.uri,
                    track_href = hl.track_href,
                    analysis_url = hl.analysis_url,
                    duration_ms = hl.duration_ms,
                    time_signature = hl.time_signature,
                    artist_url = hl.artist_url,
                    genres = hl.genres,
                    popularity = hl.popularity,
                    track_url =  hl.track_url,
                    created_year =  hl.created_year,
                    rank =  hl.rank,
                    order =  cnt,
                    display_order =  cnt + 1,
                )

                ##追加
                #arr.append([msc.danceability, msc.energy, msc.valence])




                break
            cnt = cnt + 1

        newhlList.save()

    txt = {
        'hlList':HistoryList,
        'url':url,
        'url_0':url_0,
    }
    return render(request, 'music_by_feeling/History_list.html', txt)

def historyNull(request, id):
    return render(request, 'music_by_feeling/History_null.html')


def graph(request):
    #入力パート
    output_filename = 'zep_related_track.csv' #.csv形式で名前を入力

    allMusics = AllMusic.objects.order_by('id')

    track_df = pd.DataFrame(index=[],
                            columns=['tracks', 'artist', 'danceability', 'energy',
                            'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                            'instrumentalness', 'liveness', 'valence','tempo', 'type',
                            'url', 'track_id', 'uri', 'track_href', 'analysis_url',
                            'duration_ms', 'time_signature', 'artist_url', 'genres',
                            'popularity', 'track_url', 'created_year', 'rank'])

    for msc in allMusics:
        #time.sleep(1) #1sec stop
        track_df = track_df.append({

            'tracks' : msc.tracks,
            'artist' : msc.artist,
            'danceability' : msc.danceability,
            'energy' : msc.energy,
            'key' : msc.key,
            'loudness' : msc.loudness,
            'mode' : msc.mode,
            'speechiness' : msc.speechiness,
            'acousticness' : msc.acousticness,
            'instrumentalness' : msc.instrumentalness,
            'liveness' : msc.liveness,
            'valence' : msc.valence,
            'tempo' : msc.tempo,
            'type' : msc.type,
            'url' : msc.url,
            'track_id' : msc.track_id,
            'uri' : msc.uri,
            'track_href' : msc.track_href,
            'analysis_url' : msc.analysis_url,
            'duration_ms' : msc.duration_ms,
            'time_signature' : msc.time_signature,
            'artist_url' : msc.artist_url,
            'genres' : msc.genres,
            'popularity' : msc.popularity,
            'track_url' : msc.track_url,
            'created_year' : msc.created_year,
            'rank' : msc.rank}, ignore_index=True)

    track_df.to_csv(output_filename, encoding='utf-8') #csvファイル出力
    with open(output_filename, 'a', newline='') as f:
        writer = csv.writer(f)

    txt = {

    }

    return render(request, 'music_by_feeling/maintenance.html', txt)

class MusicList(ListView):
    context_object_name="music_list"
    template_name="music_list.html"
#    template_name="music_list.html"
    model=Music
#    model=Music_by_feeling_Selection_History
    '''
    #アンケート用にカット。アンケート後に変える。
    def get_queryset(self):
        return Music.objects.filter(user=self.request.user.id)
    '''

#新規登録
def Signup(request):
    params = {
        "AccountCreate":False,
        "account_form":AccountForm(),
        "add_account_form":AddAccountForm(),
    }

    if request.method == 'POST':
        params["account_form"] = AccountForm(request.POST)
        params["add_account_form"] = AddAccountForm(request.POST)

        if params["account_form"].is_valid() and params["add_account_form"].is_valid():
            account = params["account_form"].save()
            account.set_password(account.password)
            account.save()

            add_account = params["add_account_form"].save(commit=False)
            add_account.user = account

            add_account.save()

            params["AccountCreate"] = True
        else:
            print(params["account_form"].errors)
            return render(request, 'music_by_feeling/signup.html', context=params)

    return render(request, 'music_by_feeling/signup.html', context=params)

def Login(request):
    if request.method == "POST":
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return render(request, 'music_by_feeling/index.html')
            else:
                # アカウント利用不可
                context = {
                    'etext':"アカウントが有効ではありません",
                }
                return render(request, 'music_by_feeling/e-text-login.html', context)
        # ユーザー認証失敗
        else:
            context = {
                    'etext':"ログインIDまたはパスワードが間違っています",
                }
            return render(request, 'music_by_feeling/e-text-login.html', context)
    # GET
    else:
        return render(request, "music_by_feeling/login.html")


@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return render(request, 'music_by_feeling/login.html')
