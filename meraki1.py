import json
j='{"Name":"Ram","Class":"IV","Age":9 }'
k=json.loads(j)
print(type(k))





# import json
# j={"Name":"Ram","Class":"IV","Age":9 }
# with open("sai.json","w")as file:
#     json.dump(j,file, indent=2)
