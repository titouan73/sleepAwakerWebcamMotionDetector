import cv2
import subprocess
import pyautogui

# Initialise la capture vidéo à partir de la webcam
video_capture = cv2.VideoCapture(0)

# Initialise les variables pour la détection de mouvement
motion_detected = False
prev_frame = None

while True:
    # Capture la frame courante
    ret, frame = video_capture.read()

    # Convertit la frame en niveaux de gris
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Applique un flou pour éliminer le bruit
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if prev_frame is None:
        prev_frame = gray_frame
        continue

    # Calcule la différence entre la frame courante et la frame précédente
    frame_delta = cv2.absdiff(prev_frame, gray_frame)

    # Applique un seuil pour mettre en évidence les changements
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]

    # Remplit les trous pour éviter de manquer des mouvements
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Trouve les contours de tous les objets en mouvement dans l'image
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    for c in cnts:
        # Ignore les contours de petite taille
        if cv2.contourArea(c) < 500:
            continue

        # Dessine un rectangle autour de l'objet en mouvement
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print("motion !")
        motion_detected = True

        # Envoie la commande pour sortir de veille
        subprocess.run(["xset", "dpms", "force", "on"])
        
        #fait bouger la sourie
        try:
    # Votre code utilisant pyautogui...
            pyautogui.click(100, 200)

        except pyautogui.FailSafeException:
    # Code à exécuter en cas d'activation de la fonction "Fail-Safe"
          print("Fail-Safe activé ! Arrêt des actions de pyautogui.")
        

    # Affiche la frame courante
    cv2.imshow("Webcam", frame)

    # Mise à jour de la frame précédente
    prev_frame = gray_frame

    # Attends une touche pressée pour quitter
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Libère la capture vidéo et ferme toutes les fenêtres
video_capture.release()
cv2.destroyAllWindows()