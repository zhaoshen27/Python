import pygame
import random
import sys

# 初始化pygame
pygame.init()

# 游戏常量
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
GRID_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
SIDEBAR_WIDTH = 200

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 100, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GRAY = (40, 40, 40)
DARK_GRAY = (30, 30, 30)
LIGHT_BLUE = (100, 180, 255)

# 方块形状定义
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]]   # Z
]

# 方块颜色
SHAPE_COLORS = [CYAN, YELLOW, MAGENTA, ORANGE, BLUE, GREEN, RED]

class Tetromino:
    def __init__(self):
        self.shape_index = random.randint(0, len(SHAPES) - 1)
        self.shape = SHAPES[self.shape_index]
        self.color = SHAPE_COLORS[self.shape_index]
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0
    
    def rotate(self):
        # 转置矩阵并反转每一行以实现90度旋转
        rotated = [[self.shape[y][x] for y in range(len(self.shape)-1, -1, -1)] 
                  for x in range(len(self.shape[0]))]
        return rotated
    
    def draw(self, screen, x_offset, y_offset):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    rect_x = x_offset + (self.x + x) * GRID_SIZE
                    rect_y = y_offset + (self.y + y) * GRID_SIZE
                    pygame.draw.rect(screen, self.color, 
                                    (rect_x, rect_y, GRID_SIZE, GRID_SIZE))
                    pygame.draw.rect(screen, WHITE, 
                                    (rect_x, rect_y, GRID_SIZE, GRID_SIZE), 1)

class TetrisGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("俄罗斯方块")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)
        self.small_font = pygame.font.SysFont(None, 28)
        
        self.reset_game()
        
    def reset_game(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = Tetromino()
        self.next_piece = Tetromino()
        self.game_over = False
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.fall_speed = 0.5  # 方块下落的速度（秒）
        self.fall_time = 0
        
        # 计算游戏区域的位置（居中）
        self.board_x = (SCREEN_WIDTH - SIDEBAR_WIDTH - GRID_WIDTH * GRID_SIZE) // 2
        self.board_y = (SCREEN_HEIGHT - GRID_HEIGHT * GRID_SIZE) // 2
    
    def draw_grid(self):
        # 绘制游戏区域背景
        pygame.draw.rect(self.screen, DARK_GRAY, 
                        (self.board_x - 2, self.board_y - 2, 
                         GRID_WIDTH * GRID_SIZE + 4, 
                         GRID_HEIGHT * GRID_SIZE + 4))
        
        # 绘制网格线
        for x in range(GRID_WIDTH + 1):
            pygame.draw.line(self.screen, GRAY, 
                            (self.board_x + x * GRID_SIZE, self.board_y),
                            (self.board_x + x * GRID_SIZE, 
                             self.board_y + GRID_HEIGHT * GRID_SIZE))
        for y in range(GRID_HEIGHT + 1):
            pygame.draw.line(self.screen, GRAY, 
                            (self.board_x, self.board_y + y * GRID_SIZE),
                            (self.board_x + GRID_WIDTH * GRID_SIZE, 
                             self.board_y + y * GRID_SIZE))
        
        # 绘制已落下的方块
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y][x]:
                    color_idx = self.grid[y][x] - 1
                    pygame.draw.rect(self.screen, SHAPE_COLORS[color_idx], 
                                    (self.board_x + x * GRID_SIZE, 
                                     self.board_y + y * GRID_SIZE,
                                     GRID_SIZE, GRID_SIZE))
                    pygame.draw.rect(self.screen, WHITE, 
                                    (self.board_x + x * GRID_SIZE, 
                                     self.board_y + y * GRID_SIZE,
                                     GRID_SIZE, GRID_SIZE), 1)
    
            
        # 绘制侧边栏背景
        pygame.draw.rect(self.screen, DARK_GRAY, 
                        (sidebar_x - 10, self.board_y - 10, 
                         SIDEBAR_WIDTH, GRID_HEIGHT * GRID_SIZE + 20))
        
        # 绘制分数
        score_text = self.font.render(f"分数: {self.score}", True, YELLOW)
        self.screen.blit(score_text, (sidebar_x, self.board_y + 20))
        
        # 绘制等级
        level_text = self.font.render(f"等级: {self.level}", True, YELLOW)
        self.screen.blit(level_text, (sidebar_x, self.board_y + 70))
        
        # 绘制已消除行数
        lines_text = self.font.render(f"行数: {self.lines_cleared}", True, YELLOW)
        self.screen.blit(lines_text, (sidebar_x, self.board_y + 120))
        
        # 绘制下一个方块预览
        next_text = self.font.render("下一个:", True, LIGHT_BLUE)
        self.screen.blit(next_text, (sidebar_x, self.board_y + 200))
        
        # 绘制下一个方块
        preview_x = sidebar_x + 30
        preview_y = self.board_y + 250
        pygame.draw.rect(self.screen, GRAY, 
                        (preview_x - 10, preview_y - 10, 120, 120))
        
        for y, row in enumerate(self.next_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    rect_x = preview_x + x * GRID_SIZE
                    rect_y = preview_y + y * GRID_SIZE
                    pygame.draw.rect(self.screen, self.next_piece.color, 
                                    (rect_x, rect_y, GRID_SIZE, GRID_SIZE))
                    pygame.draw.rect(self.screen, WHITE, 
                                    (rect_x, rect_y, GRID_SIZE, GRID_SIZE), 1)
        
        # 绘制操作说明
        controls_y = self.board_y + 400
        controls = [
            "操作说明:",
            "← → : 左右移动",
            "↑ : 旋转",
            "↓ : 加速下落",
            "空格 : 直接落下",
            "R : 重新开始",
            "P : 暂停游戏"
        ]
        
        for i, text in enumerate(controls):
            ctrl_text = self.small_font.render(text, True, GREEN if i == 0 else WHITE)
            self.screen.blit(ctrl_text, (sidebar_x, controls_y + i * 35))
    
    def draw_game_over(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))
        
        game_over_text = self.font.render("游戏结束!", True, RED)
        score_text = self.font.render(f"最终分数: {self.score}", True, YELLOW)
        restart_text = self.font.render("按 R 键重新开始", True, GREEN)
        
        self.screen.blit(game_over_text, 
                        (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, 
                         SCREEN_HEIGHT // 2 - 60))
        self.screen.blit(score_text, 
                        (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 
                         SCREEN_HEIGHT // 2))
        self.screen.blit(restart_text, 
                        (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 
                         SCREEN_HEIGHT // 2 + 60))
    
    def draw_pause(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.screen.blit(overlay, (0, 0))
        
        pause_text = self.font.render("游戏暂停", True, YELLOW)
        continue_text = self.font.render("按 P 键继续", True, GREEN)
        
        self.screen.blit(pause_text, 
                        (SCREEN_WIDTH // 2 - pause_text.get_width() // 2, 
                         SCREEN_HEIGHT // 2 - 30))
        self.screen.blit(continue_text, 
                        (SCREEN_WIDTH // 2 - continue_text.get_width() // 2, 
                         SCREEN_HEIGHT // 2 + 30))
    
    def check_collision(self, shape, x, y):
        for row_idx, row in enumerate(shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    # 检查是否超出边界
                    if (x + col_idx < 0 or x + col_idx >= GRID_WIDTH or 
                        y + row_idx >= GRID_HEIGHT):
                        return True
                    # 检查是否与已有方块重叠
                    if y + row_idx >= 0 and self.grid[y + row_idx][x + col_idx]:
                        return True
        return False
    
    def merge_piece(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    grid_y = self.current_piece.y + y
                    if grid_y >= 0:  # 确保在网格范围内
                        self.grid[grid_y][self.current_piece.x + x] = self.current_piece.shape_index + 1
    
    def clear_lines(self):
        lines_to_clear = []
        for y in range(GRID_HEIGHT):
            if all(self.grid[y]):
                lines_to_clear.append(y)
        
        for line in lines_to_clear:
            del self.grid[line]
            self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])
        
        # 更新分数
        if lines_to_clear:
            self.lines_cleared += len(lines_to_clear)
            self.score += [100, 300, 500, 800][min(len(lines_to_clear) - 1, 3)] * self.level
            self.level = self.lines_cleared // 10 + 1
            self.fall_speed = max(0.05, 0.5 - (self.level - 1) * 0.05)
    
    def move(self, dx, dy):
        if not self.check_collision(self.current_piece.shape, 
                                  self.current_piece.x + dx, 
                                  self.current_piece.y + dy):
            self.current_piece.x += dx
            self.current_piece.y += dy
            return True
        return False
    
    def rotate_piece(self):
        rotated = self.current_piece.rotate()
        if not self.check_collision(rotated, self.current_piece.x, self.current_piece.y):
            self.current_piece.shape = rotated
            return True
        return False
    
    def hard_drop(self):
        while self.move(0, 1):
            pass
        self.merge_piece()
        self.clear_lines()
        self.current_piece = self.next_piece
        self.next_piece = Tetromino()
        
        # 检查游戏是否结束
        if self.check_collision(self.current_piece.shape, 
                              self.current_piece.x, 
                              self.current_piece.y):
            self.game_over = True
    
    def update(self, delta_time):
        if self.game_over:
            return
        
        self.fall_time += delta_time
        if self.fall_time >= self.fall_speed:
            self.fall_time = 0
            if not self.move(0, 1):
                self.merge_piece()
                self.clear_lines()
                self.current_piece = self.next_piece
                self.next_piece = Tetromino()
                
                # 检查游戏是否结束
                if self.check_collision(self.current_piece.shape, 
                                      self.current_piece.x, 
                                      self.current_piece.y):
                    self.game_over = True
    
    def run(self):
        paused = False
        
        while True:
            delta_time = self.clock.tick(60) / 1000.0  # 转换为秒
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_game()
                    
                    if self.game_over:
                        continue
                    
                    if event.key == pygame.K_p:
                        paused = not paused
                    
                    if not paused:
                        if event.key == pygame.K_LEFT:
                            self.move(-1, 0)
                        elif event.key == pygame.K_RIGHT:
                            self.move(1, 0)
                        elif event.key == pygame.K_DOWN:
                            self.move(0, 1)
                        elif event.key == pygame.K_UP:
                            self.rotate_piece()
                        elif event.key == pygame.K_SPACE:
                            self.hard_drop()
            
            # 更新游戏状态
            if not paused and not self.game_over:
                self.update(delta_time)
            
            # 绘制
            self.screen.fill(BLACK)
            self.draw_grid()
            self.current_piece.draw(self.screen, self.board_x, self.board_y)
            self.draw_sidebar()
            
            if self.game_over:
                self.draw_game_over()
            elif paused:
                self.draw_pause()
            
            pygame.display.flip()

if __name__ == "__main__":
    game = TetrisGame()
    game.run()