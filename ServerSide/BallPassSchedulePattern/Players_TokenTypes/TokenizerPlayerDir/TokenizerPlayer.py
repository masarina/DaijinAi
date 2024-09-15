import sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class TokenizerPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None
        self.tokenizer_mode = "encode"  # 'encode' か 'decode' を設定
        self.input_data = ""  # 入力するテキストまたはIDリストを保持
        self.encoded_data = []  # エンコードされたデータを保持
        self.decoded_data = ""  # デコードされたデータを保持
        # 辞書をイニシャライザで設定
        self.vocab_dict = self.one_time_world_instance.VocabularyBuilderPlayer.vocab_dict
        self.reverse_vocab_dict = self.one_time_world_instance.VocabularyBuilderPlayer.reverse_vocab_dict

    def return_my_name(self):
        return "TokenizerPlayer"

    def main(self):
        """
        モードに応じてエンコードまたはデコードを実行し、結果をメンバ変数に保持
        """
        if self.tokenizer_mode == "encode":
            self.encoded_data = self.encode(self.input_data)
            print(f"Encoded: {self.encoded_data}")
        elif self.tokenizer_mode == "decode":
            self.decoded_data = self.decode(self.input_data)
            print(f"Decoded: {self.decoded_data}")

        return "Completed"

    def encode(self, text):
        """入力テキストをIDリストに変換（エンコード）"""
        words = text.strip().split(' ')
        return [self.reverse_vocab_dict[word] for word in words if word in self.reverse_vocab_dict]

    def decode(self, ids):
        """IDリストをテキストに変換（デコード）"""
        return ' '.join([self.vocab_dict[id] for id in ids if id in self.vocab_dict])
