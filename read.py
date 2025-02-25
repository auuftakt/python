with open("test_file.txt" , "r") as file: #읽기 위해서는 r로 바꿔줘야한다. 그렇지 않으면 오류가 난다. 
    data = file.read()
    data = data.splitlines() #줄마다 리스트에 넣고 싶다.... 문자열이다. 개행문자를 기준으로 나눈후 리스트에넣는다.
    
print(data[2])

# 오픈을 하고 클로즈를 하는 과정이 무조건 필요한데, with/open/as file을 쓰면 된다. file은 f로 써도되고 딴거써도 됨.