import random

pilihan = ["batu", "gunting", "kertas"]
simbol = {
    "batu": "🪨",
    "gunting": "✂️",
    "kertas": "📄"
}

def tentukan_pemenang(pemain, ai):
    if pemain == ai:
        return "Seri!"
    elif (pemain == "batu" and ai == "gunting") or \
         (pemain == "gunting" and ai == "kertas") or \
         (pemain == "kertas" and ai == "batu"):
        return "Kamu Menang! 🎉"
    else:
        return "AI Menang! 😈"

def main():
    print("=== GAME BATU GUNTING KERTAS ===")
    print("Ketik: batu / gunting / kertas (atau ketik 'exit' untuk keluar)")

    while True:
        pemain = input("Pilihan kamu: ").lower()
        if pemain == "exit":
            print("Permainan dihentikan.")
            break
        if pemain not in pilihan:
            print("Pilihan tidak valid. Coba lagi.")
            continue

        ai = random.choice(pilihan)
        print(f"Kamu memilih: {simbol[pemain]} ({pemain})")
        print(f"AI memilih: {simbol[ai]} ({ai})")
        print(tentukan_pemenang(pemain, ai))

        lagi = input("Main lagi? (y/n): ")
        if lagi.lower() != 'y':
            print("Terima kasih sudah bermain!")
            break

main()
