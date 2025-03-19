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

def set_awake_time():
    input_font = ("Helvetica", 40)  # フォントサイズを大きく
    layout=[
        [sg.Text("明日何時に起きますか？",text_align="center", font=("Helvetica", 5),expand_x=True)],
        #Input
        [sg.Push(),
        sg.Input("", key="hour",font=input_font,size=[5,5]), sg.Text("時", font=("Helvetica", 50)),
        sg.Input("", key="minute",font=input_font,size=[5,5]), sg.Text("分", font=("Helvetica", 50)),
        sg.Push(),],
        #処理ボタン
        [sg.Push(),
        sg.Button("Set and Start",expand_x=1,font=("Helvetica", 40),background_color=["#dddddd"]), 
        sg.Push(),
        sg.Button("'Re' set",expand_x=1,font=("Helvetica", 40),background_color=["#dddddd"]),
        sg.Push()],  # ボタン
    ]

    window=sg.Window("Input Wake up Time",layout=layout,size=(900,600),padding_y=100)#paddingで中の位置調整

    #日付も設定しないとダメだよね．ｋ
    while True:
        event,value=window.read()
        
        if event == "Set and Start":
            #書き込んでタイマー開始
            h=int(value["hour"])
            m=int(value["minute"])
            #書き込むべき時間に変換     
            time = convert_time(h,m)
            print(time)
            window.close()
            break
        
        if event == "'Re' set":
            #時刻を書き換えるだけ．
            h=int(value["hour"])
            m=int(value["minute"])
            time = convert_time(h,m)
            print(time)
            window.close()
            break
            
      
        
    window.close()


set_awake_time()





























