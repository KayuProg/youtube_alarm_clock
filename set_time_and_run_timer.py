import TkEasyGUI as sg
import datetime
import time
import threading
import play_music
import sys


def convert_time(h,m):
    now = datetime.datetime.now()
    now_h=now.hour
    if now_h>12:
        #12:00（お昼）以降だったら次の日を設定．
        now=now+datetime.timedelta(days=1)
        # print(now.day)
    time = datetime.datetime(now.year, now.month, now.day, h, m)

    return time


def timer():
   # play_music.play_music()
    while 1:
        now=datetime.datetime.now()
        with open("awake_time.txt", "r", encoding="utf-8") as file:
            ref = file.readline().strip()  # 一行目を取得して前後の空白や改行を削除
        ref_converted=datetime.datetime.strptime(ref,"%Y-%m-%d %H:%M:%S")
        print("ref is ",ref_converted)
        if ref_converted<now:
            print("アラームを流します")
            play_music.play_music()
        else:
            print("まだ寝てていいよ")
            
        time.sleep(3)
    #play_music.play_music()
    #timer_flag.txtを"0"に戻す．
    # with open("timer_flag.txt", "r+", encoding="utf-8") as file:
    #                 file.seek(0)
    #                 file.write("0")
    #                 file.truncate()  # 余計な部分を削除
    return 0

def set_awake_time():
    input_font = ("Helvetica", 40)  # フォントサイズを大きく
    layout=[
        [sg.Text("明日何時に起きますか？",key="title",text_align="center", font=("Helvetica", 40),expand_x=True,expand_y=True)],
        #Input
        [sg.Push(),
        sg.Input("", key="hour",font=input_font,size=[5,5]), sg.Text("時", font=("Helvetica", 50),expand_y=True),
        sg.Input("", key="minute",font=input_font,size=[5,5]), sg.Text("分", font=("Helvetica", 50),expand_y=True),
        sg.Push(),],
        #処理ボタン
        [sg.Push(),
        sg.Button("Set and Start",expand_x=1,font=("Helvetica", 40),background_color=["#dddddd"]), 
        sg.Push(),
        sg.Button("Stop",expand_x=1,font=("Helvetica", 40),background_color=["#dddddd"]),
        sg.Push()],  # ボタン
        
        [sg.Push(),
        sg.Button("6:00",expand_x=1,font=("Helvetica", 30),background_color=["#dddddd"]), 
        sg.Push(),
        sg.Button("6:30",expand_x=1,font=("Helvetica", 30),background_color=["#dddddd"]), 
        sg.Push(),
        sg.Button("7:00",expand_x=1,font=("Helvetica", 30),background_color=["#dddddd"]), 
        sg.Push(),
        sg.Button("7:30",expand_x=1,font=("Helvetica", 30),background_color=["#dddddd"]),
        sg.Push(),
        ], 
        
        [sg.Push(),
        sg.Button("8:00",expand_x=1,font=("Helvetica", 30),background_color=["#dddddd"]),
        sg.Push(),
        sg.Button("8:30",expand_x=1,font=("Helvetica", 30),background_color=["#dddddd"]),
        sg.Push(),
        sg.Button("9:00",expand_x=1,font=("Helvetica", 30),background_color=["#dddddd"]),
        sg.Push(),
        sg.Button("9:30",expand_x=1,font=("Helvetica", 30),background_color=["#dddddd"]),
        sg.Push(),
        ]
    ]
    
   

    window=sg.Window("Input Wake up Time",layout=layout,size=(900,600),padding_y=00)#paddingで中の位置調整

    #日付も設定しないとダメだよね．ｋ
    while True:
        event,value=window.read()
        
        if event == "6:00":
            window["hour"].update("6")
            window["minute"].update("00")
        elif event == "6:30":
            window["hour"].update("6")
            window["minute"].update("30")
        elif event == "7:00":
            window["hour"].update("7")
            window["minute"].update("00")
        elif event == "7:30":
            window["hour"].update("7")
            window["minute"].update("30")
        elif event == "8:00":
            window["hour"].update("8")
            window["minute"].update("00")
        elif event == "8:30":
            window["hour"].update("8")
            window["minute"].update("30")
        elif event == "9:00":
            window["hour"].update("9")
            window["minute"].update("00")
        elif event == "9:30":
            window["hour"].update("9")
            window["minute"].update("30")

        
        if event == "Set and Start":
            #書き込んでタイマー開始
            # print("\n",value["hour"],"\n")
            #入力がないときの処理
            if value["hour"]=="" or value["minute"]=="":
                continue
            h=int(value["hour"])
            m=int(value["minute"])
            #書き込むべき時間に変換     
            time = convert_time(h,m)
            print("Set time to ",time)
            window["title"].update(f"{h}時{m}分にtimerをsetしました．",30)
            
            #実際に書き換える
            with open("awake_time.txt", "r+", encoding="utf-8") as file:
                file.seek(0)
                file.write(str(time))
                file.truncate()  # 余計な部分を削除

                        
            with open("timer_flag.txt", "r", encoding="utf-8") as file:
                timer_flag = file.readline().strip()

            if timer_flag=="0":
                timer_thread=threading.Thread(target=timer,daemon=True)
                #timerをスタートする関数．どうする？非同期関数？
                timer_thread.start()
                print(timer_flag)
                #timer_flagをの内容を"1"に書き換える．
                with open("timer_flag.txt", "r+", encoding="utf-8") as file:
                    file.seek(0)
                    file.write("1")
                    file.truncate()  # 余計な部分を削除

            # window.close()
            # break
        
        if event == "Stop":
            with open("timer_flag.txt", "r+", encoding="utf-8") as file:
                    file.seek(0)
                    file.write("0")
                    file.truncate()
            sys.exit()
            break
            
      
        
    window.close()





if __name__ == "__main__":
    set_awake_time()
    

