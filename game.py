import json
def character(name):
    character = {
        "name": name,
        "level":1,
        "hp": 100,
        "items" : [
            '없음'
        ],
        "skill": [
            "펀치",
            "피하기"
        ],
        "exp" : 0
    }
    with open("static/save.txt", 'w', encoding='utf-8') as f:
        json.dump(character, f, ensure_ascii=False ,indent=4)
    # print("{0}님 반갑습니다. (체력 {1})으로 게임을 시작합니다".format(user["name"], user["hp"]))
    return character

def save_gmae(filename, charact):
    f = open(filename, "w", encoding="utf-8")
    for key in charact:
        print("%s:%s" % (key, charact[key]))
        f.write("%s:%s\n" % (key, charact[key]))
    f.close()