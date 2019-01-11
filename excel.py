# -*- coding:utf-8 -*-
__author__ = 'TengYu'
import xlwt


def getCount(filename):
    excel = xlwt.Workbook(encoding='utf-8')
    sheet = excel.add_sheet('sheet1')
    dic={}
    count = 0
    i = 1
    sheet.write(0,0,'mark')
    sheet.write(0,1,'count')
    sheet.write(0,2,'percent')
    for keys in open(filename):
        if i == 1:
            i += 1
            continue
        else:
            count += 1
            keys = keys[:-1]
            if keys not in dic:
                dic[keys] = 1
                print(keys)
            else:
                num = dic[keys]
                dic[keys] = num + 1
    j = 1
    for key in dic.keys():
        sheet.write(j,0,key)
        sheet.write(j,1,dic[key])
        sheet.write(j,2,float(dic[key])/count)
        j += 1
    excel.save('mark2.xls')


if __name__=="__main__":
    filename='1.txt'
    getCount(filename)
