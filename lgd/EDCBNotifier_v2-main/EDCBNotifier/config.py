
# ====================  環境設定  ====================

# [] で囲われている部分は配列 (list)
# {} で囲われている部分は辞書 (dict)
# 文字列は必ずシングルクオート ('') で囲んでください
# ハッシュ (#) をつけるとコメントになります（ // はコメントになりません）
# 文字コード UTF-8 (BOM なし)・改行コード LF 以外で保存すると動作しなくなるので注意（メモ帳は基本的に NG ）
# できれば VSCode などのシンタックスハイライトのあるエディタでの編集を推奨します


# 通知タイプ
# LINE (LINE Notify)・Tweet (ツイート)・DirectMessage (ダイレクトメッセージ) から設定
# [] 内にカンマ区切りで複数設定できます

# ex (LINE Notify): NOTIFY_TYPE = ['LINE']
# ex (LINE Notify と Discord Webhook): NOTIFY_TYPE = ['LINE', 'Discord']
# ex (ダイレクトメッセージ): NOTIFY_TYPE = ['DirectMessage']
# ex (LINE Notify とツイート): NOTIFY_TYPE = ['LINE', 'Tweet']
# ex (LINE Notify とダイレクトメッセージ): NOTIFY_TYPE = ['LINE', 'DirectMessage']
# ex (全て): NOTIFY_TYPE = ['LINE', 'Tweet', 'Discord', 'DirectMessage']

NOTIFY_TYPE = ['LINE', 'Discord', 'Tweet']


# 通知を行うイベント
# 通知するイベントのオン・オフを指定できます たとえば頻度の多い PostNotify だけ通知しない設定も可能です
# ここで設定したイベントだけが通知されます（通知オン） 設定しなかったイベントは通知されません（通知オフ）
# 各 .bat ファイルを配置しないことでも通知イベントのオン・オフは可能ですが、できるだけこの設定を使うことを推奨します

# PostAddReserve … 予約を追加したとき ( PostAddReserve.bat が実行されたとき)
# PostChgReserve … 予約を変更したとき ( PostChgReserve.bat が実行されたとき)
# PostRecStart … 録画を開始したとき（ PostRecStart.bat が実行されたとき）
# PostRecEnd … 録画を終了したとき（ PostRecEnd.bat が実行されたとき）
# PostNotify … 更新通知が送られたとき（ PostNotify.bat が実行されたとき）

# ex (全て通知): NOTIFY_EVENT = ['PostAddReserve', 'PostChgReserve', 'PostRecStart', 'PostRecEnd', 'PostNotify']
# ex (PostNotify 以外を通知): NOTIFY_EVENT = ['PostAddReserve', 'PostChgReserve', 'PostRecStart', 'PostRecEnd']
# ex (予約の追加・変更を通知): NOTIFY_EVENT = ['PostAddReserve', 'PostChgReserve']
# ex (録画の開始・終了を通知): NOTIFY_EVENT = ['PostRecStart', 'PostRecEnd']
# ex (録画結果だけ通知): NOTIFY_EVENT = ['PostRecEnd']

NOTIFY_EVENT = ['PostAddReserve', 'PostChgReserve', 'PostRecStart', 'PostRecEnd']


# 通知時に同時に送信する画像（フルパスで指定）
# 画像を config.py と同じ階層に置く場合はファイル名だけの指定でも大丈夫です
# 画像サイズが大きすぎると送れない場合があるので注意
# None（シングルクオートはつけない）に設定した場合は画像を送信しません

# ex: NOTIFY_IMAGE = 'C:\Users\User\Pictures\EDCBNotifier.png'
# ex: NOTIFY_IMAGE = 'EDCBNotifier.png'
# ex: NOTIFY_IMAGE = None

NOTIFY_IMAGE_LINE = 'None'
NOTIFY_IMAGE_DISCORD = 'None'
NOTIFY_IMAGE_TWITTER = 'None'
NOTIFY_IMAGE_TWITTER_DM = 'None'


# ダイレクトメッセージの宛先（スクリーンネーム：@ から始まるアカウントの ID で指定）
# 上の設定で DirectMessage (ダイレクトメッセージ) を設定した場合に適用されます
# @ はつけずに指定してください 予め宛先のアカウントと DM が送信できる状態になっていないと送れません
# None（シングルクオートはつけない）に設定した場合は自分宛てに送信します

# ex: NOTIFY_DIRECTMESSAGE_TO = 'AbeShinzo'
# ex: NOTIFY_DIRECTMESSAGE_TO = None

NOTIFY_DIRECTMESSAGE_TO = 'None'


# ログをファイルに保存（出力）するか
# True に設定した場合は、ログを config.py と同じフォルダの EDCBNotifier.log に保存します（コンソールに表示しない・前回のログは上書きされる）
# False に設定した場合は、ログを保存しません（コンソールに表示する）
# True・False にはシングルクオートをつけず、大文字で始めてください (true・false は NG)
# うまく通知されないときに True にしてログを確認してみるといいかも

NOTIFY_LOG = False

# ドライブ空き容量 (Cドライブの場合 'C') (PostRecEnd以外で実行)
# ex: DISK_FREE = 'C'
# ex: DISK_FREE = 'None'

DISK_FREE = 'None'

# 放送局・タイトルフィルタ
# CHANNEL_FILTER で設定した放送局のタイトルがTITLE_FILTERに含まれていたら実行される。
# 放送局・タイトルは半角英数字で設定してください。
# ex (ツイート無効化): FILTER_NOTIFY_TYPE = ['Tweet']

FILTER_NOTIFY_TYPE = ['None']

CHANNEL_FILTER = {
    'AT-X': '',
    'テレ朝チャンネル': '',
    'TBSチャンネル': '',
}
TITLE_FILTER = {
    '[無]': '',
    '[無料]': '',
    '【無料】': '',
}

# ===================  メッセージ  ===================

# 改行を入れる場合は文字列内に \n と入力してください
# 文字列は + で連結できます
# https://github.com/xtne6f/EDCB/blob/70b2331aadb328eb347fe0c4e4e23c8e91d286b7/Document/Readme_EpgTimer.txt#L929-L1008 と
# https://github.com/xtne6f/EDCB/blob/4c3bd5be3dc49607aa821d728105955c03fba4db/Document/Readme_Mod.txt#L451-L475 に記載されている EDCB のマクロが使えます
# マクロは $$ で囲んでください (ex: $ServiceName$)

# また、独自にいくつかのマクロを追加しています
# ・$HashTag$ … 放送局名から取得したハッシュタグ（ハッシュタグは utils.py の Utils.getChannelHashtag() メソッドで定義）
# ・$discord_emoji$ … 放送局名から取得したハッシュタグ（ハッシュタグは utils.py の Utils.getChannelHashtag2() メソッドで定義）
# ・$HashTagTitle$ … 番組タイトルから取得したハッシュタグ（ハッシュタグは下記の NOTIFY_HASHTAG_TITLE で定義）
# ・$NotifyName$ … $NotifyID$ から取得した更新通知タイプ（ $NotifyID$ = 1 … EPGデータ更新 2 … 予約情報更新 3 … 録画結果情報更新）
# ・$ServiceNameHankaku$ … $ServiceName$（放送局名）の英数字を半角に変換したもの
# ・$TitleHankaku$ … $Title$（番組タイトル）の英数字を半角に変換したもの
# ・$Title2Hankaku$ … $Title2$（番組タイトル・[]で囲まれている部分を削除したもの）の英数字を半角に変換したもの
# ・$TimeYYYY$ … 実行時刻の上2桁付き西暦年 (ex: 2020 (年))  $TimeYY$ … 実行時刻の上2桁なし西暦年 (ex: 20 (年))
# ・$TimeMM$ … 実行時刻の2桁固定の月 (ex: 07 (月))  $TimeM$ … 実行時刻の月 (ex: 7 (月))
# ・$TimeDD$ … 実行時刻の2桁固定の日 (ex: 09 (日))  $TimeD$ … 実行時刻の日 (ex: 9 (日))
# ・$TimeW$ … 実行時刻の曜日 (ex: 火 (曜日))
# ・$TimeHH$ … 実行時刻の2桁固定の時 (24時間) (ex: 06 (時))  $TimeH$ … 実行時刻の日 (ex: 6 (時))
# ・$TimeII$ … 実行時刻の2桁固定の分 (ex: 08 (分))  $TimeI$ … 実行時刻の分 (ex: 8 (分))
# ・$TimeSS$ … 実行時刻の2桁固定の秒 (ex: 02 (秒))  $TimeS$ … 実行時刻の分 (ex: 2 (秒))
# ・$Disksize1$ … 録画フォルダ又は指定したドライブの空き容量 ((ドライブ)残り ??.??MB ??.??GB)
# ・$filesize$ … tsファイルのサイズ (??.??MB ??.??GB) (先頭に1文字半角空白有)
# ・$ChLogo$ … Discord向け局ロゴ絵文字(対応局少ない)
# ・$NWName$ … ネットワーク名 [(地デジ) (BS) (CS1) (CS2) (SPHD) (CATV)]
# ・$EID16v2$ … FFFFの場合プログラム予約と表記(先頭に1文字半角空白有)
# ・$Resultv2$ … ($Result$の先頭に半角空白を入れただけ)
# ・$ReserveCommentv2$ … ($ReserveComment$の先頭に半角空白を入れただけ)

# Twitterに送信するメッセージ
NOTIFY_MESSAGE_TWITTER = {

    # 予約を追加したとき（ PostAddReserve.bat が実行されたとき）に送信するメッセージ
    'PostAddReserve': '★予約追加：$ServiceName$$NWName$$EID16v2$ $SDYYYY$/$SDMM$/$SDDD$($SDW$)\n' +
                      '$STHH$:$STMM$～$ETHH$:$ETMM$ $Title$$ReserveCommentv2$',

    # 予約を変更したとき（ PostChgReserve.bat が実行されたとき）に送信するメッセージ
    'PostChgReserve': '◆EPG更新：$ServiceName$$NWName$$EID16v2$\n' +
                      '変更前：$SDYYOLD$/$SDMMOLD$/$SDDDOLD$($SDWOLD$) $STHHOLD$:$STMMOLD$～$ETHHOLD$:$ETMMOLD$ $TitleOLD$\n' +
                      '変更後：$SDYY$/$SDMM$/$SDDD$($SDW$) $STHH$:$STMM$～$ETHH$:$ETMM$ $Title$',

    # 予約を変更したとき(番組名変更のみ)（ PostChgReserve.bat が実行されたとき）に送信するメッセージ
    'PostChgReserve2': '◆EPG更新：$ServiceName$$NWName$$HashTag$$EID16v2$ $SDYY$/$SDMM$/$SDDD$($SDW$) $STHH$:$STMM$～$ETHH$:$ETMM$\n' +
                      '番組名が変更されました。\n' +
                      '変更前：$TitleOLD$\n' +
                      '変更後：$Title$',

    # 予約を変更したとき(時間変更のみ)（ PostChgReserve.bat が実行されたとき）に送信するメッセージ
    'PostChgReserve3': '◆EPG更新：$ServiceName$$NWName$$HashTag$$EID16v2$ $SDMMOLD$/$SDDDOLD$($SDWOLD$)\n' +
                      '$Title$\n' +
                      '放送時間が変更されました。\n' +
                      '変更前：$STHHOLD$:$STMMOLD$～$ETHHOLD$:$ETMMOLD$\n' +
                      '変更後：$STHH$:$STMM$～$ETHH$:$ETMM$',

    # 録画を開始したとき（ PostRecStart.bat が実行されたとき）に送信するメッセージ
    'PostRecStart':   '●録画開始：$ServiceName$$NWName$$HashTag$$EID16v2$ $SDYYYY$/$SDMM$/$SDDD$($SDW$)\n' + 
                      '$STHH$:$STMM$～$ETHH$:$ETMM$ $Title$$HashTagTitle$',

    # 録画を終了したとき（ PostRecEnd.bat が実行されたとき）に送信するメッセージ
    'PostRecEnd':     '■録画終了：$ServiceName$$NWName$$HashTag$$EID16v2$ $SDYYYY$/$SDMM$/$SDDD$($SDW$)\n' + 
                      '$STHH$:$STMM$～$ETHH$:$ETMM$ $Title$$HashTagTitle$\n' +
                      'Drop:$Drops$$Resultv2$$filesize$',

    # 更新通知が送られたとき（ PostNotify.bat が実行されたとき）に送信するメッセージ
    'PostNotify':     '🔔通知：$NotifyName$ ($TimeYY$/$TimeMM$/$TimeDD$ $TimeHH$:$TimeII$:$TimeSS$)',

}

# Discordに送信するメッセージ
NOTIFY_MESSAGE_DISCORD = {

    # 予約を追加したとき（ PostAddReserve.bat が実行されたとき）に送信するメッセージ
    'PostAddReserve': '✅予約追加 $ChLogo$【$ServiceName$$NWName$】$ReserveCommentv2$$EID16v2$\n' +
                      '$SDYYYY$/$SDMM$/$SDDD$($SDW$) $STHH$:$STMM$～$ETHH$:$ETMM$\n' +
                      '`$Title$` $Disksize1$',

    # 予約を変更したとき（ PostChgReserve.bat が実行されたとき）に送信するメッセージ
    'PostChgReserve': '🔶EPG更新 $ChLogo$【$ServiceName$$NWName$】$EID16v2$\n' +
                      '[変更前]$SDYYOLD$/$SDMMOLD$/$SDDDOLD$($SDWOLD$) $STHHOLD$:$STMMOLD$～$ETHHOLD$:$ETMMOLD$ `$TitleOLD$`\n' +
                      '[変更後]$SDYY$/$SDMM$/$SDDD$($SDW$) $STHH$:$STMM$～$ETHH$:$ETMM$ `$Title$`',

    # 予約を変更したとき(番組名変更のみ)（ PostChgReserve.bat が実行されたとき）に送信するメッセージ
    'PostChgReserve2': '🔶EPG更新 $ChLogo$【$ServiceName$$NWName$】$EID16v2$\n' +
                      '$SDYY$/$SDMM$/$SDDD$($SDW$) $STHH$:$STMM$～$ETHH$:$ETMM$\n' +
                      '番組名が変更されました。\n' +
                      '[変更前]`$TitleOLD$`\n' +
                      '[変更後]`$Title$`',

    # 予約を変更したとき(時間変更のみ)（ PostChgReserve.bat が実行されたとき）に送信するメッセージ
    'PostChgReserve3': '🔶EPG更新 $ChLogo$【$ServiceName$$NWName$】$EID16v2$\n' +
                      '`$Title$`\n' +
                      '放送時間が変更されました。\n' +
                      '[変更前]$SDMMOLD$/$SDDDOLD$($SDWOLD$) $STHHOLD$:$STMMOLD$～$ETHHOLD$:$ETMMOLD$\n' +
                      '[変更後]$SDMM$/$SDDD$($SDW$) $STHH$:$STMM$～$ETHH$:$ETMM$',

    # 録画を開始したとき（ PostRecStart.bat が実行されたとき）に送信するメッセージ
    'PostRecStart':   '🔴録画開始 $ChLogo$【$ServiceName$$NWName$】$EID16v2$\n' +
                      '$SDYYYY$/$SDMM$/$SDDD$($SDW$) $STHH$:$STMM$～$ETHH$:$ETMM$\n' +
                      '`$Title$`$Disksize1$',

    # 録画を終了したとき（ PostRecEnd.bat が実行されたとき）に送信するメッセージ
    'PostRecEnd':     '⬜ 録画終了 $ChLogo$【$ServiceName$$NWName$】$EID16v2$\n' +
                      '$SDYYYY$/$SDMM$/$SDDD$($SDW$) $STHH$:$STMM$～$ETHH$:$ETMM$\n' +
                      '`$Title$`\n' +
                      'Drop:**$Drops$** Comment:**$Result$**\n' +
                      '$Disksize1$$filesize$',

    # 更新通知が送られたとき（ PostNotify.bat が実行されたとき）に送信するメッセージ
    'PostNotify':     '🔔通知：$NotifyName$ ($TimeYY$/$TimeMM$/$TimeDD$ $TimeHH$:$TimeII$:$TimeSS$)',

}

# LINEに送信するメッセージ
NOTIFY_MESSAGE_LINE = {

    # 予約を追加したとき（ PostAddReserve.bat が実行されたとき）に送信するメッセージ
    'PostAddReserve': '★予約追加：$ServiceName$$NWName$ $SDYYYY$/$SDMM$/$SDDD$($SDW$)\n' +
                      '$STHH$:$STMM$～$ETHH$:$ETMM$ $Title$$ReserveCommentv2$$EID16v2$',

    # 予約を変更したとき（ PostChgReserve.bat が実行されたとき）に送信するメッセージ
    'PostChgReserve': '◆EPG更新：$ServiceName$$NWName$$EID16v2$\n' +
                      '変更前：$SDYYOLD$/$SDMMOLD$/$SDDDOLD$($SDWOLD$) $STHHOLD$:$STMMOLD$～$ETHHOLD$:$ETMMOLD$ $TitleOLD$\n' +
                      '変更後：$SDYY$/$SDMM$/$SDDD$($SDW$) $STHH$:$STMM$～$ETHH$:$ETMM$ $Title$',

    # 予約を変更したとき(番組名変更のみ)（ PostChgReserve.bat が実行されたとき）に送信するメッセージ
    'PostChgReserve2': '◆EPG更新：$ServiceName$$NWName$$EID16v2$ $SDYY$/$SDMM$/$SDDD$($SDW$) $STHH$:$STMM$～$ETHH$:$ETMM$\n' +
                      '番組名が変更されました。\n' +
                      '変更前：$TitleOLD$\n' +
                      '変更後：$Title$',

    # 予約を変更したとき(時間変更のみ)（ PostChgReserve.bat が実行されたとき）に送信するメッセージ
    'PostChgReserve3': '◆EPG更新：$ServiceName$$NWName$$EID16v2$\n' +
                      '$Title$\n' +
                      '放送時間が変更されました。\n' +
                      '変更前：$STHHOLD$:$STMMOLD$～$ETHHOLD$:$ETMMOLD$\n' +
                      '変更後：$STHH$:$STMM$～$ETHH$:$ETMM$',

    # 録画を開始したとき（ PostRecStart.bat が実行されたとき）に送信するメッセージ
    'PostRecStart':   '●録画開始：$ServiceName$$NWName$ $SDYYYY$/$SDMM$/$SDDD$($SDW$)\n' + 
                      '$STHH$:$STMM$～$ETHH$:$ETMM$ $Title$$HashTagTitle$$EID16v2$',

    # 録画を終了したとき（ PostRecEnd.bat が実行されたとき）に送信するメッセージ
    'PostRecEnd':     '■録画終了：$ServiceName$$NWName$ $SDYYYY$/$SDMM$/$SDDD$($SDW$)\n' + 
                      '$STHH$:$STMM$～$ETHH$:$ETMM$ $Title$$HashTagTitle$$EID16v2$\n' +
                      'Drop:$Drops$ S:$Scrambles$$Resultv2$$Disksize1$$filesize$',

    # 更新通知が送られたとき（ PostNotify.bat が実行されたとき）に送信するメッセージ
    'PostNotify':     '🔔通知：$NotifyName$ ($TimeYY$/$TimeMM$/$TimeDD$ $TimeHH$:$TimeII$:$TimeSS$)',

}


# 番組タイトル（半角）に対応するハッシュタグ（ $HashTagTitle$ マクロにて利用・部分一致）
# 番組タイトルの判定には $TitleHankaku$ の値を利用します
# 以下に存在しない番組タイトルのハッシュタグは空文字になります
# 以下の記述例を参考に、番組タイトルとハッシュタグの対応を記述してください

NOTIFY_HASHTAG_TITLE = {
    'ゆるキャン△ SEASON2': ' #yurucamp',  # 記述例1
    'のんのんびより のんすとっぷ': ' #なのん #nonnontv',  # 記述例2
    'SPY×FAMILY': ' #SPY_FAMILY',
    'ハーレムきゃんぷっ！': ' #harecam #ハレきゃん',
    'ぼっち・ざ・ろっく！': ' #BTR_anime',
    'ラブライブ': ' #lovelive',
    'ポプテピピック': ' #PPTP',
    'チェンソーマン': ' #chainsawman',
    '陰の実力者になりたくて！': ' #shadow_garden',
    'モブサイコ100': ' #mobpsycho100',
    'エロマンガ先生': ' #eromanga_sensei',
}
