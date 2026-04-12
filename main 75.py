import os
files = os.lisstdir("clutteredFolder")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}.png")
        i = i + 1