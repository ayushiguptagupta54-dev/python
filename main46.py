# import os
# if(not os.path.exists("data")):
#        os.mkdir("data")
# for i in range(0, 100):
#     os.mkdir(f"data/day{i+1}")


# Os. list
import os
folders = os.listdir("data")

print(os.getcwd())
os.chdir("/users")
print(os.getcwd())

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folders}"))


    import os
    for i in range(0, 100):
         os.rename(f"data/tutorial{i+1}", f"data/tutorial {i+1}")