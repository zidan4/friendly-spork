def face_detect(path,file_name):
    img  = cv2.imread(path)
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_¬
  SCALE_IMAGE, (20,20))
    if len(rects) == 0:
    return False
    rects[:, 2:] += rects[:, :2]
# highlight the faces in the image
  for x1,y1,x2,y2 in rects:
  cv2.rectangle(img,(x1,y1),(x2,y2),(127,255,0),2)
  cv2.imwrite("%s/%s-%s" % (faces_directory,pcap_file,file_name),img)
    return True
