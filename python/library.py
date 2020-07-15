#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import time
bookcase={'《大学》':101,'《中庸》':102,'《孟子》':103,'《论语》':104}
print('欢迎来到四书库')
name=input('请输入用户名:')
print('Hello',name)
while 1:
    operation={1: '查阅书库所有图书', 2: '查阅对应图书编号', 3: '修改图书编号', 4: '删除图书', 5: '添加图书', 0: '退出查询系统'}
    print('请选择操作：\n',operation)
    a=input('请输入操作编号:')
    op_number=int(a)   # str转换成整数
    if op_number in (operation.keys()):
        print(operation[op_number]) # 打印操作名称
        if op_number == 1:
            print('正在查询中，请稍候……')
            time.sleep(2)
            print('当前此库中有：\n',bookcase.keys())
            time.sleep(2)
        elif op_number == 2:
            lookup=input('请输入想要查找编号的书名：')
            if lookup in bookcase.keys():
                print('正在查询中，请稍候……')
                time.sleep(2)
                print(lookup,'对应的编号为：',bookcase[lookup]) #打印对应的编号
                time.sleep(2)
            else:
                print('你查找的图书不在此库')
                time.sleep(2)
        elif op_number == 3:
            altername=input('请输入想要修改编号的书名：')
            if altername in bookcase.keys():
                print('正在查询中，请稍候……')
                time.sleep(2)
                print(altername,'原编号为:',bookcase[altername])
                while 2:
                    newnumber=input('请输入新编号：')
                    newnumber=int(newnumber)   # str转换成整数
                    if newnumber not in bookcase.values():
                        bookcase[altername]= newnumber # 更改key对应的value   
                        print('正在更新中，请稍候……')
                        time.sleep(2)
                        print('更新四书库:\n',bookcase)
                        break
                    else:
                        print('该编号已存在，请重新输入')
                else:
                    print('你想要修改的图书不在此库')
            time.sleep(2)
        elif op_number == 4:
            deletename=input('请输入你要删除的书名：')
            if deletename in bookcase.keys():
                bookcase.pop(deletename)  # 删除该键值对
                print('正在更新中，请稍候……')
                time.sleep(2)
                print('更新四书库:\n',bookcase)
                time.sleep(2)
            else:
                print('你想要删除的图书不在此库')
                time.sleep(2)
        elif op_number == 5:
            while 3:
                addname=input('请输入你要添加的书名:')
                if addname not in bookcase.keys():
                    while 4:
                        addnumber=input('请输入该书对应的编号:')
                        addnumber=int(addnumber)
                        if addnumber not in bookcase.values():
                            bookcase[addname]=addnumber
                            print('正在更新中，请稍候……')
                            print('更新四书库:\n',bookcase)
                            break
                        else:
                            print('该编号已存在')
                    break
                else:
                    print('该书已存在') 
            time.sleep(2)
        elif op_number == 0:
            break
    else:
        print('请输入正确的操作编号！')
        time.sleep(2)
print('*******欢迎下次光临*******')
