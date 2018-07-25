import re
import requests
import os


def getHtml(url, code='utf-8'):
	try:
		r = requests.get(url, timeout=5)
		r.raise_for_status()
		r.encoding = code
		return r.text
	except:
		return ""


def downloadPic(html, keyword, root, num):
	count = num * 60
	pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
	for each in pic_url:
		count +=1
		fpath = root + keyword + str(count) + '.jpg'
		print("正在下载第" + str(count) + "张图片")
		try:
			pic = requests.get(each, timeout=5)
		except requests.exceptions.ConnectionError:
			print("【错误】当前图片无法下载")
			continue
		with open(fpath, 'wb') as f:
			f.write(pic.content)
			f.close()
			print("第" + str(count) + "张图保存成功")


def main():
	word = input("Input keyword: ")
	number = eval(input("How many pics do you want:(x60) "))-1
	num = int(number / 60)
	root = "D://testpic//"
	if not os.path.exists(root):
		os.mkdir(root)
	start_url = "https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="
	print("找到关键词:", word, "的图片， 现在开始下载...")
	for i in range(num+1):
		url = start_url + word + "&pn=" + str(
				i * 20) + "&gsm=3c&ct=&ic=0&lm=-1&width=0&height=0"
		html = getHtml(url)
		downloadPic(html, word, root, i)


main()