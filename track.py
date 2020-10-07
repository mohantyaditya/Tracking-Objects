import cv2

cap = cv2.VideoCapture('6.mp4')
cap.set(cv2.CAP_PROP_POS_FRAMES, 500)


for i in range(10):
    success,frame = cap.read()

if not success:
    exit(1)

frame_h,frame_w = frame.shape[:2]
size = (frame_h,frame_w)

w =frame_w//8
h =frame_h//8
x =600
y =320
track_window = (x,y,w,h)

roi =frame[y:y+h, x-w:x]
hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
mask = None
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

term_criteria =(cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS,10,1)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

result = cv2.VideoWriter('car1211.mp4',fourcc,10,(int(cap.get(3)),int(cap.get(4))))

true,frame = cap.read()
while true:
    hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    back_project = cv2.calcBackProject([hsv], [0],roi_hist, [0,180],1)

    num_iters,track_window = cv2.meanShift(back_proj,track_window,term_criteria)

    x,y,w,h = track_window
    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('back-projection',back_project)


    cv2.imshow('meanshift', frame)
    result.write(frame)


    k = cv2.waitKey(50)
    if k == 27:
        break
    if k == ord('p'):
        cv2.waitKey(-1)

#cv2.destroyAllWindows()

    true,frame = cap.read()
