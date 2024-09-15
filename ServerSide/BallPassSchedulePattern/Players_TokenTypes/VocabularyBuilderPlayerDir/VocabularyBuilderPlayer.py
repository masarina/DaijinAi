import os
import json
import sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class VocabularyBuilderPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()  # スーパークラスの初期化メソッドを呼び出す
        self.my_name = None
        self.vocab_dict = {}  # 辞書の初期化

    def return_my_name(self):
        return "VocabularyBuilderPlayer"

    def main(self):
        """
        ビッグデータを読み込み、辞書を更新し、保存するメソッド
        """
        # 辞書のパスを指定
        vocab_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vocab.json")
        
        # 辞書の初期化または読み込み
        if os.path.exists(vocab_file_path):
            with open(vocab_file_path, 'r') as f:
                self.vocab_dict = json.load(f)  # 既存の辞書を読み込む
        else:
            self.vocab_dict = {}

        # テキストファイルの読み込み（ビッグデータ）
        big_data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "big_data.txt")
        with open(big_data_file, 'r') as file:
            lines = file.readlines()
        
        # ボキャブラリを生成
        for line in lines:
            words = line.strip().split(' ')  # 半角スペースで区切る
            for word in words:
                if word not in self.vocab_dict:
                    self.vocab_dict[word] = len(self.vocab_dict) + 1  # 新しい単語を辞書に追加

        # 更新された辞書を保存
        with open(vocab_file_path, 'w') as f:
            json.dump(self.vocab_dict, f, ensure_ascii=False, indent=4)

        return "Completed"

