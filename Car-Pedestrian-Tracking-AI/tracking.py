import cv2

# image
img_file = "B8EM0T.jpg"
#video = cv2.VideoCapture('Tesla Autopilot Dashcam Compilation 2018 Version.mp4')
video = cv2.VideoCapture('pedestrians-compilation-online-video-cuttercom_zzkEgx35.compressed.mp4')

# Pre- trained car classifier
classifier_file = 'cars.xml'
pedestrian_classifier = 'haarcascade_fullbody.xml'


# Create Car Classifier
car_tracker = cv2.CascadeClassifier(classifier_file)
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_classifier)

# Read until the car stops
while True:

    # Read the current frame
    (read_successful, frame) = video.read()

    # Safe coding
    if read_successful:
        # Convert into gray
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # Detect Car
    detect_car = car_tracker.detectMultiScale(grayscaled_frame, 1.1, 9)
    detect_pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)
    print(detect_car, detect_pedestrians)

    # Draw rectangle around the car
    for (x, y, w, h) in detect_car:
        plate = frame[y:y + h, x:x + w]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (51, 51, 255), 2)
        cv2.rectangle(frame, (x, y - 30), (x + w, y), (51, 51, 255), -2)
        cv2.putText(frame, 'Car', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.imshow('car', plate)

    # Draw rectangle around pedestrians
    for (x, y, w, h) in detect_pedestrians:
        plate = frame[y:y + h, x:x + w]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Pedestrians', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.imshow('Pedestrians', plate)

    # display the image with car spotted
    frame = cv2.resize(frame, (700, 500))
    cv2.imshow('Car Detection System', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
print("code completed")
cv2.destroyAllWindows()




'''
# Create opencv image
img = cv2.imread(img_file)

# Convert to grayscale
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create Car Classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

# Detect Car
detect_car = car_tracker.detectMultiScale(black_n_white)
print(detect_car)

# Draw rectangle around the car
for (x, y, w, h) in detect_car:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)


# display the image with car spotted
cv2.imshow('this is a car', img)


# Prevent autoclose
cv2.waitKey()
'''
print("code completed")
