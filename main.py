import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # the logic of what we want to do goes here:
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
    # resize = resize the img
    # src = input image name/path
    # dsize = size of the output img
    # dst = stores the output img in an existing variable
    # fx = scale factore along the horizontal axis
    # fy = scale factore along the vertical axis
    # interpolation = different methods of resizing the img
    
    original_w = gray.shape[1]
    original_h = gray.shape[0]
    new_width = 120
    new_height = (new_width * original_h) // (original_w * 2)

    resized_frame = cv.resize(gray, (new_width, new_height), interpolation=cv.INTER_AREA)

    restore_frame = cv.resize(resized_frame, (original_w, original_h), interpolation=cv.INTER_NEAREST)

    # Display the resulting frame
    cv.imshow('frame', restore_frame)
    if cv.waitKey(1) == ord('q'):
        break

# when everything done, release the capture
cap.release()
cv.destroyAllWindows()