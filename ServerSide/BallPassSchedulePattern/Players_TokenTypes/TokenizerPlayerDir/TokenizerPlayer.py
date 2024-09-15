import sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class TokenizerPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None
        self.tokenizer_mode = "encode"  # 'encode' か 'decode' を設定
        self.vocab_dict = {}  # {ID: ボキャブラリ}
        self.reverse_vocab_dict = {}  # {ボキャブラリ: ID}

    def return_my_name(self):
        return "TokenizerPlayer"

    def main(self):
        """
        モードに応じてエンコードまたはデコードを実行
        """
        self.vocab_dict = self.one_time_world_instance.VocabularyBuilderPlayer.vocab_dict
        self.reverse_vocab_dict = self.one_time_world_instance.VocabularyBuilderPlayer.reverse_vocab_dict
        
        if self.tokenizer_mode == "encode":
            input_text = self.get_input_text()
            encoded = self.encode(input_text)
            print(f"Encoded: {encoded}")
        elif self.tokenizer_mode == "decode":
            input_ids = self.get_input_ids()
            decoded = self.decode(input_ids)
            print(f"Decoded: {decoded}")

        return "Completed"

    def get_input_text(self):
        """エンコードするための入力テキストを取得"""
        # ここで実際のテキストを取得。仮に固定のテキストとしてるけど、実際は外部から受け取ることも想定
        return "サンプル テキスト"

    def get_input_ids(self):
        """デコードするためのIDリストを取得"""
        # ここで実際のIDリストを取得。仮に固定のリストとしてるけど、実際は外部から受け取ることも想定
        return [1, 2, 3]

    def encode(self, text):
        """入力テキストをIDリストに変換（エンコード）"""
        words = text.strip().split(' ')
        return [self.reverse_vocab_dict[word] for word in words if word in self.reverse_vocab_dict]

    def decode(self, ids):
        """IDリストをテキストに変換（デコード）"""
        return ' '.join([self.vocab_dict[id] for id in ids if id in self.vocab_dict])
