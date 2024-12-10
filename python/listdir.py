import os

# current_dir = os.getcwd()
# print(f"os.listdir('python') = {os.listdir('python')}")
dir = "python"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print(f"{fullname} is a directory")
    else:
        print(f"{fullname} is a file")