import lzma
import base64

with open("login.py", "rb") as f:
    raw = f.read()

packed = base64.b85encode(lzma.compress(raw)).decode("ascii")
print(packed)
