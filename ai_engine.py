"""
ĐỒ ÁN THỰC HÀNH TRÍ TUỆ NHÂN TẠO

TÊN DỰ ÁN: CHESS GAME

Tác giả: Nguyễn Anh Trọng
Mã nguồn được bảo đảm và đăng ký tại Teky Holdings

Chức năng: 
 - Triển khai lớp ChessAI để thực hiện thuật toán minimax với alpha-beta pruning trong trò chơi cờ vua.
 - Cung cấp các phương thức để tìm nước đi tối ưu cho bên trắng và bên đen trong trò chơi.
 - Đánh giá giá trị của bảng cờ cho một người chơi cụ thể.
 - Lấy giá trị của một quân cờ cụ thể theo quy tắc đánh giá.
"""

# Import các module cần thiết
import chess_engine
from enums import Player


class chess_ai:
    '''
        Class để thực hiện thuật toán minimax với alpha-beta pruning trong trò chơi cờ vua.
        - gọi hàm minimax với cắt tỉa alpha beta
        - đánh giá bảng
        - lấy giá trị của từng quân cờ
    '''
    def minimax_white(self, game_state, depth, alpha, beta, maximizing_player, player_color):
        '''
            Hàm thực hiện thuật toán minimax với alpha-beta pruning cho bên trắng.

            Parameters:
                - game_state: Trạng thái hiện tại của trò chơi.
                - depth: Độ sâu của thuật toán.
                - alpha, beta: Các giá trị alpha và beta cho alpha-beta pruning.
                - maximizing_player: True nếu đang là lượt của bên trắng, False nếu là lượt của bên đen.
                - player_color: Màu của người chơi đang xét.

            Returns:
                - Nếu depth == 3, trả về nước đi tốt nhất cho bên trắng.
                - Ngược lại, trả về giá trị đánh giá tốt nhất hoặc xấu nhất của trạng thái hiện tại.
        '''
        # Kiểm tra trạng thái game (checkmate, stalemate)
        csc = game_state.checkmate_stalemate_checker()
        if maximizing_player:
            if csc == 0:
                return 5000000
            elif csc == 1:
                return -5000000
            elif csc == 2:
                return 100
        elif not maximizing_player:
            if csc == 1:
                return 5000000
            elif csc == 0:
                return -5000000
            elif csc == 2:
                return 100

        # Kiểm tra điều kiện dừng
        if depth <= 0 or csc != 3:
            return self.evaluate_board(game_state, Player.PLAYER_1)

        # Thuật toán minimax với alpha-beta pruning
        if maximizing_player:
            max_evaluation = -10000000
            all_possible_moves = game_state.get_all_legal_moves("black")
            for move_pair in all_possible_moves:
                game_state.move_piece(move_pair[0], move_pair[1], True)
                evaluation = self.minimax_white(game_state, depth - 1, alpha, beta, False, "white")
                game_state.undo_move()

                if max_evaluation < evaluation:
                    max_evaluation = evaluation
                    best_possible_move = move_pair
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            if depth == 3:
                return best_possible_move
            else:
                return max_evaluation
        else:
            min_evaluation = 10000000
            all_possible_moves = game_state.get_all_legal_moves("white")
            for move_pair in all_possible_moves:
                game_state.move_piece(move_pair[0], move_pair[1], True)
                evaluation = self.minimax_white(game_state, depth - 1, alpha, beta, True, "black")
                game_state.undo_move()

                if min_evaluation > evaluation:
                    min_evaluation = evaluation
                    best_possible_move = move_pair
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            if depth == 3:
                return best_possible_move
            else:
                return min_evaluation
            
    # Tương tự như hàm minimax_white, nhưng cho bên đen
    def minimax_black(self, game_state, depth, alpha, beta, maximizing_player, player_color):
        csc = game_state.checkmate_stalemate_checker()
        if maximizing_player:
            if csc == 1:
                return 5000000
            elif csc == 0:
                return -5000000
            elif csc == 2:
                return 100
        elif not maximizing_player:
            if csc == 0:
                return 5000000
            elif csc == 1:
                return -5000000
            elif csc == 2:
                return 100

        if depth <= 0 or csc != 3:
            return self.evaluate_board(game_state, Player.PLAYER_2)

        if maximizing_player:
            max_evaluation = -10000000
            all_possible_moves = game_state.get_all_legal_moves("white")
            for move_pair in all_possible_moves:
                game_state.move_piece(move_pair[0], move_pair[1], True)
                evaluation = self.minimax_black(game_state, depth - 1, alpha, beta, False, "black")
                game_state.undo_move()

                if max_evaluation < evaluation:
                    max_evaluation = evaluation
                    best_possible_move = move_pair
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            if depth == 3:
                return best_possible_move
            else:
                return max_evaluation
        else:
            min_evaluation = 10000000
            all_possible_moves = game_state.get_all_legal_moves("black")
            for move_pair in all_possible_moves:
                game_state.move_piece(move_pair[0], move_pair[1], True)
                evaluation = self.minimax_black(game_state, depth - 1, alpha, beta, True, "white")
                game_state.undo_move()

                if min_evaluation > evaluation:
                    min_evaluation = evaluation
                    best_possible_move = move_pair
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            if depth == 3:
                return best_possible_move
            else:
                return min_evaluation

    def evaluate_board(self, game_state, player):
        '''
        Hàm đánh giá giá trị của bảng cờ cho một người chơi cụ thể.

        Parameters:
            - game_state: Trạng thái hiện tại của trò chơi.
            - player: Người chơi cần đánh giá (Player.PLAYER_1 hoặc Player.PLAYER_2).

        Returns:
            - Điểm đánh giá của bảng cờ cho người chơi đó.
        '''
        evaluation_score = 0
        for row in range(0, 8):
            for col in range(0, 8):
                if game_state.is_valid_piece(row, col):
                    evaluated_piece = game_state.get_piece(row, col)
                    evaluation_score += self.get_piece_value(evaluated_piece, player)
        return evaluation_score

    def get_piece_value(self, piece, player):
        '''
        Hàm lấy giá trị của một quân cờ cụ thể.

        Parameters:
            - piece: Quân cờ cần lấy giá trị.
            - player: Người chơi liên quan đến quân cờ đó (Player.PLAYER_1 hoặc Player.PLAYER_2).

        Returns:
            - Giá trị của quân cờ đó đối với người chơi cụ thể.
        '''
        if player is Player.PLAYER_1:
            if piece.is_player("black"):
                if piece.get_name() == "k":
                    return 1000
                elif piece.get_name() == "q":
                    return 100
                elif piece.get_name() == "r":
                    return 50
                elif piece.get_name() == "b":
                    return 30
                elif piece.get_name() == "n":
                    return 30
                elif piece.get_name() == "p":
                    return 10
            else:
                if piece.get_name() == "k":
                    return -1000
                elif piece.get_name() == "q":
                    return -100
                elif piece.get_name() == "r":
                    return -50
                elif piece.get_name() == "b":
                    return -30
                elif piece.get_name() == "n":
                    return -30
                elif piece.get_name() == "p":
                    return -10
        else:
            if piece.is_player("white"):
                if piece.get_name() == "k":
                    return 1000
                elif piece.get_name() == "q":
                    return 100
                elif piece.get_name() == "r":
                    return 50
                elif piece.get_name() == "b":
                    return 30
                elif piece.get_name() == "n":
                    return 30
                elif piece.get_name() == "p":
                    return 10
            else:
                if piece.get_name() == "k":
                    return -1000
                elif piece.get_name() == "q":
                    return -100
                elif piece.get_name() == "r":
                    return -50
                elif piece.get_name() == "b":
                    return -30
                elif piece.get_name() == "n":
                    return -30
                elif piece.get_name() == "p":
                    return -10