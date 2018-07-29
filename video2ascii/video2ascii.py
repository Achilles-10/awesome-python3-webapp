def video2imgs(video,size):
	"""

	:param video: video file's path
	:param size: tuple of images' width and height
	:return: a list of images
	"""
	import cv2

	img_list = []

	cap = cv2.VideoCapture(video)

	while cap.isOpened():
		ret, frame = cap.read()
		if ret:
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			img = cv2.resize(gray,size,interpolation=cv2.INTER_AREA)

			img_list.append(img)
		else:
			break

	cap.release()

	return img_list

if __name__ == '__main__':
	imgs = video2imgs()

