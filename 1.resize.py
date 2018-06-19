import cv2,glob

images=glob.glob("*.png")
num=1
for i in images:
    print(i)
    img=cv2.imread(i,1)
    resized_image =cv2.resize(img,(100,200))
    cv2.imwrite(i,resized_image)
    num = num + 1
cv2.destroyAllWindows()
    
