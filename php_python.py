#-*- coding: utf-8
import time
import socket
import os
import process
# -------------------------------------------------
# ��������
# -------------------------------------------------
LISTEN_PORT = 21230     #���������˿�
CHARSET = "utf-8"       #�����ַ�������PHP�������ַ�����
# -------------------------------------------------
# Oracle���ݿ���������
# -------------------------------------------------
'''
import cx_Oracle
#���ݿ��ַ���
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8' 
#���ݿ����ӳ�
pool = cx_Oracle.SessionPool(
    user='diaoyf',
    password='700327',
    dsn='127.0.0.1/xe',
    min=5,
    max=10,
    increment=1,
    connectiontype=cx_Oracle.Connection,
    threaded=True,
    getmode=cx_Oracle.SPOOL_ATTRVAL_NOWAIT,
    homogeneous=True)

def getConn():
    """������ݿ����ӵĹ�������"""
    return pool.acquire()

def closeConn(conn):
    """�ͷ����ݿ����ӵĹ�������"""
    pool.release(conn)
'''
# -------------------------------------------------
# ������
#    �벻Ҫ�����޸�����Ĵ���
# -------------------------------------------------
if __name__ == '__main__':

    print ("-------------------------------------------")
    print ("- PPython Service")
    print ("- Time: %s" % time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) )
    print ("-------------------------------------------")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #TCP/IP
    sock.bind(('', LISTEN_PORT))  
    sock.listen(5)  

    print ("Listen port: %d" % LISTEN_PORT)
    print ("charset: %s" % CHARSET)
    print ("Server startup...")

    while 1:  
        connection,address = sock.accept()  #�յ�һ����
        print ("client's IP:%s, PORT:%d" % address)
        # �����߳�
        try:
            process.ProcessThread(connection).start()
        except:
            pass
