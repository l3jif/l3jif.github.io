
import colorama
import os
import shutil
import sys

import config
import settings
from SendDiscord import Discord
from SendLINE import LINE
from SendTwitter import Twitter
from Utils import Utils

# バージョン情報
__version__ = '1.2.0'


def main():
    # マクロを取得
    macros = Utils.getMacro(os.environ)

    # このファイルが存在するフォルダの絶対パス
    current_folder = os.path.dirname(os.path.abspath(sys.argv[0]))

    # ターミナルの横幅
    # conhost.exe だと -1px しないと改行されてしまう
    terminal_columns = shutil.get_terminal_size().columns - 1

    # 初期化
    colorama.init(autoreset=True)
    if config.NOTIFY_LOG:  # 標準出力をファイルに変更
        sys.stdout = open(current_folder + '/EDCBNotifier.log', mode='w', encoding='utf-8')
        sys.stderr = open(current_folder + '/EDCBNotifier.log', mode='w', encoding='utf-8')

    # ヘッダー
    print('=' * terminal_columns)
    print(f'+++++{f"EDCBNotifier version {__version__}":^{terminal_columns - 10}}+++++')
    print('=' * terminal_columns)

    # 引数を受け取る
    if len(sys.argv) > 1:

        # 呼び出し元のイベント
        caller = sys.argv[1]  # 呼び出し元のバッチファイルの名前
        print(f'Event: {caller}')
        # 実行時刻
        print(f'Execution Time: {Utils.getExecutionTime()}')

        # NOTIFY_MESSAGE にあるイベントでかつ通知がオンになっていればメッセージをセット
        if (caller in config.NOTIFY_MESSAGE_TWITTER and caller in config.NOTIFY_EVENT and caller not in "PostChgReserve"):
            message = config.NOTIFY_MESSAGE_TWITTER[caller]
            message_discord = config.NOTIFY_MESSAGE_DISCORD[caller]
            message_line = config.NOTIFY_MESSAGE_LINE[caller]
        elif caller in "PostChgReserve" and macros["TitleOLD"] != macros["Title"] and macros["SDDOLD"] + macros["STHOLD"] + macros["STMOLD"] + macros["EDDOLD"] + macros["ETHOLD"] + macros["ETMOLD"] != macros["SDD"] + macros["STH"] + macros["STM"] + macros["EDD"] + macros["ETH"] + macros["ETM"]: #番組名・時間変更
                message = config.NOTIFY_MESSAGE_TWITTER["PostChgReserve"]
                message_discord = config.NOTIFY_MESSAGE_DISCORD["PostChgReserve"]
                message_line = config.NOTIFY_MESSAGE_LINE["PostChgReserve"]
        elif caller in "PostChgReserve" and macros["TitleOLD"] != macros["Title"] and macros["SDDOLD"] + macros["STHOLD"] + macros["STMOLD"] + macros["EDDOLD"] + macros["ETHOLD"] + macros["ETMOLD"] == macros["SDD"] + macros["STH"] + macros["STM"] + macros["EDD"] + macros["ETH"] + macros["ETM"]: #番組名変更のみ
                message = config.NOTIFY_MESSAGE_TWITTER["PostChgReserve2"]
                message_discord = config.NOTIFY_MESSAGE_DISCORD["PostChgReserve2"]
                message_line = config.NOTIFY_MESSAGE_LINE["PostChgReserve2"]
        elif caller in "PostChgReserve" and macros["SDDOLD"] + macros["STHOLD"] + macros["STMOLD"] + macros["EDDOLD"] + macros["ETHOLD"] + macros["ETMOLD"] != macros["SDD"] + macros["STH"] + macros["STM"] + macros["EDD"] + macros["ETH"] + macros["ETM"] and macros["TitleOLD"] == macros["Title"]: #時間変更のみ
                message = config.NOTIFY_MESSAGE_TWITTER["PostChgReserve3"]
                message_discord = config.NOTIFY_MESSAGE_DISCORD["PostChgReserve3"]
                message_line = config.NOTIFY_MESSAGE_LINE["PostChgReserve3"]

        # NOTIFY_MESSAGE にあるイベントだが、通知がオフになっているので終了
        elif caller in config.NOTIFY_MESSAGE:
            print(f'Info: {caller} notification is off, so it ends.')
            print('=' * terminal_columns)
            sys.exit(0)

        # 引数が不正なので終了
        else:
            Utils.error('Invalid argument.')

    # 引数がないので終了
    else:
        Utils.error('Argument does not exist.')

    print('-' * terminal_columns)

    # 放送局タイトルフィルタ
    Titlefilter = macros["Titlefilter"]
    Channelfilter = macros["channelfilter"]
    if Titlefilter == "0" and Channelfilter == "0": #configのTITLE_FILTER CHANNEL_FILTERに文字例存在しない場合
        titlefilter = "1"
    elif Titlefilter == "0" and Channelfilter == "1": #チャンネルは存在するがタイトルが一致しない場合
        titlefilter = "0"
    elif Titlefilter == "1" and Channelfilter == "1": #チャンネルタイトル両方一致する場合
        titlefilter = "1"
    else:
        titlefilter = "1"
    # メッセージを置換
    for macro, macro_value in macros.items():
        # $$ で囲われた文字を置換する
        message = message.replace(f'${macro}$', macro_value)
        message_discord = message_discord.replace(f'${macro}$', macro_value)
        message_line = message_line.replace(f'${macro}$', macro_value)
        discord_name = settings.Discord_USERNAME.replace(f'${macro}$', macro_value)
        discord_icon = settings.Discord_AVATARURL.replace(f'${macro}$', macro_value)
        ni_discord = config.NOTIFY_IMAGE_DISCORD.replace(f'${macro}$', macro_value)
        ni_line = config.NOTIFY_IMAGE_LINE.replace(f'${macro}$', macro_value)
        ni_twi = config.NOTIFY_IMAGE_TWITTER.replace(f'${macro}$', macro_value)
        ni_twidm = config.NOTIFY_IMAGE_TWITTER_DM.replace(f'${macro}$', macro_value)

    print('Message: ' + message.replace('\n', '\n         '))
    def TitleARIB_replace(ARIB):
        wawawa_dict = {
            '[字]': '🈑',
            '[新]': '🈟',
            '[手]': '🈐',
            '[双]': '🈒',
            '[デ]': '🈓',
            '[二]': '🈔',
            '[多]': '🈕',
            '[解]': '🈖',
            '[天]': '🈗',
            '[交]': '🈘',
            '[映]': '🈙',
            '[無]': '🈚',
            '[料]': '🈛',
            '[再]': '🈞',
            '[初]': '🈠',
            '[終]': '🈡',
            '[生]': '🈢',
            '[販]': '🈣',
            '[声]': '🈤',
            '[吹]': '🈥',
            '[Ｓ]': '🅂',
            '[SS]': '🅍',
            '[Ｎ]': '🄽',
            '[HV]': '🅊',
        }
        for key, value in wawawa_dict.items():
            ARIB = ARIB.replace(key, value)
        return ARIB
    message_discord = TitleARIB_replace(message_discord)
    message = TitleARIB_replace(message)
    message_line = TitleARIB_replace(message_line)
    # 送信する画像(discord)
    # パスをそのまま利用
    if (ni_discord is not None) and (os.path.isfile(ni_discord)):
        image_d = ni_discord

    # パスを取得して連結
    elif (ni_discord is not None) and (os.path.isfile(current_folder + '/' + ni_discord)):
        image_d = current_folder + '/' + ni_discord

    # 画像なし
    else:
        image_d = None

    # 送信する画像(LINE)
    # パスをそのまま利用
    if (ni_line is not None) and (os.path.isfile(ni_line)):
        image_l = ni_line

    # パスを取得して連結
    elif (ni_line is not None) and (os.path.isfile(current_folder + '/' + ni_line)):
        image_l = current_folder + '/' + ni_line

    # 画像なし
    else:
        image_l = None

    # 送信する画像(Tweet)
    # パスをそのまま利用
    if (ni_twi is not None) and (os.path.isfile(ni_twi)):
        image_t = ni_twi

    # パスを取得して連結
    elif (ni_twi is not None) and (os.path.isfile(current_folder + '/' + ni_twi)):
        image_t = current_folder + '/' + ni_twi

    # 画像なし
    else:
        image_t = None

    # 送信する画像(TwitterDM)
    # パスをそのまま利用
    if (ni_twidm is not None) and (os.path.isfile(ni_twidm)):
        image_dm = ni_twidm

    # パスを取得して連結
    elif (ni_twidm is not None) and (os.path.isfile(current_folder + '/' + ni_twidm)):
        image_dm = current_folder + '/' + ni_twidm

    # 画像なし
    else:
        image_dm = None

    if 'LINE' in config.NOTIFY_TYPE and 'LINE' not in config.FILTER_NOTIFY_TYPE:
        titlefilter_line = "1"
    elif 'LINE' not in config.NOTIFY_TYPE and 'LINE' in config.FILTER_NOTIFY_TYPE:
        titlefilter_line = "0"
    elif 'LINE' in config.NOTIFY_TYPE and 'LINE' in config.FILTER_NOTIFY_TYPE and titlefilter == "1":
        titlefilter_line = "1"
    else:
        titlefilter_line = "0"
    # LINE Notify にメッセージを送信
    if titlefilter_line == "1":

        print('-' * terminal_columns)

        line = LINE(settings.LINE_ACCESS_TOKEN)

        try:
            result_line:dict = line.sendMessage(message_line, image_path=image_l)
        except Exception as error:
            print(f'[LINE Notify] Result: Failed')
            print(f'[LINE Notify] {colorama.Fore.RED}Error: {error.args[0]}')
        else:
            if result_line['status'] != 200:
                # ステータスが 200 以外（失敗）
                print(f'[LINE Notify] Result: Failed (Code: {result_line["status"]})')
                print(f'[LINE Notify] {colorama.Fore.RED}Error: {result_line["message"]}')
            else:
                # ステータスが 200（成功）
                print(f'[LINE Notify] Result: Success (Code: {result_line["status"]})')
                print(f'[LINE Notify] Message: {result_line["message"]}')

    # Discord にメッセージを送信
    if 'Discord' in config.NOTIFY_TYPE and 'Discord' not in config.FILTER_NOTIFY_TYPE:
        titlefilter_discord = "1"
    elif 'Discord' not in config.NOTIFY_TYPE and 'Discord' in config.FILTER_NOTIFY_TYPE:
        titlefilter_discord = "0"
    elif 'Discord' in config.NOTIFY_TYPE and 'Discord' in config.FILTER_NOTIFY_TYPE and titlefilter == "1":
        titlefilter_discord = "1"
    else:
        titlefilter_discord = "0"
    if caller == "PostChgReserve" and macros["SDDOLD"] + macros["STHOLD"] + macros["STMOLD"] + macros["EDDOLD"] + macros["ETHOLD"] + macros["ETMOLD"] + macros["TitleOLD"] == macros["SDD"] + macros["STH"] + macros["STM"] + macros["EDD"] + macros["ETH"] + macros["ETM"] + macros["Title"]:
        chg1 = "0"
    else:
        chg1 = "1"
    if titlefilter_discord == "1" and chg1 == "1":

        print('-' * terminal_columns)

        discord = Discord(settings.Discord_WEBHOOK_URL)

        try:
            result_discord:dict = discord.sendMessage(message_discord, discord_name, discord_icon, image_path=image_d)
        except Exception as error:
            print(f'[Discord] Result: Failed')
            print(f'[Discord] {colorama.Fore.RED}Error: {error.args[0]}')
        else:
            if result_discord['status'] != 200 and result_discord['status'] != 204:
                # ステータスが 200 or 204 以外（失敗）
                print(f'[Discord] Result: Failed (Code: {result_discord["status"]})')
                print(f'[Discord] {colorama.Fore.RED}Error: {result_discord["message"]}')
            else:
                # ステータスが 200 or 204（成功）
                print(f'[Discord] Result: Success (Code: {result_discord["status"]})')
                print(f'[Discord] Message: {result_discord["message"]}')

    # Twitter API を初期化
    if 'Tweet' in config.NOTIFY_TYPE or 'DirectMessage' in config.NOTIFY_TYPE:

        twitter = Twitter(
            settings.TWITTER_CONSUMER_KEY,
            settings.TWITTER_CONSUMER_SECRET,
            settings.TWITTER_ACCESS_TOKEN,
            settings.TWITTER_ACCESS_TOKEN_SECRET
        )

    # Twitter にツイートを送信
    if 'Tweet' in config.NOTIFY_TYPE and 'Tweet' not in config.FILTER_NOTIFY_TYPE:
        titlefilter_tweet = "1"
    elif 'Tweet' not in config.NOTIFY_TYPE and 'Tweet' in config.FILTER_NOTIFY_TYPE:
        titlefilter_tweet = "0"
    elif 'Tweet' in config.NOTIFY_TYPE and 'Tweet' in config.FILTER_NOTIFY_TYPE and titlefilter == "1":
        titlefilter_tweet = "1"
    else:
        titlefilter_tweet = "0"
    if titlefilter_tweet == "1":

        print('-' * terminal_columns)

        # ツイートを送信
        try:
            result_tweet:dict = twitter.sendTweet(message, image_path=image_t)
        except Exception as error:
            print(f'[Tweet] Result: Failed')
            print(f'[Tweet] {colorama.Fore.RED}Error: {error.args[0]}')
        else:
            print(f'[Tweet] Result: Success')
            print(f'[Tweet] Tweet: https://twitter.com/i/status/{result_tweet["id"]}')

    # Twitter にダイレクトメッセージを送信
    if 'DirectMessage' in config.NOTIFY_TYPE and 'DirectMessage' not in config.FILTER_NOTIFY_TYPE:
        titlefilter_DirectMessage = "1"
    elif 'DirectMessage' not in config.NOTIFY_TYPE and 'DirectMessage' in config.FILTER_NOTIFY_TYPE:
        titlefilter_DirectMessage = "0"
    elif 'DirectMessage' in config.NOTIFY_TYPE and 'DirectMessage' in config.FILTER_NOTIFY_TYPE and titlefilter == "1":
        titlefilter_DirectMessage = "1"
    else:
        titlefilter_DirectMessage = "0"
    if titlefilter_DirectMessage == "1":

        print('-' * terminal_columns)

        # ダイレクトメッセージを送信
        try:
            result_directmessage:dict = twitter.sendDirectMessage(message, image_path=image_dm, destination=config.NOTIFY_DIRECTMESSAGE_TO)
        except Exception as error:
            print(f'[DirectMessage] Result: Failed')
            print(f'[DirectMessage] {colorama.Fore.RED}Error: {error.args[0]}')
        else:
            recipient_id = result_directmessage['event']['message_create']['target']['recipient_id']
            sender_id = result_directmessage['event']['message_create']['sender_id']
            print(f'[DirectMessage] Result: Success')
            print(f'[DirectMessage] Message: https://twitter.com/messages/{recipient_id}-{sender_id}')

    print('=' * terminal_columns)


if __name__ == '__main__':
    main()
