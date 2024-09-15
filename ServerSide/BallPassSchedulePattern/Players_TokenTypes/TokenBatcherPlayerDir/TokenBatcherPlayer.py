import sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class TokenBatcherPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None
        self.input_data = None  # 二次元リストの入力データ（ID化されていないトークン）
        self.batch_size = 1  # バッチサイズ
        self.output_batches = []  # バッチ処理後の出力データ

    def return_my_name(self):
        return "TokenBatcherPlayer"

    def main(self):
        """
        メインの処理：入力データをバッチサイズに応じて分割
        """
        if self.input_data:
            self.output_batches = self.batchify(self.input_data, self.batch_size)
            print(f"Batchified Output: {self.output_batches}")
        else:
            print("No input data provided!")

        return "Completed"

    def batchify(self, data, batch_size):
        """
        二次元リストをバッチサイズに応じて分割するメソッド
        """
        # バッチサイズに基づいてデータを分割する
        return [data[i:i + batch_size] for i in range(0, len(data), batch_size)]
