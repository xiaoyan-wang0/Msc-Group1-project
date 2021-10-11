# -*- coding: utf-8 -*-
import  random,string,hashlib,base64
class UserService():

    @staticmethod
    def geneAuthCode( user = None ):
        m = hashlib.md5()
        str = "%s-%s-%s"%( user.userId,user.userName,user.password )
        m.update( str.encode("utf-8") )
        return m.hexdigest()

    @staticmethod
    def genePwd(pwd):
        m = hashlib.md5()
        str = "%s"%( base64.encodebytes( pwd.encode("utf-8") )  )
        m.update( str.encode("utf-8") )
        return m.hexdigest()
