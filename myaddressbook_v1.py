#!/usr/bin/python
#-*- encoding:UTF-8 -*-
# Filename:myaddress_books.py

import cPickle as p
import os

class Contact:     #m目前类没有用上……
    def __init__(self,name,tel):
        self.tel=tel
        self.name=name
        a_b={self.name:self.tel} #ab is short for address_book
    def add(self,name,tel):
        a_b[name]=self.name
        a_b[tel]=self.tel
a_b={}
f=file('address_book.data','r')
a_b=p.load(f)
f.close
while True:
    print '''
|---欢迎进入通讯录程序---------|
|---1、 查询联系人资料---------|
|---2、 插入或修改联系人资料---|
|---3、 删除已有联系人---------|
|---4、 退出通讯录程序---------|'''
    temp=raw_input('请输入指令代码')
    if not temp.isdigit():
        print "输入的指令错误，请按照提示输入"
        continue
    item=int(temp) #转换为数字
    if item ==4:
        print"|---感谢使用通讯录程序---|"
        break
    if item==1:
        name=raw_input("请输入联系人姓名：")
        if name in a_b:
            print "您输入的联系人信息为：",name,":",a_b[name]
            continue
        else:
            print "该联系人不存在！"
    if item==2:
        name=raw_input("请输入联系人姓名：")
        if name in a_b:
            print"您输入的姓名在通讯录中已存在-->>",name,":",a_b[name]
            isEdit=raw_input("是否修改联系人资料(Y/N）:")
            if isEdit=="Y"or"y":
                tel=raw_input("请输入联系人电话：")
                a_b["name"]=tel
                print "联系人修改成功"
                continue
            else:
                continue
        else:
            tel=raw_input("请输入联系人电话：")
            a_b[name]=tel
            print "联系人修改成功"
        
    if item==3:
        name=raw_input("请输入联系人姓名：")
        if name in a_b:
            del a_b[name]
            print "联系人删除成功"
            continue
        else:
            print "联系人不存在"
    f=open('address_book.data','w')
    p.dump(a_b,f)
    f.close
