import TkEasyGUI as sg

# window create
window = sg.Window("UI test", layout=[
    # テキスト
    [sg.Text("TkEasyGUI Test:" ),sg.Text("TkEasyGUI Test:" )],
    # テキスト入力
    [sg.Input(
        "input1", # テキスト
        key="-input1-", # 要素の参照キー
        enable_events=True # アクションがあれば実行する引数
    )],
    # 文字を隠すテキスト入力
    [sg.Input(
        "input2", # テキスト
        key="-input2-", # 要素の参照キー
        password_char="*" # 文字を隠す文字
    )],
    # 複数行入力テキスト
    [sg.Multiline(
        "multiine", # テキスト
        key="-multiline-", # 要素の参照キー
        enable_events=True, # アクションがあれば実行する引数
        size=(40, 2) # 縦横サイズ
    )],
    # スライダー
    [sg.Slider(
        key="-slide-", # 要素の参照キー
        enable_events=True, # アクションがあれば実行する引数
        orientation="h", # 水平（horizontal）
        range=(0, 100), # 範囲
        default_value=50, # デフォルトの数値
        expand_x=True # 水平方向に広げる
    )],
    # リストボックス、テキスト
    [
        sg.Listbox(
            ["list1", "list2", "list3", "list4"], # リストボックスの値リスト
            key="-listbox-", # 要素の参照キー
            enable_events=True, # アクションがあれば実行する引数
            select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED # リストの選択モード 使われているのは`extended`(multiple, browse, extended, single)
        ),
        sg.Text(
            "-", # ラベル
            key="-listbox-text-" # 要素の参照キー
    )],
    # ラジオボタン
    [
        sg.Radio(
            "Radio1", # ラベル
            group_id="abc", # グループID
            key="-radio1-", # 要素の参照キー
            enable_events=True # アクションがあれば実行する引数
        ),
        sg.Radio(
            "Radio2", # ラベル
            group_id="abc", # グループID
            key="-radio2-", # 要素の参照キー
            default=True, # デフォルトの選択
            enable_events=True # アクションがあれば実行する引数
        )
    ],
    # チェックボックス
    [
        sg.Checkbox(
            "Checkbox", # ラベル
            key="-checkbox-", # 要素の参照キー
            enable_events=True # アクションがあれば実行する引数
        ), 
        sg.Button(
            "Change", # ラベル
            key="-checkbox-button-" # 要素の参照キー
        )
    ],
    # コンボボックス
    [
        sg.Combo(
            ["combo1", "combo2", "combo3"], # コンボボックスの値リスト
            default_value="combo1", # デフォルトの値
            key="-combo-",  # 要素の参照キー
            enable_events=True # アクションがあれば実行する引数
        ), 
        sg.Button(
            "Change",  # ラベル
            key="-combo-button-" # 要素の参照キー
        )
    ],
    # ボタン
    [sg.Button("Exit"), sg.Button("Maximize"), sg.Button("Minimize"), sg.Button("Hide"), sg.Button("UnHide")],
], font=("Arial", 12), finalize=True, resizable=True)
# event loop

while True:
    event, values = window.read()
    print("#", event, values)
    if event in (None, "Exit", sg.WINDOW_CLOSED):
        break
    if event == "Maximize":
        # ウィンドウの最大化
        window.maximize()
        
    if event == "Minimize":
        # ウィンドウの縮小化
        window.minimize()
        
    if event == "Hide":
        # ウィンドウを隠す
        window.hide()
        
    if event == "UnHide":
        # ウィンドウの非表示を解除
        window.un_hide()
    
    # listbox内のものを選択した場合
    if event == "-listbox-":
        # リストボックスの値を取得し文字列と結合
        selected = " selected: " + "/".join(values["-listbox-"])
        
        # 結果をテキスト（-listbox-text-キー）要素に表示
        window["-listbox-text-"].update(text=selected)
    
    # -checkbox-button- キーのボタンが押された場合
    if event == "-checkbox-button-":
        # チェックボックスの現在の状態を取得
        b = window["-checkbox-"].get()
        
        # チェックボックスの状態を反転し、テキストを"Changed"に更新
        window["-checkbox-"].update(value=(not b), text="Changed")
    
    # -combo-button- キーのボタンが押された場合
    if event == "-combo-button-":
        # コンボボックス（-combo-キー）の値を"combo3"に変更
        window["-combo-"].update(value="combo3")
        
window.close()