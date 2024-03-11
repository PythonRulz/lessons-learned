import requests

class Post:
    def __init__(self):
        self.id = []
        self.get_response()
        
        

    def get_response(self):
        
        response = requests.get("https://api.npoint.io/c9dfefe145f500bbe081").json()
        for blog in response:
            self.id.append(blog['title'])
            for k, v in blog.items():
                print(k)
                print(v)

data = Post()
print(data.id)
