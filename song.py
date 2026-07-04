import time
from threading import Thread, Lock
import sys

MAGENTA = '\033[95m'

RESET = '\033[0m'
lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write("\n")  # instead of print()
        sys.stdout.flush()

def sing_lyric(color, lyric, delay, speed):
    time.sleep(delay)
    animate_text(color + lyric + RESET, speed)

def sing_song():
    lyrics = [
    (MAGENTA, "'Cause we were just kids when we fell in love, not knowin' what it was",0.08),
    (MAGENTA, "I will not give you up this time",0.06),
    (MAGENTA, "Oh, darling, just kiss me slow, your heart is all I own",0.07),
    (MAGENTA, "And in your eyes, you're holding mine",0.06),
    (RESET, "",0.01),
    (MAGENTA, "Baby, I'm dancin' in the dark with you between my arms",0.07),
    (MAGENTA, "Barefoot on the grass while listenin' to our favourite song",0.07),
    (MAGENTA, "When you said you looked a mess, I whispered underneath my breath",0.08),
    (MAGENTA, "But you heard it, 'Darling, you look perfect tonight' <3",0.075)
]
    

    delays = [
   0.0,    # line 1

    6.3,    # after line 1 (~6s typing)
    9.0,    # after line 2 (~2.5s typing)
    13.5,   # after line 3 (~4s typing)
    14,   # after line 4 (~3s typing)

    15,   # blank line pause

    16.0,   # dancing in the dark
    21.0,   # barefoot on the grass
    26.5,   # you looked a mess
    32.5    # perfect tonight
]

    threads = []
    for i in range(len(lyrics)):
        color, lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(color, lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()