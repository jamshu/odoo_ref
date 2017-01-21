import xmlrpclib
dbname = 'lili_live'
username = pwd = 'admin'
sock_common = xmlrpclib.ServerProxy ('http://128.199.125.32/xmlrpc/common')
uid = sock_common.login(dbname, username, pwd)

#replace localhost with the address of the server
sock = xmlrpclib.ServerProxy('http://128.199.125.32/xmlrpc/object')


args = [] #query clause
ids = sock.execute(dbname, uid, pwd, 'res.partner', 'search', args)

fields = ['name','email','mobile'] #fields to read
data = sock.execute(dbname, uid, pwd, 'res.partner', 'read', ids, fields) #ids is a list of id
print "data>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",data
