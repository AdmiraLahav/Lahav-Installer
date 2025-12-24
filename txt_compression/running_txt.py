import lzma
import base64

PAYLOAD = """"""

code_bytes = lzma.decompress(base64.b85decode(PAYLOAD))
exec(code_bytes.decode("utf-8"), {"__name__": "__main__"})


print("HERE IS -------3")