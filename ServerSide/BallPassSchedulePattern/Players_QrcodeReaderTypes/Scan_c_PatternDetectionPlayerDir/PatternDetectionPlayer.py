import os, sys
sys.path.append("../..")
from Players_CommonPlayers.SuperPlayerDir.SuperPlayer import SuperPlayer

class PatternDetectionPlayer(SuperPlayer):
    def __init__(self):
        super().__init__()
        self.my_name = None  # 必ずNoneで初期化
        self.patterns_detected = False  # パターン検出結果を保持

    def return_my_name(self):
        return "PatternDetectionPlayer"

    def main(self):
        """
        25x25のバイナリマトリックスからパターンを検出します。
        """
        # TrapezoidCorrectionPlayerから25x25のマトリックスを取得
        binary_matrix = self.one_time_world_instance.trapezoidCorrectionPlayer.binary_matrix_2Dlist

        # 入力データの検証
        if binary_matrix is None or len(binary_matrix) != 25 or len(binary_matrix[0]) != 25:
            raise ValueError("バイナリマトリックスが正しく取得できませんでした。")

        # パターン検出
        position_detected = self.detect_position_patterns(binary_matrix)
        alignment_detected = self.detect_alignment_pattern(binary_matrix)
        timing_detected = self.detect_timing_patterns(binary_matrix)

        # すべてのパターンが検出された場合
        if position_detected and alignment_detected and timing_detected:
            self.patterns_detected = True
            print("すべてのパターンが正常に検出されました。")
        else:
            print("パターンの検出に失敗しました。")
            if not position_detected:
                print("位置検出パターンの検出に失敗しました。")
            if not alignment_detected:
                print("アライメントパターンの検出に失敗しました。")
            if not timing_detected:
                print("タイミングパターンの検出に失敗しました。")

        # 自身を更新
        self.one_time_world_instance.patternDetectionPlayer = self

        return "Completed"

    def detect_position_patterns(self, matrix):
        """
        位置検出パターンを検出します。

        Args:
            matrix (list): 25x25のバイナリマトリックス。

        Returns:
            bool: パターンが正しく検出された場合はTrue、そうでない場合はFalse。
        """
        # 位置検出パターンの座標
        positions = [
            (0, 0),               # 左上
            (0, len(matrix)-7),   # 右上
            (len(matrix)-7, 0),   # 左下
        ]

        for (row_start, col_start) in positions:
            if not self.check_position_detection_pattern(matrix, row_start, col_start):
                return False
        return True

    def check_position_detection_pattern(self, matrix, row_start, col_start):
        """
        単一の位置検出パターンを検証します。

        Args:
            matrix (list): バイナリマトリックス。
            row_start (int): パターンの開始行。
            col_start (int): パターンの開始列。

        Returns:
            bool: パターンが正しければTrue、そうでなければFalse。
        """
        # 位置検出パターンのサイズは7x7
        pattern_size = 7
        expected_pattern = [
            [1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1],
        ]

        for i in range(pattern_size):
            for j in range(pattern_size):
                if matrix[row_start + i][col_start + j] != expected_pattern[i][j]:
                    return False
        return True

    def detect_alignment_pattern(self, matrix):
        """
        アライメントパターンを検出します。

        Args:
            matrix (list): 25x25のバイナリマトリックス。

        Returns:
            bool: パターンが正しく検出された場合はTrue、そうでない場合はFalse。
        """
        # アライメントパターンの中心座標（モデル2 バージョン2の場合）
        center_row = 19
        center_col = 19

        # アライメントパターンのサイズは5x5
        pattern_size = 5
        row_start = center_row - 2
        col_start = center_col - 2

        expected_pattern = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]

        for i in range(pattern_size):
            for j in range(pattern_size):
                if matrix[row_start + i][col_start + j] != expected_pattern[i][j]:
                    return False
        return True

    def detect_timing_patterns(self, matrix):
        """
        タイミングパターンを検出します。

        Args:
            matrix (list): 25x25のバイナリマトリックス。

        Returns:
            bool: パターンが正しく検出された場合はTrue、そうでない場合はFalse。
        """
        size = len(matrix)

        # 行方向のタイミングパターンは (6, 8) から (6, size - 9) まで
        for col in range(8, size - 8):
            expected_bit = (col % 2)
            if matrix[6][col] != expected_bit:
                return False

        # 列方向のタイミングパターンは (8, 6) から (size - 9, 6) まで
        for row in range(8, size - 8):
            expected_bit = (row % 2)
            if matrix[row][6] != expected_bit:
                return False

        return True