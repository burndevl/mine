import cv2
import time

# vidio overlay
video_path = "bemines.mp4"

# Lirik menyesuaikan saran pake gemini buat cek detik liriknya
lyrics = [
    ("1", 1),
    ("2", 1),
    ("3", 1),
    ("we fall in love in October", 2),
    ("we fell in love in October", 2),
    ("that's why, i love fall", 2),
    ("Looking at the stars", 1),
    ("admiring from afar", 2),
    ("my girl, my girl, my girl", 1),
    ("you will be my girl", 2),
    ("my girl, my girl, my girl", 3),
    ("Info Template cwe :/", 5)
]

# Buka video
cap = cv2.VideoCapture(video_path)

# frame rate inisiasi
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0:
    fps = 25 

# waktu
start_time = time.time()
lyric_index = 0
current_text, duration_text = lyrics[lyric_index]

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # inisiasi posisi frame
    height, width, _ = frame.shape
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.2      # font
    thickness = 3         # jadi bold
    (text_width, text_height), _ = cv2.getTextSize(current_text, font, font_scale, thickness)
    x = (width - text_width) // 2
    y = (height + text_height) // 2

    # Overlay teks atur warna dll dsini
    warna_hitam = (0, 0, 0)
    cv2.putText(frame, current_text, (x, y), font, font_scale, warna_hitam, thickness, cv2.LINE_AA)

    # buka tab vidio
    cv2.imshow("mines template pinterst", frame)

    # if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):
    #     break

    # Update lirik sesuai durasi
    elapsed = time.time() - start_time
    if elapsed > duration_text:
        lyric_index += 1
        start_time = time.time()
        if lyric_index < len(lyrics):
            current_text, duration_text = lyrics[lyric_index]
        else:
            current_text = ""  # teks hilang kalo lyrik habis

cap.release()
cv2.destroyAllWindows()
