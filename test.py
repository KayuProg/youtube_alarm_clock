import TkEasyGUI as sg
import datetime

def convert_time(h,m):
    now = datetime.datetime.now()
    now_h=now.hour
    if now_h>12:
        #12:00（お昼）以降だったら次の日を設定．
        now=now+datetime.timedelta(days=1)
        # print(now.day)
    time = datetime.datetime(now.year, now.month, now.day, h, m)

    return time

timer_flag=0

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
        sg.Button("'Re' set",expand_x=1,font=("Helvetica", 40),background_color=["#dddddd"]),
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
            window["minute"].update("0")
        elif event == "6:30":
            window["hour"].update("6")
            window["minute"].update("30")
        elif event == "7:00":
            window["hour"].update("7")
            window["minute"].update("0")
        elif event == "7:30":
            window["hour"].update("7")
            window["minute"].update("30")
        elif event == "8:00":
            window["hour"].update("8")
            window["minute"].update("0")
        elif event == "8:30":
            window["hour"].update("8")
            window["minute"].update("3")
        elif event == "9:00":
            window["hour"].update("9")
            window["minute"].update("0")
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
            if timer_flag==0:
                #timerをスタートする関数．どうする？非同期関数？
                timer_flag==1
                pass
            # window.close()
            # break
        
        #こっちのボタンいらなくね？
        if event == "'Re' set":
            if value["hour"]=="" or value["minute"]=="":
                continue
            #時刻を書き換えるだけ．
            h=int(value["hour"])
            m=int(value["minute"])
            time = convert_time(h,m)
            print("Reset time to ",time)
            window["title"].update(f"{h}時{m}分にtimerをsetしました．",30)
            # window.close()
            # break
            
      
        
    window.close()


set_awake_time()





























