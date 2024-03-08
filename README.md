# Projekt Akwizycji RGB

Projekt Akwizycji RGB jest aplikacją Pythona służącą do przechwytywania wartości składowych RGB z obrazu kamery i zapisywania tych danych do pliku CSV co minutę.

## Wymagania

Do działania projektu wymagana jest instalacja Pythona 3.6+ oraz następujących bibliotek:
- OpenCV-Python
- NumPy

## Instalacja

Aby zainstalować wymagane zależności, użyj poniższego polecenia:

```bash
pip install opencv-python numpy
python main.py
```

## Format logowania
```bash
Timestamp, R, G, B
2024-03-08 07:55:00, 137, 137, 127
2024-03-08 07:56:01, 137, 136, 126
...
```


