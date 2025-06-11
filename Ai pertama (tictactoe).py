import random

board = [" " for _ in range(9)]

def tampilkan_papan():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def cek_menang(pemain):
    kombinasi = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # baris
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # kolom
        [0, 4, 8], [2, 4, 6]              # diagonal
    ]
    for combo in kombinasi:
        if all(board[i] == pemain for i in combo):
            return True
    return False

def pemain_move():
    while True:
        try:
            posisi = int(input("Pilih posisi (1-9): ")) - 1
            if board[posisi] == " ":
                board[posisi] = "X"
                break
            else:
                print("Sudah diisi! Pilih yang lain.")
        except:
            print("Masukkan angka 1-9!")

def ai_move():
    kosong = [i for i, val in enumerate(board) if val == " "]
    if kosong:
        posisi = random.choice(kosong)
        board[posisi] = "O"

def main():
    print("=== TIC TAC TOE ===")
    tampilkan_papan()

    while True:
        pemain_move()
        tampilkan_papan()
        if cek_menang("X"):
            print("Kamu menang! 🎉")
            break
        if " " not in board:
            print("Seri!")
            break

        print("Giliran AI...")
        ai_move()
        tampilkan_papan()
        if cek_menang("O"):
            print("AI menang! 😈")
            break
        if " " not in board:
            print("Seri!")
            break

main()