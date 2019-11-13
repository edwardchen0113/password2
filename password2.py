password = 'a123456'
i = 3
while i > 0:
	psd = input('請輸入密碼:')
	if psd == password:
		print('登錄成功！')
		break
	else:
		i = i - 1
		print('密碼錯誤！')
		if i > 0:
		    print('您還剩', i,'次機會')
		else:
			print('已錯三次！您的帳號將被鎖，請洽管理人員')