extensions = input("Insert File Type:" ).lower()

if extensions.endswith(".jpeg"):
    print("image/jpeg")
elif extensions.endswith(".jpg"):
    print("image/jpg")
elif extensions.endswith(".gif"):
    print("image/gif")
elif extensions.endswith(".png"):
    print("image/png")
elif extensions.endswith(".pdf"):
    print("application/pdf")
elif extensions.endswith(".txt"):
    print("text/plain")
elif extensions.endswith(".zip"):
    print("application/x-zip-compressed")
else:
    print("application/octet-stream")