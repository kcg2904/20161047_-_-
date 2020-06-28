id = "aaa"
pw = 1234

a = input("아이디를 입력하세요 : ")
b = int(input("비밀번호를 입력하세요 : "))
def tf():
    if a == "aaa" and b == 1234:
        return True
    else:
        return False
print(tf())
