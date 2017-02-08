# -*- coding:utf-8 -*-
import requests,simplejson
from Crypto.Cipher import AES
import hashlib
import base64
def get_sha1(data):
    '''
    sha1加密
    '''
    s = hashlib.sha1()
    s.update(data)
    return s.hexdigest()

def aespks5b64_encrypt(data, key, iv):
    '''
    用aes CBC加密，再用base64  encode，补码方式：pks5
    '''
    BS = AES.block_size
    datas =data.encode('utf8')
    #PKCS5Padding方式补码
    pad_PKCS5 = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad_PKCS5(datas))  #aes加密
    result = base64.b64encode(encrypted)  #base64 encode
    return result

def aespks7b64_encrypt(data, key, iv):
    '''
    用aes CBC加密，再用base64  encode，补码方式：pks7
    '''
    BS = AES.block_size
    datas=data.encode('utf8')
    #PKCS7Padding方式补码
    pad_PKCS7 = lambda s: s + (BS - len(s) % BS) * '0'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad_PKCS7(datas))  #aes加密
    result = base64.b64encode(encrypted)  #base64 encode
    return result

def GetToken(username,password):
    try:
        url = 'https://app.niiwoo.com:5004/niiwoo-api/niwoportservice.svc/PostUserLogin'
        datas = 'jsonString={"userName":"'+username+'","password":"'+password+'"}'
        r = requests.post(url,params=datas)
        response=simplejson.loads(r.text)
        UserToken=response['Data']['userToken']
        print '获取Token成功'
        return UserToken
    except Exception as e:
        print e
    

def RequestAPI(apiName,apiVersion,data,sign=None):
    try:
        url = 'https://app.niiwoo.com:5004/niiwoo-api/niwoportservice.svc/'+apiName+'?appKey=00002&v='+apiVersion+'&sign='+sign
        resp = requests.post(url,data)
        response = simplejson.loads(resp.text)
        print '接口 %s ,响应: %s'
        return response
    except:
        raise



def GetSign(version,Token,data_sign):

    # 密钥 key
    key = 'A0B5C2D4E7F90301'  # the length can be (16, 24, 32)
    # 初始向量
    iv = key
    # 拼接的字符串预处理定义
    appKey = 'appKey00002'
    jsonString = 'jsonString'
    UserToken = 'userToken'
    ver = 'v'

    AESencrypt_value = aespks5b64_encrypt(data_sign,key,iv)
    ssign = ''
    a = [key, appKey, jsonString, AESencrypt_value,UserToken,Token, ver, version, key]
    # 将 a 按照顺序进行拼接
    ssign = ssign.join(a)
    # 进行sha1 运算得到 签名的值
    asign = get_sha1(ssign)
    # 将sha1运算的结果转换为大写
    sign = asign.upper()
    return sign

username = '18589091413'
password = 'Solution@559'
apiName = 'Sign'
apiVersion = '3.2'
data_sign = 'jsonString={"签到积分":"20"}'
Token = GetToken(username, password)
sign = GetSign(apiVersion,Token,data_sign)
resp = RequestAPI(apiName,apiVersion,data_sign,sign)
print resp