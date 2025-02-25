import json

with open("uesr.txt" ,"r") as f:
    data = f.read() #read 뒤에는 size가 들어간다. 
# print(data) #이건 된다. 
# print(data["name"]) #이건 오류가 생긴다. 문자열로 읽어온다는 건 통째로 그냥 들고온다는 것이기 때문에. 

dicdata = json.loads(data) #이렇게 변수를 선언해주고, 로즈로 바꾸어주면면
print(dicdata)

print(dicdata['coin']) #딕셔너리타입이된다.
