password = 'a2288218'
t = 3
while t > 0 :
    pwd = input('請輸入密碼')
    if pwd == password:
        print('恭喜,登入成功')
        break # 離開迴圈
    else:
        t = t - 1
        print('密碼輸入錯誤!')
        if t > 0:
            print('還有',t,'次機會')
        else :
            print('沒機會驗證了,帳號已被鎖')     