import cv2

def detect_objects(image_path, cascade_path):
    # Načtení obrázku
    image = cv2.imread(image_path)

    # Načtení klasifikátoru pro rozpoznávání obličejů
    cascade = cv2.CascadeClassifier(cascade_path)

    # Převod obrázku na černobílý
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detekce objektů
    objects = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Vykreslení rámečku kolem detekovaných objektů
    for (x, y, w, h) in objects:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Zobrazení výsledného obrázku
    cv2.imshow("Detekce objektů", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Cesta k obrázku, který chceme analyzovat
image_path = "RyanReynolds.jpg"

# Cesta k souboru s klasifikátorem pro rozpoznávání obličejů
cascade_path = "haarcascade_frontalface_default.xml"

# Spuštění detekce objektů
detect_objects(image_path, cascade_path)
