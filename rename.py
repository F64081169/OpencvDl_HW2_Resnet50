import os

for i in range (1251,2501):
    if os.path.isfile("./PetImages/new_test/"+str(i+1249)+".jpg"):
        os.rename("./PetImages/new_test/"+str(i+1249)+".jpg","./PetImages/new_test/"+str(i)+".jpg")