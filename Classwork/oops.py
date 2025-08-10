
class Instagram:
    def addingUsername(self,username):
        print(f"{username}is added")
    def uploadPost(self,name,posturl):
        print(f"Added the {posturl}")
taruni=Instagram()
sirisha=Instagram()
sheshu=Instagram()
adhitya=Instagram()
kowshik=Instagram()
taruni.uploadPost("taruni","dsgshshj.png")
sirisha.uploadPost("sirisha","hguigigig.png")
sheshu.uploadPost("sheshu","uiihihuv.png")
adhitya.uploadPost("adhitya","tttuiuii.png")
kowshik.uploadPost("kowshik","marvek.png")

taruni.addingUsername("Taruni")
sirisha.addingUsername("Sirisha")

'''
output:
Added the dsgshshj.png
Added the hguigigig.png
Added the uiihihuv.png
Added the tttuiuii.png
Added the marvek.png
Taruniis added
Sirishais added
'''

class Shopping:
    discount=10
    cat=['men','women','footware','electronics']
    def placeorder(self,product):
        self.product=product
        print("order is placed")
        @classmethod
        def updatediscount(cls,upd_dis):
            cls.discount=upd_dis
    
            print("discount is updated")

        @staticmethod
        def formatdiscount(discount):
            print(f"{discount}%discount is availble.shop now!!!")
            
        
kowshik=Shopping()


kowshik.placeorder("phone")


kowshik.updatediscount(15)
'''

output:
Welcome to the instagram
HelloManikanta login successfull
Bio: 
Post: []
Followers: []
Following: []
Username: Manikanta
Password: mani@1234!
updated Password: None
'''

class Instagram:
    def __init__(self,username,password):
        print("Welcome to the instagram")
        self.bio=''
        self.post=[]
        self.followers=[]
        self.following=[]
        self.username=username
        self._password=password
        print(f"Hello{self.username} login successfull")
    @property
    def externalbio(self):
        return self.bio

    @externalbio.setter
    def externalbio(self, new_bio):
        self.bio=upd_bio

    def show_Password(self):
        return self._password
    def updatePassword(self,new_pwd):
        self._password=new_pwd
manikanta=Instagram("Manikanta","mani@1234!")
print("Bio:",manikanta.bio)
print("Post:",manikanta.post)
print("Followers:",manikanta.followers)
print("Following:",manikanta.following)
print("Username:",manikanta.username)

manikanta.bio="peace"
manikanta.post.append("python-course.png")
manikanta.followers.extend(["Adithya","Shanmuk","Kiran"])
manikanta.following.extend(["jrntr","virat","klrahul"])
manikanta.username="manikanta_."
print("\nAfter upadting:")
print("Bio:",manikanta.bio)
print("Post:",manikanta.post)
print("Followers:",manikanta.followers)
print("Following:",manikanta.following)
print("Username:",manikanta.username)

print("\nPassword:", manikanta.show_Password())
print("updated Password:",manikanta.updatePassword("mani@12"))
'''
output:
Welcome to the instagram
HelloManikanta login successfull
Bio:
Post: []
Followers: []
Following: []
Username: Manikanta

After upadting:
Bio: peace
Post: ['python-course.png']
Followers: ['Adithya', 'Shanmuk', 'Kiran']
Following: ['jrntr', 'virat', 'klrahul']
Username: manikanta_.

Password: mani@1234!
updated Password: None


'''
class Login:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self._otp=1234
        
    def getpassword(self):
        return self.__password
    def updatePassword(self,new_pwd):
        self.__password=new_pwd
    @property
    def publicotp(self):
        return self._otp
    
    @publicotp.setter
    def publicotp(self,new_otp):
        self._otp=new_otp
vikash=Login("vikash","vikash@1234")
print("username",vikash.username)

print("password",vikash.getpassword())
print("OTP",vikash.publicotp)
vikash.username="_vikash_"
print("Updated username",vikash.username)

vikash.updatePassword("vk@18")
print("Updated password",vikash.getpassword())
vikash.publicotp=1111
print("Update OTP",vikash.publicotp)
'''
output:
username vikash
password vikash@1234
OTP 1234
Updated username _vikash_
Updated password vk@18
Update OTP 1111
'''

        




    
