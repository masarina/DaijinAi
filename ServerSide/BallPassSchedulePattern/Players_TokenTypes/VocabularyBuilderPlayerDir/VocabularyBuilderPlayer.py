import os
import json
import sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class VocabularyBuilderPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None
        self.vocab_dict = {}  # {ID: ボキャブラリ}の辞書
        self.reverse_vocab_dict = {}  # {ボキャブラリ: ID}の辞書
        self.mode = "id_to_vocab"  # 'id_to_vocab' か 'vocab_to_id' で機能を切り替える

    def return_my_name(self):
        return "VocabularyBuilderPlayer"

    def main(self):
        """
        メインの処理を実行するメソッド。モードに応じて処理を切り替える。
        """
        vocab_file_path = self.get_vocab_file_path()
        self.load_existing_vocab(vocab_file_path)
        big_data_file = self.get_big_data_file_path()

        # モードに応じて処理を分岐
        if self.mode == "id_to_vocab":
            self.build_vocab_from_data(big_data_file)  # IDからボキャブラリを作成
        elif self.mode == "vocab_to_id":
            self.build_reverse_vocab()  # ボキャブラリからIDを作成

        self.save_vocab(vocab_file_path)
        return "Completed"

    def get_vocab_file_path(self):
        """辞書ファイルのパスを返すメソッド"""
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), "vocab.json")

    def load_existing_vocab(self, vocab_file_path):
        """既存の辞書を読み込むメソッド"""
        if os.path.exists(vocab_file_path):
            with open(vocab_file_path, 'r') as f:
                self.vocab_dict = json.load(f)
        else:
            self.vocab_dict = {}

    def get_big_data_file_path(self):
        """ビッグデータファイルのパスを返すメソッド"""
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), "big_data.txt")

    def build_vocab_from_data(self, big_data_file):
        """ビッグデータから{ID: ボキャブラリ}の辞書を構築するメソッド"""
        with open(big_data_file, 'r') as file:
            lines = file.readlines()
        
        for line in lines:
            words = line.strip().split(' ')
            for word in words:
                if word not in self.vocab_dict:
                    self.vocab_dict[word] = len(self.vocab_dict) + 1

    def build_reverse_vocab(self):
        """{ボキャブラリ: ID}の辞書を構築するメソッド"""
        self.reverse_vocab_dict = {vocab: id for id, vocab in self.vocab_dict.items()}

    def save_vocab(self, vocab_file_path):
        """更新された辞書を保存するメソッド"""
        with open(vocab_file_path, 'w') as f:
            json.dump(self.vocab_dict, f, ensure_ascii=False, indent=4)

        # 逆引き辞書も同じように保存
        reverse_vocab_file_path = vocab_file_path.replace("vocab.json", "reverse_vocab.json")
        with open(reverse_vocab_file_path, 'w') as f:
            json.dump(self.reverse_vocab_dict, f, ensure_ascii=False, indent=4)
