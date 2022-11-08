# /music_by_feeling/views.py

from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .models import Music_by_feeling, Category, Comment, AllMusic, Music, Music_by_feelingList, FavoriteMusicList, History, Account
from .forms import CommentForm, MusicForm, AccountForm, AddAccountForm
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import csv


import numpy as np
#from scipy.spatial.distance import pdist, squareform



from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

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
                )

                ##追加
                #arr.append([msc.danceability, msc.energy, msc.valence])




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

    select_year = []
    if request.method == 'POST':
        select_year = request.POST['select_year']

        ##追加
        feeling_1 = request.POST['feeling_1']
        feeling_2 = request.POST['feeling_2']
    else:
        select_year = '2022'

    count = 0
    Music_by_feelingList.objects.all().delete() #?
    allMusics = AllMusic.objects.order_by('id')


    ##追加
    ##feeling_1 = ''
    ##feeling_2 = ''
    Music.feeling_1 = feeling_1
    Music.feeling_2 = feeling_2

    arr = []#dancealibity, energy, uri, 指定した感情とのdistanceの4つが入った配列


    for msc in allMusics:
        s = select_year[0:len(select_year) - 1]#select_yearには"2022,"のように最後に","が入っているようなので","を除外する処理追加

        if msc.created_year == int(s):
            arr.append([msc.energy, msc.danceability, msc.uri, 0])#distanceを0と置いて場所を作った


    point = np.array([float(feeling_1),float(feeling_2)])#指定した感情

    for daen_i, daen in enumerate(arr):
        distance = np.linalg.norm(point-(daen[0],daen[1]))#二点間の距離
        arr[daen_i][3] = distance


    arr.sort(key = lambda x:x[3])#4番目の要素(distance)をキーにして小さい順に並べ替え


    for i in range(5):#5回繰り返す
      for msc in allMusics:
        if(arr[i][2] == msc.uri):
            print(msc.energy,'----',msc.valence,'---', msc.danceability)

            newmbfList = Music_by_feelingList.objects.create(
                #ログイン中のユーザ情報の取得
                user=request.user,

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
            )
            newmbfList.save()
            break

    mbfl = Music_by_feelingList.objects.order_by('id')
    txt2 = {
        'mbfl':mbfl,
    }
    return render(request, 'music_by_feeling/spotifyLoad.html', txt2)

"""ページ３"""
'''
def page3(request):
    if request.method == "POST":
        form_m = MusicForm(request.POST)
        if form_m.is_valid():
            music = form_m.save(commit=False)
            #ログイン中のユーザ情報の取得
            music.user=request.user
            music.save()
            return redirect('music_by_feeling:page3')
    else:
        form_m = MusicForm()

    return render(request, 'music_by_feeling/page3.html', {'forms':form_m})
'''
'''
def page3(request):
    if request.method == "POST":
        form_m = MusicForm(request.POST)
        if form_m.is_valid():
            music = form_m.save(commit=False)
            #ログイン中のユーザ情報の取得
            music.user=request.user
            #music_db=Music(**form_m.cleaned_data) #create?
            #music_db.save() #save?
            #music_db=Music.objects.create(**form_m.cleaned_data)
            music.save()
            return redirect('music_by_feeling:page3')
    else:
        form_m = MusicForm()

    return render(request, 'music_by_feeling/page3.html', {'forms':form_m})
'''

"""音楽リストを表示"""
def music_render(request):
    if request.method == "POST":
        form_m = MusicForm(request.POST)
        if form_m.is_valid():
            music = form_m.save(commit=False)
            #ログイン中のユーザ情報の取得
            music.user=request.user
            #music_db=Music(**form_m.cleaned_data) #create?
            #music_db.save() #save?
            music_db=Music.objects.create(**music.cleaned_data)
            music_db.save()
            music.save()
            return redirect('music_by_feeling:page3')
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

class MusicList(ListView):
    model=Music
    context_object_name="music_list"
    template_name="music_list.html"

class HistoryList(ListView):
    model=History
    context_object_name="history_list"
    template_name="History_list.html"

class LikeList(ListView):
    model=FavoriteMusicList
    context_object_name="fm_list"
    template_name="FavoriteMusicList_list.html"


    
#新規登録
class  SignUpView(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    #Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"music_by_feeling/signup.html",context=self.params)

    #Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        #フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
            add_account.user = account

            # モデル保存
            add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

            login(request,account)
            return redirect('login')

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

            return render(request,"music_by_feeling/signup.html",context=self.params)

def login(request):
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
                return HttpResponseRedirect(reverse('home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, "music_by_feeling/login.html")


@login_required
def logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('Login'))
'''
def feeling(request,pk):
    feel=get_object_or_404(spotifyLoad, pk=pk)
    return render(request, 'music_by_feeling/feeling.html', {spotifyLoad: spotifyLoad})
'''
