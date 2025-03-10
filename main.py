# -*- coding: utf-8 -*-
import os
from google.auth.transport.requests import Request
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError


SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

json_pass="./jsons/token.json"
client_secrets_file = "./jsons/client.json"


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    # Get credentials and create an API client
  
    creds = None#認証情報を格納する変数

    if os.path.exists(json_pass):
        creds = Credentials.from_authorized_user_file(json_pass, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # flow = InstalledAppFlow.from_client_secrets_file("./jsons/client.json", SCOPES)
            # creds = flow.run_local_server(port=0)
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        print("\n",creds,"\n")
        with open(json_pass, "w") as token:
            token.write(creds.to_json())
    
    youtube = googleapiclient.discovery.build("youtube","v3", credentials=creds)
    
    # playlist id取得
    # try:
    #     request = youtube.playlists().list(
    #         part="snippet,contentDetails",
    #         # maxResults=25,
    #         mine=True  # 認証されたアカウントのプレイリストを取得
    #     )
    #     response = request.execute()

    #     # 結果を表示
    #     for playlist in response.get("items", []):
    #         print(f"🎵 {playlist['snippet']['title']} (ID: {playlist['id']})")
    
    
    
    
    #プレイリストidから中の情報取得
    urls=[]
    try:
        # 指定されたプレイリストの動画を取得
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            maxResults=25,  # 取得する最大件数（最大50）
            playlistId="PL8G4Ylahsmrrf6_uMWaQGNUBOf8COtlK5"  # 取得したいプレイリストのID
        )
        response = request.execute()

        # 結果を表示
        # print(f"🎵 プレイリスト内の動画一覧（ID: PL8G4Ylahsmrrf6_uMWaQGNUBOf8COtlK5）:")
        for item in response.get("items", []):
            # print(item)
            # video_title = item["snippet"]["title"]
            video_id = item["contentDetails"]["videoId"]
            # print(f"URL is (https://www.youtube.com/watch?v={video_id})")
            urls.append(f"https://www.youtube.com/watch?v={video_id}")

        print(urls)
    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred: {e.content}")



#動画を再生するための関数．windowで開く．
# import time
# import webbrowser

# def player(movie_url):
#     # time.sleep(5)
#     #&t=0は初めから再生するため
#     url = movie_url+"&t=0"  # 完全なURLを指定
#     browser_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
#     webbrowser.register('brave', None, webbrowser.BackgroundBrowser(browser_path))  # Braveを登録
#     browser = webbrowser.get('brave')  # Braveを取得
#     browser.open(url)  # URLを開く
#     print(1)
#     return 0


# player("https://www.youtube.com/watch?v=TdeYkT7DEJQ")



import yt_dlp
import time
import random

def audio_make(url, output_name):
    # カスタムUser-Agentを設定（YouTubeに自動スクリプトとバレにくくする）
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"

    # yt-dlp のオプションを設定
    ydl_opts = {
        'format': 'bestaudio/best',  # 最高品質の音声を選択
        # 'outtmpl': output_name + ".mp3",  # 保存ファイル名
        'outtmpl': output_name,  # 保存ファイル名
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  # ビットレート設定
        }],
        'nocheckcertificate': True,  # 証明書エラーを無視
        'noplaylist': True,  # プレイリスト全体のダウンロードを防ぐ
        'quiet': True,  # 不要なログを抑える
        'user_agent': user_agent, # カスタムUser-Agentを設定
        'ffmpeg_location': r'C:\Program Files\ffmpeg-master-latest-win64-gpl-shared\ffmpeg-master-latest-win64-gpl-shared\bin',
    }

    # ランダムな遅延を入れてアクセスを分散（Bot対策）
    # # delay = random.uniform(1.5, 3.0)
    # print(f"Waiting for {delay:.2f} seconds before download...")
    # time.sleep(delay)

    # YouTubeの音声をダウンロード
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Download successful")
    #保存したとき，ファイルは上書きされる．


# YouTube動画のURLと保存先のファイル名（拡張子なし）を指定
audio_make('https://www.youtube.com/watch?v=yRBKzeCkuyQ', './audio/audio')


if __name__ == "__main__":
    main()
    
    
from playsound3 import playsound
import time
# time.sleep(5)
playsound("./audio/audio.mp3")
