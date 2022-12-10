import requests

First_inp = int(input("Enter a total image: "))   #this is total image user input

# This is empty dictionary
url_dict = {}

# This loop is input 
for i in range (1, First_inp+1):
    img_name = input("Please image name here: ")
    img_url = input("Please 'copy image address' here: ")
    url_dict[img_name]=img_url

# This loop is dict key and value different variable
for x, y in url_dict.items():
    r = requests.get(y) #This url var is y  

    with open(x, "wb") as f: #This is print the name and url hit , then output at download image
        f.write(r.content)
        
# This my project, please check this program and where is problem inform me