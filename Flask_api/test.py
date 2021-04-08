import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"likes": 78, "name" : "Nidhi", "views": 10000},
# 		{"likes": 1000, "name" : "How to make API", "views": 12300},
# 		{"likes": 54, "name" : "Nisarg", "views": 3000}]

# for i in range(len(data)):
# 	response = requests.put(BASE + "video/" + str(i), data[i])
# 	print(response.json())

# input()
# response = requests.get(BASE + "video/4")
# print(response.json())

response = requests.patch(BASE + "video/2", {})
print(response.json())