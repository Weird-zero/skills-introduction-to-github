#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的数独求解程序 (Simple Sudoku Solver)
使用回溯算法求解数独问题
"""


def print_board(board):
    """打印数独棋盘"""
    print("\n" + "=" * 25)
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 25)
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
    print("=" * 25 + "\n")


def is_valid(board, row, col, num):
    """
    检查在指定位置放置数字是否有效
    
    参数:
        board: 9x9 数独棋盘
        row: 行索引
        col: 列索引
        num: 要放置的数字 (1-9)
    
    返回:
        布尔值，表示是否可以放置该数字
    """
    # 检查行
    for j in range(9):
        if board[row][j] == num:
            return False
    
    # 检查列
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # 检查3x3宫格
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    
    return True


def find_empty(board):
    """
    找到棋盘上第一个空位置（值为0的位置）
    
    返回:
        (row, col) 元组或 None
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def solve_sudoku(board):
    """
    使用回溯算法求解数独
    
    参数:
        board: 9x9 数独棋盘，空位用0表示
    
    返回:
        布尔值，表示是否成功求解
    """
    empty = find_empty(board)
    
    # 如果没有空位，说明已解决
    if empty is None:
        return True
    
    row, col = empty
    
    # 尝试数字1-9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            # 递归求解
            if solve_sudoku(board):
                return True
            
            # 回溯
            board[row][col] = 0
    
    return False


def main():
    """主函数"""
    # 示例数独问题 (0 代表空格)
    # 这是一个中等难度的数独题
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    print("原始数独题目:")
    print_board(board)
    
    print("正在求解...")
    if solve_sudoku(board):
        print("求解成功！")
        print("解答:")
        print_board(board)
    else:
        print("无解！")


if __name__ == "__main__":
    main()
