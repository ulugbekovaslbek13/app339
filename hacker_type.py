import sys
import time

def hacker_print(text, tezlik=0.05):
    for harf in text:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(tezlik)
    print()

print("⚡ Kiber Animatsiya Tizimi Ishga Tushdi:\n")
gap = "System hack initiated... Access granted to junior full stack developer profil. Code running smoothly."

hacker_print(gap, 0.04)
hacker_print("\n🚀 Barcha fayllar GitHub bazasiga yuborilishga tayyor!", 0.05)