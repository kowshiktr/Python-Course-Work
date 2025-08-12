class Status2015:
    def view(self):
        print("You can view status")
    def reply(self):
        print("You can reply status")
    def caption(self):
        print("You can add caption")
        
class Status2020(Status2015):
    def uploadingImg(self):
        print("You can upload Image")
    def uploadingVid(self):
        print("you can upload video -30 sec")
    def privacy(self):
        print("You can select who see yout status")

class Status2023(Status2020):
    def ProfilePrivacy(self):
        print("You can update the profile privacy")
    def reaction(self):
        print("You can send reaction")
    def like(self):
        print("You can like status")
        
class Status2024(Status2020):
    def statusstrings(self):
        print("color is added to the status display")
    def mute(self):
        print("You can mute the other's status")
    def filters(self):
        print("You can filters")


class Status2025(Status2023,Status2024):
    def music(self):
        print("You can add music")
    def mention(self):
        print("You can mention others")
    def collob(self):
        print("You can share your status from insta or fb")
    def voicenote(self):
        print("You can voice note")
        

print("\nSheshu")
sheshu=Status2015()
sheshu.view()
sheshu.reply()
sheshu.caption()

print("\nHemanth")
hemanth=Status2020()
hemanth.uploadingImg()
hemanth.uploadingVid()
hemanth.privacy()
hemanth.view()
hemanth.reply()
hemanth.caption()

print("\nRasool")
rasool=Status2023()
rasool.uploadingImg()
rasool.uploadingVid()
rasool.privacy()
rasool.view()
rasool.reply()
rasool.caption()
rasool.ProfilePrivacy()
rasool.reaction()
rasool.like()

print("\nTarit")
tarit=Status2024()
tarit.uploadingImg()
tarit.uploadingVid()
tarit.privacy()
tarit.view()
tarit.reply()
tarit.caption()
tarit.statusstrings()
tarit.mute()
tarit.filters()

print('\nVarun')
varun=Status2025()
varun.uploadingImg()
varun.uploadingVid()
varun.privacy()
varun.view()
varun.reply()
varun.caption()
varun.statusstrings()
varun.mute()
varun.filters()
varun.ProfilePrivacy()
varun.reaction()
varun.like()
'''
output:
Sheshu
You can view status
You can reply status
You can add caption

Hemanth
You can upload Image
you can upload video -30 sec
You can select who see yout status
You can view status
You can reply status
You can add caption

Rasool
You can upload Image
you can upload video -30 sec
You can select who see yout status
You can view status
You can reply status
You can add caption
You can update the profile privacy
You can send reaction
You can like status

Tarit
You can upload Image
you can upload video -30 sec
You can select who see yout status
You can view status
You can reply status
You can add caption
color is added to the status display
You can mute the other's status
You can filters

Varun
You can upload Image
you can upload video -30 sec
You can select who see yout status
You can view status
You can reply status
You can add caption
color is added to the status display
You can mute the other's status
You can filters
You can update the profile privacy
You can send reaction
You can like status
'''

class A:
    def display_a(self):
        print("Parent class A")
class B(A):
    def display_b(self):
        print("Child Class B<-A")
a=A()
a.display_a()

b=B()
b.display_b()
b.display_a()

'''
output:
Parent class A
Child Class B<-A
Parent class A
'''

class A:
    def display_a(self):
        print("Parent class A")
class B:
    def display_b(self):
        print("Parent Class B")
class C:
    def display_c(self):
        print("Parent Class C")
class D(A,B,C):
    def display_d(self):
        print("Child Class A,B,C->D")

d=D()
d.display_a()
d.display_b()
d.display_c()
d.display_d()

'''
output:
Parent class A
Parent Class B
Parent Class C
Child Class A,B,C->D
'''

class A:
    def display_a(self):
        print("Parent class A")
class B(A):
    def display_b(self):
        print("Parent Class B")
class C(A):
    def display_c(self):
        print("Parent Class C")
class D(A):
    def display_d(self):
        print("Child Class A,B,C->D")

b=B()
b.display_b()
b.display_a()
c=C()
c.display_a()
c.display_a()
d=D()
d.display_a()
d.display_a()

'''
output:
  Parent Class B
Parent class A
Parent class A
Parent class A
Parent class A
Parent class A  
'''
