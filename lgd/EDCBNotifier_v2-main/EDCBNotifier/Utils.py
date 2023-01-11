import colorama
import datetime
import jaconv
import os
import psutil
import sys
import config


class Utils:
    """
    ユーティリティクラス
    """


    @staticmethod
    def getMacro(environ: os._Environ) -> dict:
        """
        環境変数に格納されているマクロを取得し、辞書にして返す
        environ には os.environ を渡す

        Args:
            environ (os._Environ): os.environ の値

        Returns:
            dict: マクロの値が入った辞書
        """

        # 実行時刻
        time = datetime.datetime.now()
        
        # 値が存在しなかった場合の初期値
        macro_default = '--'

        # マクロテーブル
        # 一部のみ利用できる、もしくは利用できないマクロも含む（注釈あり）
        macro_table = {

            # 標準マクロ
            'FilePath': environ.get('FilePath', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ
            'FolderPath': environ.get('FolderPath', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ
            'FileName': environ.get('FileName', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ
            'Title': environ.get('Title', macro_default),
            'Title2': environ.get('Title2', macro_default),
            'SDYYYY': environ.get('SDYYYY', macro_default),
            'SDYY': environ.get('SDYY', macro_default),
            'SDMM': environ.get('SDMM', macro_default),
            'SDM': environ.get('SDM', macro_default),
            'SDDD': environ.get('SDDD', macro_default),
            'SDD': environ.get('SDD', macro_default),
            'SDW': environ.get('SDW', macro_default),
            'STHH': environ.get('STHH', macro_default),
            'STH': environ.get('STH', macro_default),
            'STMM': environ.get('STMM', macro_default),
            'STM': environ.get('STM', macro_default),
            'STSS': environ.get('STSS', macro_default),
            'STS': environ.get('STS', macro_default),
            'EDYYYY': environ.get('EDYYYY', macro_default),
            'EDYY': environ.get('EDYY', macro_default),
            'EDMM': environ.get('EDMM', macro_default),
            'EDM': environ.get('EDM', macro_default),
            'EDDD': environ.get('EDDD', macro_default),
            'EDD': environ.get('EDD', macro_default),
            'EDW': environ.get('EDW', macro_default),
            'ETHH': environ.get('ETHH', macro_default),
            'ETH': environ.get('ETH', macro_default),
            'ETMM': environ.get('ETMM', macro_default),
            'ETM': environ.get('ETM', macro_default),
            'ETSS': environ.get('ETSS', macro_default),
            'ETS': environ.get('ETS', macro_default),
            'ONID10': environ.get('ONID10', macro_default),
            'TSID10': environ.get('TSID10', macro_default),
            'SID10': environ.get('SID10', macro_default),
            'EID10': environ.get('EID10', macro_default),
            'ONID16': environ.get('ONID16', macro_default),
            'TSID16': environ.get('TSID16', macro_default),
            'SID16': environ.get('SID16', macro_default),
            'EID16': environ.get('EID16', macro_default),
            'ServiceName': environ.get('ServiceName', macro_default),
            'SDYYYY28': environ.get('SDYYYY28', macro_default),
            'SDYY28': environ.get('SDYY28', macro_default),
            'SDMM28': environ.get('SDMM28', macro_default),
            'SDM28': environ.get('SDM28', macro_default),
            'SDDD28': environ.get('SDDD28', macro_default),
            'SDD28': environ.get('SDD28', macro_default),
            'SDW28': environ.get('SDW28', macro_default),
            'STHH28': environ.get('STHH28', macro_default),
            'STH28': environ.get('STH28', macro_default),
            'EDYYYY28': environ.get('EDYYYY28', macro_default),
            'EDYY28': environ.get('EDYY28', macro_default),
            'EDMM28': environ.get('EDMM28', macro_default),
            'EDM28': environ.get('EDM28', macro_default),
            'EDDD28': environ.get('EDDD28', macro_default),
            'EDD28': environ.get('EDD28', macro_default),
            'EDW28': environ.get('EDW28', macro_default),
            'ETHH28': environ.get('ETHH28', macro_default),
            'ETH28': environ.get('ETH28', macro_default),
            'DUHH': environ.get('DUHH', macro_default),
            'DUH': environ.get('DUH', macro_default),
            'DUMM': environ.get('DUMM', macro_default),
            'DUM': environ.get('DUM', macro_default),
            'DUSS': environ.get('DUSS', macro_default),
            'DUS': environ.get('DUS', macro_default),
            'Drops': environ.get('Drops', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ
            'Scrambles': environ.get('Scrambles', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ
            'Result': environ.get('Result', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ
            'TitleF': environ.get('TitleF', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ
            'Title2F': environ.get('Title2F', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ
            'Genre': environ.get('Genre', macro_default),  # 利用不可（RecName_Macro.dll のみ）
            'Genre2': environ.get('Genre2', macro_default),  # 利用不可（RecName_Macro.dll のみ）
            'AddKey': environ.get('AddKey', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ
            'SubTitle': environ.get('SubTitle', macro_default),  # 利用不可（RecName_Macro.dll のみ）
            'SubTitle2': environ.get('SubTitle2', macro_default),  # 利用不可（RecName_Macro.dll のみ）
            # (PostChgReserve.bat のみ？)変更前
            'TitleOLD': (environ.get('TitleOLD', macro_default)),  #[1:][:-1] 番組名（予約一覧の番組名に表示されているもの） 冒頭と末尾の引用符を削除
            'SDYYYYOLD': environ.get('SDYYYYOLD', macro_default),  # 開始日の年4桁固定
            'SDYYOLD': environ.get('SDYYOLD', macro_default),  # 開始日の年2桁固定
            'SDMMOLD': environ.get('SDMMOLD', macro_default),  # 開始日の月2桁固定
            'SDMOLD': environ.get('SDMOLD', macro_default),  # 開始日の月
            'SDDDOLD': environ.get('SDDDOLD', macro_default),  # 開始日の日2桁固定
            'SDDOLD': environ.get('SDDOLD', macro_default),  # 開始日の日
            'STHHOLD': environ.get('STHHOLD', macro_default),  # 開始時間の時2桁固定
            'STHOLD': environ.get('STHOLD', macro_default),  # 開始時間の時
            'STMMOLD': environ.get('STMMOLD', macro_default),  # 開始時間の分2桁固定
            'STMOLD': environ.get('STMOLD', macro_default),  # 開始時間の分
            'STSSOLD': environ.get('STSSOLD', macro_default),  # 開始時間の秒2桁固定
            'STSOLD': environ.get('STSOLD', macro_default),  # 開始時間の秒
            'EDYYYYOLD': environ.get('EDYYYYOLD', macro_default),  # 終了日の年4桁
            'EDYYOLD': environ.get('EDYYOLD', macro_default),  # 終了日の年2桁
            'EDMMOLD': environ.get('EDMMOLD', macro_default),  # 終了日の月2桁固定
            'EDMOLD': environ.get('EDMOLD', macro_default),  # 終了日の月
            'EDDDOLD': environ.get('EDDDOLD', macro_default),  # 終了日の日2桁固定
            'EDDOLD': environ.get('EDDOLD', macro_default),  # 終了日の日
            'ETHHOLD': environ.get('ETHHOLD', macro_default),  # 終了時間の時2桁固定
            'ETHOLD': environ.get('ETHOLD', macro_default),  # 終了時間の時
            'ETMMOLD': environ.get('ETMMOLD', macro_default),  # 終了時間の分2桁固定
            'ETMOLD': environ.get('ETMOLD', macro_default),  # 終了時間の分
            'ETSSOLD': environ.get('ETSSOLD', macro_default),  # 終了時間の秒2桁固定
            'ETSOLD': environ.get('ETSOLD', macro_default),  # 終了時間の秒
            'ONID10OLD': environ.get('ONID10OLD', macro_default),  # OriginalNetworkID 10進数
            'TSID10OLD': environ.get('TSID10OLD', macro_default),  # TransportStreamID 10進数
            'SID10OLD': environ.get('SID10OLD', macro_default),  # ServiceID 10進数
            'EID10OLD': environ.get('EID10OLD', macro_default),  # EventID 10進数
            'ONID16OLD': environ.get('ONID16OLD', macro_default),  # OriginalNetworkID 16進数
            'TSID16OLD': environ.get('TSID16OLD', macro_default),  # TransportStreamID 16進数
            'SID16OLD': environ.get('SID16OLD', macro_default),  # ServiceID 16進数
            'EID16OLD': environ.get('EID16OLD', macro_default),  # EventID 16進数
            'ServiceNameOLD': environ.get('ServiceNameOLD', macro_default),  # サービス名（予約一覧の放送局に表示されているもの）
            'SDYYYY28OLD': environ.get('SDYYYY28OLD', macro_default),  # 28時間表記開始日の年4桁固定
            'SDYY28OLD': environ.get('SDYY28OLD', macro_default),  # 28時間表記開始日の年2桁固定
            'SDMM28OLD': environ.get('SDMM28OLD', macro_default),  # 28時間表記開始日の月2桁固定
            'SDM28OLD': environ.get('SDM28OLD', macro_default),  # 28時間表記開始日の月
            'SDDD28OLD': environ.get('SDDD28OLD', macro_default),  # 28時間表記開始日の日2桁固定
            'SDD28OLD': environ.get('SDD28OLD', macro_default),  # 28時間表記開始日の日
            'STHH28OLD': environ.get('STHH28OLD', macro_default),  # 28時間表記開始時間の時2桁固定
            'STH28OLD': environ.get('STH28OLD', macro_default),  # 28時間表記開始時間の時
            'EDYYYY28OLD': environ.get('EDYYYY28OLD', macro_default),  # 28時間表記終了日の年4桁
            'EDYY28OLD': environ.get('EDYY28OLD', macro_default),  # 28時間表記終了日の年2桁
            'EDMM28OLD': environ.get('EDMM28OLD', macro_default),  # 28時間表記終了日の月2桁固定
            'EDM28OLD': environ.get('EDM28OLD', macro_default),  # 28時間表記終了日の月
            'EDDD28OLD': environ.get('EDDD28OLD', macro_default),  # 28時間表記終了日の日2桁固定
            'EDD28OLD': environ.get('EDD28OLD', macro_default),  # 28時間表記終了日の日
            'ETHH28OLD': environ.get('ETHH28OLD', macro_default),  # 28時間表記終了時間の時2桁固定
            'ETH28OLD': environ.get('ETH28OLD', macro_default),  # 28時間表記終了時間の時
            'DUHHOLD': environ.get('DUHHOLD', macro_default),  # 番組総時間の時2桁固定
            'DUHOLD': environ.get('DUHOLD', macro_default),  # 番組総時間の時
            'DUMMOLD': environ.get('DUMMOLD', macro_default),  # 番組総時間の分2桁固定
            'DUMOLD': environ.get('DUMOLD', macro_default),  # 番組総時間の分
            'DUSSOLD': environ.get('DUSSOLD', macro_default),  # 番組総時間の秒2桁固定
            'DUSOLD': environ.get('DUSOLD', macro_default),  # 番組総時間の秒
            'SDWOLD': environ.get('SDWOLD', macro_default),  # 番組総時間の秒
            # xtne6f 版で追加されたマクロ
            'BatFileTag': environ.get('BatFileTag', macro_default),  # PostRecEnd.bat と 録画後実行 bat のみ（？）
            'RecInfoID': environ.get('ReserveID', macro_default),  # PostRecEnd.bat のみ
            'ReserveID': environ.get('ReserveID', macro_default),  # PostRecEnd.bat 以外のみ
            'RecMode': environ.get('RecMode', macro_default),  # PostRecEnd.bat 以外のみ
            'ReserveComment': environ.get('ReserveComment', macro_default),  # PostRecEnd.bat 以外のみ
            'NotifyID': environ.get('NotifyID', macro_default),  # PostNotify.bat のみ

            # EDCBNotifier 独自マクロ
            'HashTag': " " + Utils.getChannelHashtag(jaconv.z2h(environ.get('ServiceName', macro_default), digit=True, ascii=True, kana=False)),
            'ChLogo': Utils.getChannellogo(jaconv.z2h(environ.get('ServiceName', macro_default), digit=True, ascii=True, kana=False)),
            'HashTagTitle': " " + Utils.getProgramHashtag(jaconv.z2h(environ.get('Title', macro_default), digit=True, ascii=True, kana=False)),
            'Titlefilter': Utils.getTitlefilter(jaconv.z2h(environ.get('Title', macro_default), digit=True, ascii=True, kana=False)),
            'channelfilter': Utils.getchannelfilter(jaconv.z2h(environ.get('ServiceName', macro_default), digit=True, ascii=True, kana=False)),
            'NotifyName': Utils.getNotifyType(environ.get('NotifyID', macro_default)),
            'ServiceNameHankaku': jaconv.z2h(environ.get('ServiceName', macro_default), digit=True, ascii=True, kana=False),
            'TitleHankaku': jaconv.z2h(environ.get('Title', macro_default), digit=True, ascii=True, kana=False),
            'Title2Hankaku': jaconv.z2h(environ.get('Title2', macro_default), digit=True, ascii=True, kana=False),
            'TimeYYYY': time.strftime('%Y'),
            'TimeYY': time.strftime('%y'),
            'TimeMM': time.strftime('%m'),
            'TimeM': str(int(time.strftime('%m'))),
            'TimeDD': time.strftime('%d'),
            'TimeD': str(int(time.strftime('%d'))),
            'TimeW': Utils.getExecutionDay(),
            'TimeHH': time.strftime('%H'),
            'TimeH': str(int(time.strftime('%H'))),
            'TimeII': time.strftime('%M'),
            'TimeI': str(int(time.strftime('%M'))),
            'TimeSS': time.strftime('%S'),
            'TimeS': str(int(time.strftime('%S'))),
            'Disksize1':  Utils.getdisksize(environ.get('FolderPath', macro_default)),
            'filesize':  Utils.getfilesize(environ.get('FilePath', macro_default)),
            'NWName':  Utils.getNetworkName(environ.get('ONID10', macro_default)),
            'Resultv2':  Utils.getResult(environ.get('Result', macro_default)),
            'EID16v2':  Utils.getEID16(environ.get('EID16', macro_default)),
            'ReserveCommentv2':  Utils.getReserveComment(environ.get('ReserveComment', macro_default)),
        }

        return macro_table


    @staticmethod
    def getChannellogo(cn: str) -> str:
        # BS・CS
        if 'NHKBS1' in cn:
            ChLogo = '<:bs1:939138467059863593>'
        elif 'NHKBSプレミアム' in cn:
            ChLogo = '<:bsp:939138659611975721>'
        elif 'BS日テレ' in cn:
            ChLogo = '<:bs4:939138806450376754>'
        elif 'BS朝日' in cn:
            ChLogo = '<:bs5:939139008263503932>'
        elif 'BS-TBS' in cn:
            ChLogo = '<:bs6:939139170335612968>'
        elif 'BSテレ東' in cn:
            ChLogo = '<:bs7:939139338573320222>'
        elif 'BSフジ' in cn:
            ChLogo = '<:bs8:939139473671880724>'
        elif 'BS11イレブン' in cn:
            ChLogo = '<:bs11:939139641154621440>'
        elif 'BS12トゥエルビ' in cn:
            ChLogo = '<:bs12:939140076175261696>'
        elif 'WOWOWプライム' in cn:
            ChLogo = '<:wow1:939162166798458900>'
        elif 'WOWOWライブ' in cn:
            ChLogo = '<:wow2:939164744873562152>'
        elif 'WOWOWシネマ' in cn:
            ChLogo = '<:wow3:939164758551166986>'
        elif 'スターチャンネル' in cn:
            ChLogo = '<:star:939165060926955520>'
        elif 'BSJapanext' in cn:
            ChLogo = '<:bs_263:1021004538674675722>'
        elif 'BSよしもと' in cn:
            ChLogo = '<:bs_265:1021003692469661768>'
        elif 'BS松竹東急' in cn:
            ChLogo = '<:bs_260:1021004536179073044>'
        elif 'カートゥーンHD' in cn:
            ChLogo = '<:cn:939143908326248448>'
        elif 'キッズステーション' in cn:
            ChLogo = '<:kids:939144555486412811>'
        elif 'AT-X' in cn:
            ChLogo = '<:atx:939144253202915338>'

        # 地デジ
        ## NHK
        elif 'NHK総合' in cn:
            ChLogo = '<:nhkg:939136923631501362>'
        elif 'NHKEテレ' in cn:
            ChLogo = '<:nhke:939137227659812924>'
        ## 民放
        ## 石川
        elif 'テレビ金沢' in cn:
            ChLogo = '<:ktk:1059420041508044830>'
        elif 'HAB' in cn:
            ChLogo = '<:hab:1059420038148399105>'
        elif 'MRO' in cn:
            ChLogo = '<:mro:1059420196193968178>'
        elif '石川テレビ' in cn:
            ChLogo = '<:itc:1059420039842889789>'
        ## 福井
        elif '福井放送' in cn:
            ChLogo = '<:fbc:1059420036646830171>'
        elif '福井テレビ' in cn:
            ChLogo = '<:ftb:1059420036646830171>'
        ## 秋田
        elif 'AKT秋田テレビ' in cn:
            ChLogo = '<:akt:1059420030258913310>'
        elif '秋田朝日放送' in cn:
            ChLogo = '<:aab:1059420026790228028>'
        elif 'ABS秋田放送' in cn:
            ChLogo = '<:abs:1059420028363083796>'
        ## 長崎
        elif 'NBC長崎放送' in cn:
            ChLogo = '<:nbc:939129960671625218>'
        elif 'テレビ長崎' in cn:
            ChLogo = '<:ktn:939132663082647572>'
        elif 'NCC長崎文化放送' in cn:
            ChLogo = '<:ncc:939133274230501457>'
        elif '長崎国際テレビ' in cn:
            ChLogo = '<:nib:939133523367985192>'
        elif '諫早お天気チャンネル' in cn:
            ChLogo = '<:3suntv:939151986824192040>'
        elif '3SUNてれび' in cn:
            ChLogo = '<:3suntv:939151986824192040>'
        ## 福岡
        elif 'KBCテレビ' in cn:
            ChLogo = '<:kbc:939137419427610636>'
        elif 'RKB毎日放送' in cn:
            ChLogo = '<:rkb:939137568962916383>'
        elif 'FBS福岡放送' in cn:
            ChLogo = '<:fbs:939137718661840957>'
        elif 'TVQ九州放送' in cn:
            ChLogo = '<:tvq:939134845114789929>'
        elif 'テレビ西日本' in cn:
            ChLogo = '<:tnc:939135089630117893>'
        ## 佐賀
        elif 'STSサガテレビ' in cn:
            ChLogo = '<:sts:939136237762121768>'
        ## 愛媛
        elif '愛媛朝日テレビ' in cn:
            ChLogo = '<:eat:939135318307774465>'
        elif '南海放送' in cn:
            ChLogo = '<:rnb:939158716501094410>'
        elif 'あいテレビ' in cn:
            ChLogo = '<:itv:939135565335494737>'
        elif 'テレビ愛媛' in cn:
            ChLogo = '<:ebc:939135748748247141>'
        ## 熊本
        elif 'RKK熊本放送' in cn:
            ChLogo = '<:rkk:939133772329254942>'
        elif 'テレビ熊本' in cn:
            ChLogo = '<:tku:939134018052554782>'
        elif 'くまもと県民' in cn:
            ChLogo = '<:kkt:939134350178549790>'
        elif 'KAB熊本朝日放送' in cn:
            ChLogo = '<:kab:939134606727319593>'
        ## 大分
        elif 'OBS大分放送' in cn:
            ChLogo = '<:obs:939136434198151168>'
        elif 'TOSテレビ大分' in cn:
            ChLogo = '<:tos:939136614586794044>'
        elif 'OAB大分朝日放送' in cn:
            ChLogo = '<:oab:939136757335748618>'
        elif 'CTBメディア' in cn:
            ChLogo = '<:ctb:1021006077468364830>'
        ## 沖縄
        elif 'RBCテレビ' in cn:
            ChLogo = '<:gr_63504_1:1021003195033587753>'
        elif '琉球朝日放送' in cn:
            ChLogo = '<:gr_63520:1021001588220899368>'
        elif '沖縄テレビ' in cn:
            ChLogo = '<:gr_63544:1021002573467095092>'
        ## 三大都市圏は網羅してるはず
        elif '日テレ' in cn:
            ChLogo = '<:ntv:1059420044569870436>'
        elif '読売テレビ' in cn:
            ChLogo = '<:ytv:939161471076667455>'
        elif '中京テレビ' in cn:
            ChLogo = '<:ctv:939160617594540054>'
        elif 'テレビ朝日' in cn:
            ChLogo = '<ex:1059420033639514182>'
        elif 'ABCテレビ' in cn:
            ChLogo = '<:abc:939161063121879071>'
        elif 'メ〜テレ' in cn:
            ChLogo = '<:nbn:939159840259985438>'
        elif 'TBS' in cn:
            ChLogo = '<:tbs:1059420128569212999>'
        elif 'MBS毎日放送' in cn:
            ChLogo = '<:mbs:939160888382984254>'
        elif 'CBCテレビ' in cn:
            ChLogo = '<:cbc:939159225236598824>'
        elif 'テレビ東京' in cn:
            ChLogo = '<:tx:1059420158776582194>'
        elif 'テレビ大阪' in cn:
            ChLogo = '<:tvo:939161774710734849>'
        elif 'テレビ愛知' in cn:
            ChLogo = '<:tva:1059422453849407518>'
        elif 'フジテレビ' in cn:
            ChLogo = '<:cx:1059420032087621642>'
        elif '関西テレビ' in cn:
            ChLogo = '<:ktv:939161275831840769>'
        elif '東海テレビ' in cn:
            ChLogo = '<:thk:939158968331288626>'
        ## 独立局
        elif 'TOKYO MX1' in cn:
            ChLogo = '<:mx:939137942000119858>'
        elif 'TOKYO MX2' in cn:
            ChLogo = '<:mx2:939138129238032405>'
        elif 'tvk' in cn:
            ChLogo = '<:tvk:939156292092694588>'
        elif 'チバテレ' in cn:
            ChLogo = '<:ctc:939156440877244436>'
        elif 'テレ玉' in cn:
            ChLogo = '<:tvs:939157894761414686>'
        elif 'とちテレ' in cn:
            ChLogo = '<:gyt:939156811125260329>'
        elif '群馬テレビ' in cn:
            ChLogo = '<:gtv:939157274897825862>'
        elif 'サンテレビ' in cn:
            ChLogo = '<:sun:939154655580143667>'
        elif 'KBS京都' in cn:
            ChLogo = '<:kbs:939154970006143086>'
        elif '奈良テレビ' in cn:
            ChLogo = '<:tvn:939155691627761695>'
        elif 'BBCびわ湖放送' in cn:
            ChLogo = '<:bbc:939156018561175593>'
        elif 'WTV' in cn:
            ChLogo = '<:wtv:939155426925244456>'
        ## CS
        elif 'BSアニマックス' in cn:
            ChLogo = '<:animax:939148615593631794>'
        elif 'ディズニーch' in cn:
            ChLogo = '<:dch:939145500312084510>'
        elif 'TBSチャンネル1' in cn:
            ChLogo = '<:tbsch1:939145238419746856>'
        elif 'TBSチャンネル2' in cn:
            ChLogo = '<:tbsch2:939144951898451969>'
        elif '日テレプラス' in cn:
            ChLogo = '<:ntvplus:939148941289742396>'
        elif 'ファミリー劇場' in cn:
            ChLogo = '<:family:939152536777130034>'
        elif 'MONDO' in cn:
            ChLogo = '<:mondo:939146805051031622>'
        elif 'テレ朝チャンネル1' in cn:
            ChLogo = '<:excs1:939146175020433430>'
        elif 'テレ朝チャンネル2' in cn:
            ChLogo = '<:excs2:939145790822178846>'
        elif 'ディズニージュニア' in cn:
            ChLogo = '<:djr:939146420773089290>'
        elif '衛星劇場' in cn:
            ChLogo = '<:eg:939147006348230656>'
        elif 'フジテレビONE' in cn:
            ChLogo = '<:cx1:939149673577447545>'
        elif 'フジテレビTWO' in cn:
            ChLogo = '<:cx2:939149427019485254>'
        elif 'フジテレビNEXT' in cn:
            ChLogo = '<:cxnext:939150038792286238>'
        elif 'Mnet' in cn:
            ChLogo = '<:mnet:939154105421664268>'
        elif 'KBS World' in cn:
            ChLogo = '<:kbs1:939147199504347157>'
        elif 'ムービープラス' in cn:
            ChLogo = '<:movieplus:939153791377358888>'

        # ハッシュタグが見つからないのでそのまま利用
        else:
            ChLogo = ''

        return ChLogo

    @staticmethod
    def getChannelHashtag(service_name: str) -> str:
        """
        チャンネル名からハッシュタグを取得する
        BS-TBS が TBS と判定されるといったことがないように、BS・CS 局を先に判定する
        service_name には半角に変換済みのチャンネル名が入るので注意
        ref: https://nyanshiba.com/blog/dtv-edcb-twitter

        Args:
            service_name (str): チャンネル名

        Returns:
            str: チャンネル名に紐づくハッシュタグ
        """

        # BS
        if 'NHKBS1' in service_name:
            hashtag = '#nhkbs1'
        elif 'NHKBSプレミアム' in service_name:
            hashtag = '#nhkbsp'
        elif 'BS日テレ' in service_name:
            hashtag = '#bsntv'
        elif 'BS朝日' in service_name:
            hashtag = '#bsasahi'
        elif 'BS-TBS' in service_name:
            hashtag = '#bstbs'
        elif 'BSテレ東' in service_name:
            hashtag = '#bstvtokyo'
        elif 'BSフジ' in service_name:
            hashtag = '#bsfuji'
        elif 'BS11イレブン' in service_name:
            hashtag = '#bs11'
        elif 'BS12トゥエルビ' in service_name:
            hashtag = '#bs12'
        elif 'WOWOWプラス' in service_name:
            hashtag = '#wowowplus'
        elif 'WOWOW' in service_name:
            hashtag = '#wowow'
        elif 'スターチャンネル' in service_name:
            hashtag = '#starchannel'
        elif 'グリーンチャンネル' in service_name:
            hashtag = '#gch'
        elif 'BSアニマックス' in service_name:
            hashtag = '#animax'
        elif 'BSスカパー!' in service_name:
            hashtag = '#bs_sptv'
        elif 'J SPORTS' in service_name:
            hashtag = '#jsports'
        elif '釣りビジョン' in service_name:
            hashtag = '#fishingvision'
        elif '日本映画専門ch' in service_name:
            hashtag = '#nihoneiga'
        elif 'ディズニーch' in service_name:
            hashtag = '#disneychannel'
        elif 'BSJapanext' in service_name:
            hashtag = '#BSjapanext'
        elif 'BSよしもと' in service_name:
            hashtag = '#bsyoshimoto'
        elif 'BS松竹東急' in service_name:
            hashtag = '#BS260ch'
        # CS
        elif 'AT-X' in service_name:
            hashtag = '#at_x'
        elif '東映チャンネル' in service_name:
            hashtag = '#toei_channel'
        elif '衛星劇場' in service_name:
            hashtag = '#eisei_gekijo'
        elif '映画・chNECO' in service_name:
            hashtag = '#chneco'
        elif 'ザ・シネマ' in service_name:
            hashtag = '#thecinema'
        elif 'ムービープラス' in service_name:
            hashtag = '#movie_plus'
        elif 'スカイA' in service_name:
            hashtag = '#skyA'
        elif 'GAORA' in service_name:
            hashtag = '#GAORA'
        elif '日テレジータス' in service_name:
            hashtag = '#Gtasu'
        elif 'SKY　STAGE' in service_name:
            hashtag = '#skystage'
        elif '時代劇専門ch' in service_name:
            hashtag = '#jidaigekich'
        elif 'ファミリー劇場' in service_name:
            hashtag = '#famigeki'
        elif 'ホームドラマch' in service_name:
            hashtag = '#Home_Drama_Ch'
        elif 'MONDO TV' in service_name:
            hashtag = '#mondotv'
        elif 'TBSチャンネル' in service_name:
            hashtag = '#TBSch'
        elif 'テレ朝チャンネル' in service_name:
            hashtag = '#tvasahich'
        elif '日テレプラス' in service_name:
            hashtag = '#nitteleplus'
        elif 'エンタメ~テレ' in service_name:
            hashtag = '#entermeitele'
        elif '銀河◆歴ドラ・サスペ' in service_name:
            hashtag = '#chginga'
        elif 'スーパー!ドラマTV' in service_name:
            hashtag = '#SuperdramaTV'
        elif 'AXN 海外ドラマ' in service_name:
            hashtag = '#axn'
        elif '女性ch/LaLa' in service_name:
            hashtag = '#lalatv'
        elif 'AXNミステリー' in service_name:
            hashtag = '#AXNMystery'
        elif 'KBS World' in service_name:
            hashtag = '#kbsworld'
        elif 'Mnet' in service_name:
            hashtag = '#Mnet'
        elif 'スペシャプラス' in service_name:
            hashtag = '#sstvplus'
        elif 'スペースシャワーTV' in service_name:
            hashtag = '#sstv'
        elif 'MTV' in service_name:
            hashtag = '#mtv'
        elif 'ミュージック・エア' in service_name:
            hashtag = '#musicair'
        elif 'エムオン!' in service_name:
            hashtag = '#musicontv'
        elif '歌謡ポップス' in service_name:
            hashtag = '#kayopops'
        elif 'カートゥーン' in service_name:
            hashtag = '#cartoonnetwork'
        elif 'キッズステーション' in service_name:
            hashtag = '#kidsstation'
        elif 'ディズニージュニア' in service_name:
            hashtag = '#disneyjunior'
        elif 'フジテレビONE' in service_name:
            hashtag = '#fujitv_one'
        elif 'フジテレビTWO' in service_name:
            hashtag = '#fujitv_two'
        elif 'フジテレビNEXT' in service_name:
            hashtag = '#fujitv_next'
        elif 'スポーツライブ+' in service_name:
            hashtag = '#sportsliveplus'

        # 地デジ
        ## NHK
        elif 'NHK総合' in service_name:
            hashtag = '#nhk'
        elif 'NHKEテレ' in service_name:
            hashtag = '#etv'
        ## 民放
        ## 北海道
        elif 'HBC北海道放送' in service_name:
            hashtag = '#hbc'
        elif '札幌テレビ' in service_name:
            hashtag = '#stv'
        elif 'HTB' in service_name:
            hashtag = '#htb'
        elif 'TVh' in service_name:
            hashtag = '#tvh'
        elif '北海道文化放送' in service_name:
            hashtag = '#uhb'
        ## 青森
        elif 'RAB青森放送' in service_name:
            hashtag = '#rab'
        elif '青森朝日放送' in service_name:
            hashtag = '#aba'
        elif 'ATV青森テレビ' in service_name:
            hashtag = '#atv'
        ## 岩手
        elif 'テレビ岩手' in service_name:
            hashtag = '#tvi'
        elif '岩手朝日テレビ' in service_name:
            hashtag = '#iat'
        elif 'IBCテレビ' in service_name:
            hashtag = '#ibc'
        elif 'めんこいテレビ' in service_name:
            hashtag = '#mit'
        ## 宮城
        elif 'TBCテレビ' in service_name:
            hashtag = '#tbc'
        elif 'ミヤギテレビ' in service_name:
            hashtag = '#mmt'
        elif '東日本放送CH' in service_name:
            hashtag = '#khb'
        elif '仙台放送' in service_name:
            hashtag = '#oxtv'
        ## 秋田
        elif 'ABS秋田放送' in service_name:
            hashtag = '#abs'
        elif '秋田朝日放送' in service_name:
            hashtag = '#aab'
        elif 'AKT秋田テレビ' in service_name:
            hashtag = '#akt'
        ## 山形
        elif '山形放送' in service_name:
            hashtag = '#ybc'
        elif '山形テレビ' in service_name:
            hashtag = '#yts'
        elif 'TUY' in service_name:
            hashtag = '#tuy'
        elif 'さくらんぼテレビ' in service_name:
            hashtag = '#saytv'
        ## 福島
        elif '福島中央テレビ' in service_name:
            hashtag = '#fct'
        elif 'KFB福島放送' in service_name:
            hashtag = '#kfb'
        elif 'テレビユー福島' in service_name:
            hashtag = '#tuf'
        elif 'FTV福島テレビ' in service_name:
            hashtag = '#ftv'
        ## 新潟
        elif 'TeNY' in service_name:
            hashtag = '#TeNY'
        elif '新潟テレビ21' in service_name:
            hashtag = '#uxtv'
        elif 'BSN' in service_name:
            hashtag = '#bsn'
        elif 'NST' in service_name:
            hashtag = '#nst'
        ## 富山
        elif 'KNBテレビ' in service_name:
            hashtag = '#knbtv'
        elif 'チューリップテレビ' in service_name:
            hashtag = '#tuliptv'
        elif '富山テレビ放送' in service_name:
            hashtag = '#toyamatv'
        ## 石川
        elif 'テレビ金沢' in service_name:
            hashtag = '#tv_kanazawa'
        elif 'HAB' in service_name:
            hashtag = '#hab'
        elif 'MRO' in service_name:
            hashtag = '#mro'
        elif '石川テレビ' in service_name:
            hashtag = '#ishikawatv'
        ## 福井
        elif '福井放送' in service_name:
            hashtag = '#fbc'
        elif '福井テレビ' in service_name:
            hashtag = '#fukuitv'
        ## 山梨
        elif '山梨放送' in service_name:
            hashtag = '#ybs'
        elif 'UTYテレビ山梨' in service_name:
            hashtag = '#uty'
        ## 長野
        elif 'テレビ信州' in service_name:
            hashtag = '#tsb'
        elif '長野朝日放送' in service_name:
            hashtag = '#abn'
        elif 'SBC信越放送' in service_name:
            hashtag = '#sbc'
        elif '長野放送' in service_name:
            hashtag = '#nbs'
        ## 静岡
        elif 'Daiichi-TV' in service_name:
            hashtag = '#SDT'
        elif '静岡朝日テレビ' in service_name:
            hashtag = '#satv'
        elif 'SBS' in service_name:
            hashtag = '#sbs'
        elif 'テレビ静岡' in service_name:
            hashtag = '#sut'
        ## 中京広域
        elif '東海テレビ' in service_name:
            hashtag = '#tokaitv'
        elif '中京テレビ' in service_name:
            hashtag = '#chukyotv'
        elif 'CBCテレビ' in service_name:
            hashtag = '#cbc'
        elif 'メ~テレ' in service_name:
            hashtag = '#nagoyatv'
        ## 中京テレ東系・独立局
        elif 'テレビ愛知' in service_name:
            hashtag = '#tva'
        elif '三重テレビ' in service_name:
            hashtag = '#mietv'
        elif 'ぎふチャン' in service_name:
            hashtag = '#gifuchan'
        ## 関西広域
        elif 'MBS毎日放送' in service_name:
            hashtag = '#mbs'
        elif 'ABCテレビ' in service_name:
            hashtag = '#abc'
        elif '読売テレビ' in service_name:
            hashtag = '#ytv'
        elif '関西テレビ' in service_name:
            hashtag = '#kantele'
        ## 関西テレ東系・独立局
        elif 'テレビ大阪' in service_name:
            hashtag = '#tvo'
        elif 'BBC琵琶湖放送' in service_name:
            hashtag = '#BBC_biwako'
        elif 'サンテレビ' in service_name:
            hashtag = '#suntv'
        elif 'KBS京都' in service_name:
            hashtag = '#kbs'
        elif '奈良テレビ' in service_name:
            hashtag = '#tvn'
        elif 'WTV' in service_name:
            hashtag = '#telewaka'
        ## 岡山香川
        elif 'RNC西日本テレビ' in service_name:
            hashtag = '#rnc'
        elif '瀬戸内海放送' in service_name:
            hashtag = '#ksb'
        elif 'ＲＳＫテレビ' in service_name:
            hashtag = '#rsk'
        elif 'TSCテレビせとうち' in service_name:
            hashtag = '#tvsetouchi'
        elif 'OHK' in service_name:
            hashtag = '#ohk'
        ## 広島
        elif 'RCCテレビ' in service_name:
            hashtag = '#rcc'
        elif '広島テレビ' in service_name:
            hashtag = '#htv'
        elif '広島ホームテレビ' in service_name:
            hashtag = '#hometv'
        elif 'テレビ新広島' in service_name:
            hashtag = '#tss'
        ## 鳥取島根
        elif '日本海テレビ' in service_name:
            hashtag = '#ｎｋｔ'
        elif 'BSSテレビ' in service_name:
            hashtag = '#bss'
        elif 'さんいん中央テレビ' in service_name:
            hashtag = '#tsk'
        ## 山口
        elif 'tysテレビ山口' in service_name:
            hashtag = '#tys'
        elif '山口放送' in service_name:
            hashtag = '#kry'
        elif 'yab山口朝日' in service_name:
            hashtag = '#yab'
        ## 徳島
        elif '四国放送' in service_name:
            hashtag = '#jrt'
        ## 愛媛
        elif '南海放送' in service_name:
            hashtag = '#rnb'
        elif '愛媛朝日テレビ' in service_name:
            hashtag = '#eat'
        elif 'あいテレビ' in service_name:
            hashtag = '#itv'
        elif 'テレビ愛媛' in service_name:
            hashtag = '#ebc'
        ## 高知
        elif '高知放送' in service_name:
            hashtag = '#rkc'
        elif 'テレビ高知' in service_name:
            hashtag = '#kutv'
        elif '高知さんさんテレビ' in service_name:
            hashtag = '#kss'
        ## 福岡
        elif 'KBCテレビ' in service_name:
            hashtag = '#kbc'
        elif 'RKB毎日放送' in service_name:
            hashtag = '#rkb'
        elif 'FBS福岡放送' in service_name:
            hashtag = '#fbs'
        elif 'TVQ九州放送' in service_name:
            hashtag = '#tvq'
        elif 'テレビ西日本' in service_name:
            hashtag = '#tnc'
        ## 佐賀
        elif 'STSサガテレビ' in service_name:
            hashtag = '#sagatv'
        ## 長崎
        elif 'NBC長崎放送' in service_name:
            hashtag = '#nbc'
        elif '長崎国際テレビ' in service_name:
            hashtag = '#nib'
        elif 'NCC長崎文化放送' in service_name:
            hashtag = '#ncc'
        elif 'テレビ長崎' in service_name:
            hashtag = '#ktn'
        ## 熊本
        elif 'RKK熊本放送' in service_name:
            hashtag = '#rkk'
        elif 'くまもと県民' in service_name:
            hashtag = '#kkt'
        elif 'KAB熊本朝日放送' in service_name:
            hashtag = '#kab'
        elif 'テレビ熊本' in service_name:
            hashtag = '#tku'
        ## 大分
        elif 'OBS大分放送' in service_name:
            hashtag = '#obs'
        elif 'TOSテレビ大分' in service_name:
            hashtag = '#tos'
        elif 'OAB大分朝日放送' in service_name:
            hashtag = '#oab'
        ## 宮崎
        elif 'MRT宮崎放送' in service_name:
            hashtag = '#mrt'
        elif 'テレビ宮崎' in service_name:
            hashtag = '#umk'
        ## 鹿児島
        elif 'MBC南日本放送' in service_name:
            hashtag = '#mbc'
        elif '鹿児島讀賣テレビ' in service_name:
            hashtag = '#kyt'
        elif 'KKB鹿児島放送' in service_name:
            hashtag = '#kkb'
        elif '鹿児島テレビ放送' in service_name:
            hashtag = '#kts'
        ## 沖縄
        elif 'RBCテレビ' in service_name:
            hashtag = '#rbc'
        elif '琉球朝日放送' in service_name:
            hashtag = '#qab'
        elif '沖縄テレビ' in service_name:
            hashtag = '#otv'
        ## 関東
        elif '日テレ' in service_name:
            hashtag = '#ntv'
        elif 'テレビ朝日' in service_name:
            hashtag = '#tvasahi'
        elif 'TBS' in service_name:
            hashtag = '#tbs'
        elif 'テレビ東京' in service_name:
            hashtag = '#tvtokyo'
        elif 'フジテレビ' in service_name:
            hashtag = '#fujitv'
        ## 関東独立局
        elif 'TOKYO MX' in service_name:
            hashtag = '#tokyomx'
        elif 'tvk' in service_name:
            hashtag = '#tvk'
        elif 'チバテレ' in service_name:
            hashtag = '#chibatv'
        elif 'テレ玉' in service_name:
            hashtag = '#teletama'
        elif '群馬テレビ' in service_name:
            hashtag = '#gtv'
        elif 'とちぎテレビ' in service_name:
            hashtag = '#tochitere'

        # ハッシュタグが見つからないのでそのまま利用
        else:
            hashtag = ''

        return hashtag

    @staticmethod
    def getProgramHashtag(program_title: str) -> str:
        """
        番組タイトルからハッシュタグを取得する
        program_title には半角に変換済みのタイトル名が入るので注意

        Args:
            title (str): 番組タイトル

        Returns:
            str: 番組タイトルに紐づくハッシュタグ
        """

        # dict 内に指定された番組タイトルが存在するか
        for hashtag_title in config.NOTIFY_HASHTAG_TITLE.keys():
            if hashtag_title in program_title:
                return config.NOTIFY_HASHTAG_TITLE[hashtag_title]

        # 存在しなかったら空文字列を返す
        return ''

    @staticmethod
    def getTitlefilter(program_title: str) -> str:

        # dict 内に指定された番組タイトルが存在するか
        for title in config.TITLE_FILTER.keys():
            if title in program_title:
                return "1"

        # 存在しなかったら空文字列を返す
        return '0'

    @staticmethod
    def getchannelfilter(channelname: str) -> str:

        # dict 内に指定されたchが存在するか
        for channel in config.CHANNEL_FILTER.keys():
            if channel in channelname:
                return "1"

        # 存在しなかったら空文字列を返す
        return '0'

    @staticmethod
    def getNotifyType(notify_id: str) -> str:
        """
        NotifyID から通知の種類を取得する

        Args:
            notify_id (str): EDCB の NotifyID

        Returns:
            str: 通知の種類
        """

        if notify_id == '1':
            notify_name = 'EPGデータ更新'
        elif notify_id == '2':
            notify_name = '予約情報更新'
        elif notify_id == '3':
            notify_name = '録画結果情報更新'
        else:
            notify_name = '更新なし'

        return notify_name


    @staticmethod
    def getExecutionTime() -> str:
        """
        EDCBNotifier の実行時刻をフォーマットして返す

        Returns:
            str: EDCBNotifier の実行時刻
        """
        return datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')


    @staticmethod
    def getExecutionDay() -> str:
        """
        EDCBNotifier の実行日を返す
        ref: https://note.nkmk.me/python-datetime-day-locale-function/

        Returns:
            str: EDCBNotifier の実行日
        """
        weeklist = ['月', '火', '水', '木', '金', '土', '日']
        return weeklist[datetime.datetime.now().weekday()]

    @staticmethod
    def getdisksize(filepath_D: str) -> str:
        """
        録画ファイルのあるドライブの空き容量を取得
        """
        GB = "GB"
        drive = filepath_D[:1] + ":\\"
        mes = filepath_D[:1] + "-FREE:"
        drive2 = config.DISK_FREE + ":\\"
        mes2 = config.DISK_FREE + "-FREE:"
        dr = filepath_D[:1]
        dr2 = config.DISK_FREE
        if os.path.exists(drive):
            disktest = mes + str('{:.2f}'.format(psutil.disk_usage(drive).free/(1024*1024*1024))) + GB
        elif os.path.exists(drive2) and ("A" == dr2 or "B" == dr2 or "C" == dr2 or "D" == dr2 or "E" == dr2 or "F" == dr2 or "G" == dr2 or "H" == dr2 or "I" == dr2 or "J" == dr2 or "K" == dr2 or "L" == dr2 or "M" == dr2 or "N" == dr2 or "O" == dr2 or "P" == dr2 or "Q" == dr2 or "R" == dr2 or "S" == dr2 or "T" == dr2 or "U" == dr2 or "V" == dr2 or "W" == dr2 or "X" == dr2 or "Y" == dr2 or "Z" == dr2):
            disktest = mes2 + str('{:.2f}'.format(psutil.disk_usage(drive2).free/(1024*1024*1024))) + GB
        elif dr2 == "None":
            disktest = ""
        else:
            disktest = ""
            # disktest = dr2 + "ドライブが接続されてないよ"

        return disktest

    @staticmethod
    def getfilesize(tsfile: str) -> str:
        """
        録画tsファイルのサイズを取得
        """
        is_file = os.path.isfile(tsfile)
        if is_file and os.path.getsize(tsfile) < 1000000000:
            filesize = " TS:" + str('{:.2f}'.format(os.path.getsize(tsfile)/(1024*1024))) + "MB"
        elif is_file and os.path.getsize(tsfile) > 1000000000:
            filesize = " TS:" + str('{:.2f}'.format(os.path.getsize(tsfile)/(1024*1024*1024))) + "GB"
        else:
            filesize = "-"

        return filesize

    @staticmethod
    def getNetworkName(ONID: str) -> str:
        if ONID == "--":
            NWN = ""
        elif ONID == 4:
            NWN = "(BS)"
        elif ONID == 6:
            NWN = "(CS1)"
        elif ONID == 7:
            NWN = "(CS2)"
        elif ONID == 10:
            NWN = "(SPHD)"
        elif 30848 <= int(ONID) <=32744:
            NWN = "(地デジ)"
        elif 64000 <= int(ONID) <=66000:
            NWN = "(CATV)"
        else:
            NWN = ""

        return NWN
    @staticmethod
    def getEID16(EID16: str) -> str:
        """
       プログラム予約の場合は(プログラム予約)、そうでない場合はEID:0x????
        """

        if EID16 in "FFFF":
            EID16 = " (プログラム予約)"
        else:
            EID16 = " EID:0x" + EID16
        return EID16

    @staticmethod
    def getReserveComment(RC: str) -> str:
        """
        先頭に半角空白を入れただけ
        """

        if RC[:7] == "EPG自動予約":
            RC = " " + RC
        else:
            RC = ""
        return RC

    @staticmethod
    def getResult(result: str) -> str:
        """
        先頭に半角空白を入れただけ
        """
        if result == "録画終了":
            result = ""
        else:
            result = " Comment:" + result
        return result

    @staticmethod
    def error(message: str) -> None:
        """
        エラーメッセージを表示して終了する

        Args:
            message (str): エラーメッセージ
        """
        print(colorama.Fore.RED + 'Error: ' + message)
        print('=' * (shutil.get_terminal_size().columns - 1))
        sys.exit(1)
