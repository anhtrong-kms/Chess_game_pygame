class Player:
    """
    Lớp đại diện cho các người chơi và quân cờ trong trò chơi cờ vua.
    """
    PLAYER_1 = 'white'  # Biểu diễn người chơi 1 với màu trắng
    PLAYER_2 = 'black'  # Biểu diễn người chơi 2 với màu đen
    EMPTY = -9          # Biểu diễn ô trống trên bàn cờ
    PIECES = ['white_r', 'white_n', 'white_b', 'white_q', 'white_k', 'white_p',
              'black_r', 'black_n', 'black_b', 'black_q', 'black_k', 'black_p']
    """
    Danh sách các quân cờ có thể xuất hiện trên bàn cờ.
    
    Bao gồm:
    - Quân xe trắng
    - Quân mã trắng
    - Quân tượng trắng
    - Hậu trắng
    - Vua trắng
    - Quân tốt trắng
    
    - Quân xe đen
    - Quân mã đen
    - Quân tượng đen
    - Hậu đen
    - Vua đen
    - Quân tốt đen
    """