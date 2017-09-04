import numpy as np
from scipy import stats
import cv2
import os

files 	= os.listdir("Data/")
print(files)
pace 	= []
writer 	= []
for file in files:
	cap = cv2.VideoCapture("Data/" + file)

	print("Processing file " + file)
	iterator = 0
	while(True):
		iterator = iterator + 1
		
		# Capture frame-by-frame
		ret, frame = cap.read()
		if(iterator%100 == 0):
	   		if(frame is None):
	   			break
			average_color = [stats.mode(frame[:, :, i]) for i in range(frame.shape[-1])]
			average_color = [int(x) for x in average_color]
			writer.append(average_color)

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

		if(iterator%5000==0):
			print(iterator)

	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()

for i in range(100):
	pace.append(writer)

pace = np.asarray(pace)
print(pace.shape)
cv2.imwrite("ResultMode.jpg", pace)