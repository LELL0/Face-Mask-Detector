import cv2

name = 'People'

cam = cv2.VideoCapture(0)

cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("press space to take a photo", 500, 300)

img_counter = 0
f=0
f = open("imgcounter.txt","r")
img_counter = int(f.readline())
f.close()
def takePic():
    ret, frame = cam.read()
    cv2.imshow("press space to take a photo", frame)
    img_name = name +"/image_{}.jpg".format(img_counter)
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    img_counter += 1

    f = open("imgcounter.txt", "w")
    f.write(str(img_counter))
    print("exiting...")
    f.close() 
    cam.release()
    cv2.destroyAllWindows()

# while True:
#     ret, frame = cam.read()
#     if not ret:
#         print("failed to grab frame")
#         break
#     cv2.imshow("press space to take a photo", frame)
# 
#     k = cv2.waitKey(1)
#     if k%256 == 27:
#         # ESC pressed
#         print("Escape hit, closing...")
#         break
#     
#     elif k%256 == 32:
#         # SPACE pressed
#         img_name = "dataset/"+ name +"/image_{}.jpg".format(img_counter)
#         cv2.imwrite(img_name, frame)
#         print("{} written!".format(img_name))
#         img_counter += 1

