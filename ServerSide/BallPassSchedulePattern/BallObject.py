import copy
import sys 
sys.path.append('/etc/api_store')

class BallObject:
    """
    このクラスはWorldクラスでインスタンス化されます。
    """
    def __init__(self):
        """
        デザインパターン用
        """
        # 変数の用意
        self.now_schedule = None
        self.now_schedule_status = None
        self.schedule_mode = None  # 初期スケジュールモード
        self.index_of_schedule = 0 # 本スケジュール
        self.index_of_schedule_of_schedule = 0 # スケジュール内のスケジュール
        self.schedule_mode = "Mode_First" # 一番最初のモードを選択。
        self.schedule_dict(mode_name=self.schedule_mode) # スケジュールをセット。
        self.reset_schedule_status() # ステータスの初期化。
        
        """
        今回の本プログラミング用
        """
        # 全ての情報を格納する辞書の用意
        self.all_data_dict = {}
        
        
        """
        デバッグ用（メンバ変数は全てDebugPlayerがデバッグしてくれます。）
        """
        self.now_catch_balling_player = None
        self.next_player_name = None

    def schedule_mode_settings(self, world=None):
        """ とりあえず、実行順序を忘れないようにメモ的に実装(2024-09-18) """
        
        # トレーニングデータをダウンロード
        if self.schedule_mode == 'Mode_First':
            self.schedule_mode = 'Mode_Standby'
            
        elif self.schedule_mode == 'なんの次か未定':
            self.schedule_mode = 'Mode_QrcodeGenerator'


        else:
            print(f"{self.schedule_mode} というスケジュールモードは存在しません。BallObjectの「schedule_mode_settings」と「schedule_dict」を確認してください。")
            exit(1)


        # ifで選択されたモードのスケジュールを、メンバ変数に反映させる。
        self.schedule_dict(mode_name=self.schedule_mode)


    def reset_schedule_status(self):
        keep = copy.deepcopy(self.now_schedule)

        self.now_schedule_status = self.now_schedule
        for mini_schedule in range(len(self.now_schedule_status)):
            for players_status in range(len(self.now_schedule_status[mini_schedule])):
                self.now_schedule_status[mini_schedule][players_status] = "None"

        self.now_schedule = keep


    def schedule_dict(self,mode_name=None):
        array_2d = None
        
        if mode_name == "Mode_First":
            array_2d = [
                [['FirstPlayer']],  # 例: 第一ミニスケジュール
                [['DebugPlayer']], # Discordボットをインスタンス化
                [['FinalPlayer']]  # 例: 第三ミニスケジュール
            ]
            
        elif mode_name == "Mode_Setting":
            array_2d = [
                [['FirstPlayer']],  # 例: 第一ミニスケジュール
                [['VocabularyBuilderPlayer']], # ビッグデータtxtを読み込み、ID辞書を作成
                [['ParamsSettingPlayer']], # 各レイヤーのパラメータの設定
                [['FinalPlayer']]  # 例: 第二ミニスケジュール
            ]
            
        """ 新しいメンバーが入ってきた時の処理 """
        elif mode_name == "Mode_NewUserThenTask":
            array_2d = [
                [['FirstPlayer']],  # 例: 第一ミニスケジュール
                [['LoadToBallPlayer_By_ChannelType']], # ChannelTypeプレイヤー群の為の初期化処理
                [['LoadToBallPlayer_By_BallUpdaters']], # BallUpdaterプレイヤー群の為の初期化処理
                [['UpdateUIDPlayer']], # 
                [['LoadToBallPlayer_By_MessageType']],
                [['WelcomeNewUserPlayer']], # ウェルカムメッセージ
                [['CreateChannelPlayer']], # 新メンバーにチャンネルを作ってあげる
                [['RankUpPlayer']], # visitorからnewUserにランクアップさせる
                [['FinalPlayer']]  # 例: 第二ミニスケジュール
            ]
            
        elif mode_name == "Mode_NewMessageThenTask":
            array2d = [
                [['FirstPlayer']],
                [['LoadToBallPlayer_By_MessageType']],
                [['DaijinMessageMakePlayer']],
                [['SendMessagePlayer']],
                [['FinalPlayer']]
            ]
            
        elif mode_name == "Mode_NewChannelThenTask":
            array2d = [
                [['FirstPlayer']],
                [['LoadToBallPlayer_By_ChannelType']], # ChannelType全般の初期化
                [['ChannelCreatorCheckerPlayer']], # UIDとChIDの辞書を作る
                [['LoadToBallPlayer_By_MessageType']], # MessageType全般の初期化
                [['SendToChannelMakingUserPlayer']] # このチャンネル作成者にメッセージ。
                [['FinalPlayer']]
            ]

        elif mode_name == "end":
            print("プログラムが完了しました。確認してください。")
            exit(0)


        if array_2d == None:
            print("モードの選択が出来ませんでした。モード名を確認してください。")
            exit(1)
        
        self.now_schedule = array_2d        







