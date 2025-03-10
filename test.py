# from pytubefix import YouTube
# from moviepy import *
# import os
# # YouTube動画をロード
# yt = YouTube("https://www.youtube.com/watch?v=ekr2nIex040")

# # 最高品質のオーディオストリームを選択
# audio_stream = yt.streams.filter(only_audio=True).first()

# # オーディオを一時ファイルとしてダウンロード
# temp_file = audio_stream.download()

# # MoviePyを使用してオーディオをMP3に変換
# audio_clip = AudioFileClip(temp_file)
# audio_clip.write_audiofile("test.mp3", codec="libmp3lame")

# # 一時ファイルを削除
# os.remove(temp_file)

# # YouTube動画のURLと保存先のファイル名（拡張子なし）を指定
# # download_youtube_audio_as_mp3('https://www.youtube.com/watch?v=ekr2nIex040', 'apt')


import yt_dlp
import time
import random

def download_youtube_audio_as_mp3(url, output_name):
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

# YouTube動画のURLと保存先のファイル名（拡張子なし）を指定
download_youtube_audio_as_mp3('https://www.youtube.com/watch?v=ekr2nIex040', './audio/audio')



    
from playsound3 import playsound
import time
# time.sleep(5)
playsound("./apt.mp3")