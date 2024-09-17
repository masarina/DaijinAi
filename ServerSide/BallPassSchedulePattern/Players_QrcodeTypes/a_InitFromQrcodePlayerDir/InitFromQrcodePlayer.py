import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer 

class InitFromQrcodePlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None

    def return_my_name(self):
        return "InitFromQrcodePlayer"

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
        
        → つまり、このメソッド内で
        self.one_time_world_instanceを上書きすると、
        その内容が、反映されます。
        """
        
        print(f"{return_my_name}が実行されました。")

        # データは自身のイニシャライザのメンバ変数で保持、
        # またはjsonなどに出力した場合、そのパスを保持
        self.one_time_world_instance.InitFromQrcodePlayer = self

        return "Completed"
