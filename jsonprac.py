import json    #제이쓴 호출하기 
data = {"name" : "auftakt", "coin":1000}
jsondata = json.dumps(data) #data를 json.dumps로 받아서, 변수에 넣어주기. 
with open('uesr.txt','w') as f:
    f.write(jsondata)