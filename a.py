import TkEasyGUI as sg

# define layout --- make 12 buttons
layout = []
for row in range(3):
    layout.append([])
    for col in range(4):
        no = row*4+col+1
        btn = sg.Button(str(no), key=f"-button{no}",
                        size=(3, 1),
                        etadata={"no": no}) # ボタンにメタデータを追加
        layout[row].append(btn)
# add close button
layout.append([sg.HSeparator()]) # 横線
layout.append([sg.Button("Close")])

# 最終的なレイアウト
# layout = [
#     [sg.Button(str(1), key=f"-button1",size=(3, 1), metadata={"no": 1}), sg.Button(str(2), key=f"-button2",size=(3, 1), metadata={"no": 2}), sg.Button(str(3), key=f"-button3",size=(3, 1), metadata={"no": 3}), sg.Button(str(4), key=f"-button4",size=(3, 1), metadata={"no": 4})],
#     [sg.Button(str(5), key=f"-button5",size=(3, 1), metadata={"no": 5}), sg.Button(str(6), key=f"-button6",size=(3, 1), metadata={"no": 6}), sg.Button(str(7), key=f"-button7",size=(3, 1), metadata={"no": 7}), sg.Button(str(8), key=f"-button8",size=(3, 1), metadata={"no": 8})],
#     [sg.Button(str(9), key=f"-button9",size=(3, 1), metadata={"no": 9}), sg.Button(str(10), key=f"-button10",size=(3, 1), metadata={"no": 10}), sg.Button(str(11), key=f"-button11",size=(3, 1), metadata={"no": 11}), sg.Button(str(12), key=f"-button12",size=(3, 1), metadata={"no": 12})],
#     [sg.HSeparator()],
#     [sg.Button("Close")]
# ]


# make window
window = sg.Window("Many buttons", layout)

# イベントループ
for event, values in window.event_iter():
    # close button
    if event == "Close":
        break
    
    # -button という文字で始まっているかどうかをチェック
    # -button で始まっていれば True 
    if event.startswith("-button"):
        # アクジョンがあった event のメタデータの取得
        no = window[event].metadata["no"]
        sg.popup(f"You Pushed {no}")
        # ボタンの無効化（押せなくする）
        window[event].update(disabled=True)
