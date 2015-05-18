#-*- coding:utf-8-*-
import jieba
from numpy import *
from numpy.linalg import *
from scipy import *
from pickle import *

def get_id(stem):
    s = stem.encode('gbk')
    if s in term:
    	return term[s]
    else:
    	return -1

def getq(query):
    qlist = jieba.cut(query)
    qlen = len(term)+1
    print qlen
    q = zeros((1,qlen))
    print q
    for w in qlist:
        i = get_id(w)
        print i
        if (i>=0):
            q[0][i]=q[0][i]+1
    q=log10(q+1)
    return q

def getcos(mat,qr):
    d = mat.shape[1]
    cos = []
    for i in range(d):
        d_n=norm(mat[:,i],ord=2)
        q_n=norm(qr,ord=2)
        if (d_n*q_n>0):
            cos.append([dot(mat[:,i],qr)/(d_n*q_n),i])
    cos=sorted(cos,key=lambda cos:cos[0],reverse=True)
    return cos

def smart(q,mat):
    print q.shape
    print mat.shape
    a1=1;
    b1=0.75
    lq = len(q)
    lmat = mat.shape[0]
    qs=q*a1;
    for i in range(lmat):
        qs+=b1/lmat*mat[i,:]
    return qs


u = load(open("uf.data"))
s = load(open("sf.data"))
v = load(open("vf.data"))
term=load(open("term_id.data"))
tit=load(open("title.data"))
con = load(open("content.data"))

def getans(query):
    q1=getq(query)
    ans=[]
    mat1 = dot(inv(s),u.T);
    q2=dot(q1,mat1.T)
    cos=getcos(v,q2[0])
    for i in range(len(cos)):
        t = cos[i][1]
        content = con[t]
        title = tit[t]
        ans.append({'id':t,'title':title.decode('gbk').encode('utf-8'),'doc':content.decode('gbk').encode('utf-8')})
    return ans

# query = "发烧咳嗽"
# qans=getans(query)
# str1=qans[1]
# print str1
# #print mat
