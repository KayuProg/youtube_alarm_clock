# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlists.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

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

        # print(urls)
    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred: {e.content}")



if __name__ == "__main__":
    main()