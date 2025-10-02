# library
import cv2
import time
import pygame

# run music
pygame.mixer.init()
pygame.mixer.music.load("mine.mp3")
pygame.mixer.music.play()

# Video yang mau diputar
video_path = "beminee.mp4"

# ator lirik dsni
lyrics = [
    ("3", 1),
    ("we fell in love in October", 4),
    ("that's why, i love fall", 4),
    ("Looking at the stars", 4),
    ("admiring from afar", 3),
    ("my girl, my girl, my girl", 5),
    ("you will be my girl", 4),
    ("my girl, my girl, my girl", 5),
    ("Info Template cwe :/", 5)
]

# Buka video
cap = cv2.VideoCapture(video_path)

# Ambil frame rate
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 25  # fallback

# waktu
start_time = time.time()
lyric_index = 0
current_text, duration_text = lyrics[lyric_index]

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # cek posisi frame
    height, width, _ = frame.shape
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.2      # ukuran font lebih besar
    thickness = 3         # lebih tebal = bold
    (text_width, text_height), _ = cv2.getTextSize(current_text, font, font_scale, thickness)
    x = (width - text_width) // 2
    y = (height + text_height) // 2

    # Overlay teks dengan warna hitam
    warna_hitam = (0, 0, 0)
    cv2.putText(frame, current_text, (x, y), font, font_scale, warna_hitam, thickness, cv2.LINE_AA)

    # Tampilkan video
    cv2.imshow("Iko Trend Anomali", frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):
        break

    # Update lirik sesuai durasi
    elapsed = time.time() - start_time
    if elapsed > duration_text:
        lyric_index += 1
        start_time = time.time()
        if lyric_index < len(lyrics):
            current_text, duration_text = lyrics[lyric_index]
        else:
            current_text = ""  # teks hilang setelah habis

cap.release()
cv2.destroyAllWindows()

# Stop musik setelah selesai
pygame.mixer.music.stop()
