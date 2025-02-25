with open("mission_1.txt" , "r") as file:
    data = file.read()
    data = data.splitlines()

print(len(data))

line_number = 1  
for line in data:
    content = line.split(":")[-1].strip()
    if "segfault" in content:
       print(f"{line_number}번째 줄!")     
    line_number += 1

target = 3420
if "segfault" in data[target]:
    parts = data[target].split(":")
    parts[-1] = "segfault{Change it!!}" 
    data[target] = " : ".join(parts)  
       
with open("mission_1.txt", "w") as file:
     file.write("\n".join(data))
    