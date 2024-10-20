import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class QRCodeMapInitializerPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.version = 2  # QRコードのバージョン
        self.grid_size = 25  # QRコードのグリッドサイズ
        self.mode_charNumInfo_checksum_bitlist = None

    def return_my_name(self):
        return "QRCodeMapInitializerPlayer"

    def main(self):
        """
        このメソッド実行直前に、
        このスーパークラスのメンバ変数
        one_time_world_instanceに、
        最新のworldインスタンスを代入しています。
        
        このメソッド終了後、
        メインで使用しているworld_instanceを
        このスーパークラスのメンバ変数
        one_time_world_instanceで上書きし、
        更新しています。
        """
        
        """ 入力 """
        self.mode_charNumInfo_checksum_bitlist = self.one_time_world_instance.checksumPlayer.mode_charNumInfo_checksum_bitlist
        
        # QRコードマップを初期化して保持
        print(f"{self.return_my_name()}が実行されました。")
        
        """ 出力 """
        self.mode_charNumInfo_checksum_bitlist # データ
        self.version # QRコードのバージョン
        self.grid_size # QRコードのグリッドサイズ
  
        
        # 自身を更新
        self.one_time_world_instance.qRCodeMapInitializerPlayer = self

        return "Completed"
