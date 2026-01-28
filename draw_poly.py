import cv2 as cv
import numpy as np

h, w = 600, 800

main_image = np.zeros((h, w, 3), dtype="uint8")

drawing = 0
ix = 0
iy = 0
# Adding Function Attached To Mouse Callback
def draw(event,x,y,flags,params):
    global ix,iy,drawing
    # Left Mouse Button Down Pressed (for Drawing)
    if event==cv.EVENT_LBUTTONDOWN:
        drawing = 1
        ix = x
        iy = y

    # Righ Mouse Button Down Pressed (for Erasing)
    if event==cv.EVENT_RBUTTONDOWN:
        drawing = 2
        ix = x
        iy = y

    if event==cv.EVENT_MOUSEMOVE:
        if drawing==1:
            #For Drawing Line
            cv.line(main_image,pt1=(ix,iy),pt2=(x,y),color=(255,255,255),thickness=1)
            ix = x
            iy = y
        elif drawing==2:
            #For Drawing Line
            cv.line(main_image,pt1=(ix,iy),pt2=(x,y),color=(0,0,0),thickness=10)
            ix = x
            iy = y
        
    if event==cv.EVENT_LBUTTONUP or event==cv.EVENT_RBUTTONUP:
        drawing = 0

cv.namedWindow("Window")

# Adding Mouse CallBack Event
cv.setMouseCallback("Window",draw)

def nothing(x): pass

cv.namedWindow("Elements")
cv.createTrackbar('approx val', 'Elements', 1, 50, nothing)
# cv.CHAIN_APPROX_NONE, cv.CHAIN_APPROX_SIMPLE, cv.CHAIN_APPROX_TC89_L1, cv.CHAIN_APPROX_TC89_KCOS
cv.createTrackbar('chain', 'Elements', 1, 4, nothing) 
cv.createTrackbar('acc type', 'Elements', 0, 1, nothing)
cv.createTrackbar('approx type', 'Elements', 0, 1, nothing)

thickness = 1
chain_type_list = ["CHAIN APPROX NONE", "CHAIN APPROX SIMPLE", "CHAIN APPROX TC89 L1", "CHAIN APPROX TC89 KCOS"]
border = 30

while True:
    cv.imshow("Window", main_image)
    
    # image1 = np.zeros_like(main_image)
    # image2 = np.zeros_like(main_image)
    image1 = np.zeros((h+border, w, 3), dtype="uint8")
    image2 = np.zeros((h+border, w, 3), dtype="uint8")

    app_val = cv.getTrackbarPos('approx val', 'Elements')
    chain_type = cv.getTrackbarPos('chain', 'Elements')
    acc_type = cv.getTrackbarPos('acc type', 'Elements')
    app_type = cv.getTrackbarPos('approx type', 'Elements')   

    if app_val == 0:
        app_val = 1
    app_val = app_val**2 / 5000
    if chain_type == 0:
        chain_type = 1


    gray = cv.cvtColor(main_image, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

    contours1, hierarchy1 = cv.findContours(thresh.copy(), cv.RETR_LIST, chain_type)
    for cnt1 in contours1:
        acc = app_val * cv.arcLength(cnt1, acc_type)
        approx1 = cv.approxPolyDP(cnt1, acc, app_type)
        cv.drawContours(image1[border:], [approx1], 0, (0,255,0), thickness)


    contours2, hierarchy2 = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, chain_type)
    for cnt2 in contours2:
        acc = app_val * cv.arcLength(cnt2, acc_type)
        approx2 = cv.approxPolyDP(cnt2, acc, app_type)
        cv.drawContours(image2[border:], [approx2], 0, (0,255,0), thickness)

    old_h, old_w, _ = image1.shape
    new_h, new_w = 3*old_h//4, 3*old_w//4
    new_image = np.zeros((2*new_h+border, new_w, 3))


    image1 = cv.resize(image1, (new_w, new_h))
    image2 = cv.resize(image2, (new_w, new_h))
    cv.putText(image1, "INTERNAL", [10,15], cv.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
    cv.putText(image2, "EXTERNAL", [10,15], cv.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

    new_image[border:new_h+border,:,:] = image1
    new_image[new_h+border:,:,:] = image2

    text = f"{chain_type_list[chain_type-1]}, approx value: {app_val}"
    cv.putText(new_image, text, [10,15], cv.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

    cv.imshow("Result", new_image)
    if cv.waitKey(1) & 0xFF ==27:
        cv.destroyAllWindows()
        break


