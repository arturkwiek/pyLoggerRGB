import cv2
import numpy as np
from datetime import datetime
import os


def put_text_with_background(img, text, org, font, scale, color, thickness, bgcolor):
    """Funkcja do nanoszenia tekstu z tłem dla lepszej czytelności na różnych tłach."""
    text_size = cv2.getTextSize(text, font, scale, thickness)[0]
    box_coords = ((org[0], org[1] + 5), (org[0] + text_size[0] + 5, org[1] - text_size[1] - 5))
    cv2.rectangle(img, box_coords[0], box_coords[1], bgcolor, cv2.FILLED)
    cv2.putText(img, text, org, font, scale, color, thickness)


def log_rgb_values(avg_color):
    """Funkcja do logowania wartości RGB."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_name = f"{datetime.now().strftime('%Y_%m_%d')}.csv"
    data = f"{timestamp}, R: {avg_color[2]}, G: {avg_color[1]}, B: {avg_color[0]}"

    # Sprawdzenie, czy plik już istnieje, aby zdecydować o dodaniu nagłówka
    file_exists = os.path.isfile(file_name)

    with open(file_name, 'a') as file:
        if not file_exists:
            file.write("Timestamp, R, G, B\n")
        file.write(data + "\n")

    print(f"Zapisano wartości RGB: {data}")


def capture_and_display():
    """Funkcja do przechwytywania i wyświetlania obrazu z kamery z naniesionymi wartościami RGB, logująca wartości co minutę."""
    cap = cv2.VideoCapture(0)
    last_log_time = datetime.now()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Obliczanie średnich wartości RGB dla klatki
        avg_color_per_row = np.average(frame, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        avg_color = np.round(avg_color).astype(int)

        # Sprawdzenie, czy minęła minuta od ostatniego logowania
        if (datetime.now() - last_log_time).seconds >= 60:
            log_rgb_values(avg_color)
            last_log_time = datetime.now()

        # Tekst do wyświetlenia na obrazie
        text = f"R: {avg_color[2]}, G: {avg_color[1]}, B: {avg_color[0]}"
        put_text_with_background(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, (0, 0, 0))

        cv2.imshow("Camera Output", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

capture_and_display()
