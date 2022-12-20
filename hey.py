#my project is image download in online site
import requests

def Dnload_pro(a):
    First_inp = int(input("Enter a total image: "))   #Total image user input
    url_dict = {}  # This is empty dictionary

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

func_inp = input("Is the code really useful to you? If yes then write 'Yes' and if not then write 'No'.: ")
if func_inp=="Yes":
    print(Dnload_pro(func_inp))   #call function
else:
    print("Then this code will not be of any use to you, thanks.")

            
    # This my project, please check this program code and where is problem inform me
