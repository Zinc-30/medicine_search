#-*- coding:utf-8-*-
import jieba
from numpy import *
from numpy.linalg import *
from scipy import *
from pickle import *
def getdlen():
    return len(doc1)
def getans(query):
    qlist = jieba.cut(query)
    q=[];
    nnum = getdlen();
    for w in qlist:
        s=w.encode('gbk')
        if s in tf:
            res = tf[s]
            print "s",s
            dn = len(res)
            if (dn<nnum/2):
                for i in range(dn):
                    find = True
                    wtd=(1+log10(res[i][1]))*log10(nnum/dn)
                    for j in range(len(q)):
                        if (res[i][0]==q[j][0]):
                            q[j][1]+=wtd
                            find = False;
                    if find:
                        q.append([res[i][0],wtd])          
    q=sorted(q,key=lambda q:q[1],reverse=True)
    ans=[]
    maxl=min(len(q),126);
    for i in range(maxl):
        if (q[i][0]<4013):
            con = doc[q[i][0]]
            #print "con",con
            title = doc1[q[i][0]]
            #print "title",title
            ans.append({'id':q[i][0],'title':title.decode('gbk').encode('utf-8'),'doc':con.decode('gbk').encode('utf-8')})
    return ans

def getans1(query):
    qlist = jieba.cut(query)
    q=[];
    nnum = getdlen();
    for w in qlist:
        s=w.encode('gbk')
        if s in tf1:
            res = tf1[s]
            print "s",s
            dn = len(res)
            if (dn<nnum/2):
                for i in range(dn):
                    find = True
                    wtd=(1+log10(res[i][1]))*log10(nnum/dn)
                    for j in range(len(q)):
                        if (res[i][0]==q[j][0]):
                            q[j][1]+=wtd
                            find = False;
                    if find:
                        q.append([res[i][0],wtd])          
    q=sorted(q,key=lambda q:q[1],reverse=True)
    ans=[]
    maxl=min(len(q),125);
    for i in range(maxl):
        if (q[i][0]<4013):
            con = doc[q[i][0]]
            #print "con",con
            title = doc1[q[i][0]]
            #print "title",title
            ans.append({'id':q[i][0],'title':title.decode('gbk').encode('utf-8'),'doc':con.decode('gbk').encode('utf-8')})
    return ans

def get_info(id):
    name = 'buy/'+doc1[id]+'.txt'
    j = -1 
    i = 0
    buy = []
    f = open(name,'r')
    s = f.readline()
    while s:
        if i == 0 :
            j = j + 1
            a = {}
        if s.strip()!='': i = i + 1
        else:
            s = f.readline()
            i = i + 1
        i = i % 4
        #print s.strip()
        #print i
        if i == 1:
            a['name'] = s.strip()
        elif i == 2:
            a['price'] = s.strip()
        elif i == 3:
            a['url'] = s.strip()
        elif i == 0:
            a['image'] = s.strip()
            buy.append(a)    
        s = f.readline()
    f.close()
    return buy

docf=open("content.data",'rb')
doc=load(docf);
docf.close();
docf=open("title.data",'rb')
doc1=load(docf);
docf.close();
# termf=open("tid.data",'rb')
# term=load(termf)
# termf.close()
tff = open("tf_con.data",'rb')
tf = load(tff);#content tf
tff.close();
tff = open("tf_tit.data",'rb')
tf1 = load(tff);#title tf
tff.close();


#query = "发烧咳嗽"
#qans=getans(query)
#str1=qans[1]
#print str1
#print mat
