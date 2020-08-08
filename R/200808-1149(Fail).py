# 나름의 색상연속방지와 최소비용을 고려해서 짠 코드지만
# 2 101 100 101, 100 1 100 같은 입력은 생각지도 못함.
# 코드짠거 아까워서 그냥 깃헙올림..
house = int(input())
rgb = []
for i in range(house):
	rgb.append(list(map(int, input().split())))
	
price = 0
housecheck = 0 #rgb = '[26, 40, 83]', '[49, 60, 57]'...
rgbcheck = 0 #rgb = ['26', '40', '83'], ['49', '60', '57']...

while (house != housecheck): # 한 집씩 체크할때마다 housecheck += 1
	if housecheck == 0: # 제일 첫 집
		price += min(rgb[housecheck])
		rgbcheck = rgb[housecheck].index(min(rgb[housecheck])) #무슨 색상?
		housecheck += 1
	
	else:
		rgbcheck_s = rgb[housecheck].index(min(rgb[housecheck])) #현재 집의 색상중 가장 싼 비용
		if rgbcheck == rgbcheck_s: # 현 집의 가장 싼 비용의 색상과 전 색상이 같다면
			a = [0, 1, 2]
			del a[rgbcheck] # 현 집 색상 후보에서 전 색상 제거
			# 현 집 색상 후보 중 더 싼 색상을 고름
			if rgb[housecheck][a[0]] < rgb[housecheck][a[1]]:
				price += rgb[housecheck][a[0]]
				rgbcheck = a[0]
				housecheck += 1
			elif rgb[housecheck][a[0]] >= rgb[housecheck][a[1]]:
				price += rgb[housecheck][a[1]]
				rgbcheck = a[1]
				housecheck += 1
		else: # 현 집의 가장 싼 비용의 색상과 전 색상이 다르다면
			price += rgb[housecheck][rgbcheck_s]
			rgbcheck = rgbcheck_s
			housecheck += 1
			
print(price)
