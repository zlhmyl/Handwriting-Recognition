# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 20:38:57 2019

@author: SA
"""

import logging

log = logging.getLogger()
log.setLevel('INFO')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

#from cassandra.cluster import Cluster
#from cassandra import ConsistencyLevel

from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

KEYSPACE = "Users"

def createKeySpace():
   cluster = Cluster(contact_points=['172.18.0.3'],port=9042)#cassandra container ip address
   session = cluster.connect()

   log.info("Creating keyspace...")
   try:
       '''
       session.execute("""
           CREATE KEYSPACE %s
           WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '1' };
           """ % KEYSPACE)
       '''
       session.execute("CREATE KEYSPACE %s WITH replication = {'class':'SimpleStrategy', 'replication_factor':1};" % KEYSPACE)

       log.info("setting keyspace...")
       session.execute('use %s;' % KEYSPACE)
       #session.set_keyspace(KEYSPACE)

       log.info("creating table...")
       session.execute("CREATE TABLE UserInfo(timestamp timestamp,imagename text,predict_number int,PRIMARY KEY(timestamp,imagename));")


   except Exception as e:
       #log.error("Unable to create keyspace")
       log.error(e)
       

#createKeySpace();

def insertData(file_name,number):
    cluster = Cluster(contact_points=['172.18.0.3'],port=9042)
    session = cluster.connect()
    session.execute("use %s" % KEYSPACE)
    session.execute('INSERT INTO USerInfo(timestamp,imagename,predict_number)VALUES(toTimestamp(now()),%s,%s);',[file_name,number])
    
#insertData('text.jpg',5)
    

