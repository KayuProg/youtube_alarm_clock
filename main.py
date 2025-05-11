import set_time_and_run_timer
import TkEasyGUI as sg
import sys

def caution_window():
    input_font = ("Helvetica", 40)  # フォントサイズを大きく
    layout=[
        [sg.Text("Timer を Set しましょう！",key="title",text_align="center", font=("Helvetica", 40),expand_x=True,expand_y=True)],
        #処理ボタン
        [sg.Push(),
        sg.Button("OK !!",expand_x=1,font=("Helvetica", 40),background_color=["#dddddd"]), 
        sg.Push(),
      ],  # ボタン
    ]
    
    window=sg.Window("Waking time set notice",layout=layout,size=(900,600),padding_y=00)#paddingで中の位置調整

    while True:
        event,value=window.read()
        
        if event == "OK !!":
            #実際に書き換える
            with open("notice_window.txt", "r+", encoding="utf-8") as file:
                file.seek(0)
                file.write(str(1))
                file.truncate()  # 余計な部分を削除
            break

    window.close()
    
    
def main():
    with open("notice_window.txt", "r", encoding="utf-8") as file:
            windows_flag = file.readline().strip()
    print(windows_flag/)
    #windows_flagが0の時にcaution window表示．
    if windows_flag == "0":        
        caution_window()
        sys.exit()

    if windows_flag == "1":
         #notice windowを次回表示できるようにする．
        with open("notice_window.txt", "r+", encoding="utf-8") as file:
            file.seek(0)
            file.write(str(0))
            file.truncate()  # 余計な部分を削除
        
        set_time_and_run_timer.set_awake_time()

            



if __name__ == "__main__":
    main()
