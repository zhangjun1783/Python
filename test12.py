#coding=utf-8
#coding=utf-8
from selenium import webdriver
import os

url='http://www.baidu.com'
iedriver ='C:\Program Files (x86)\Python37-32\IEDriverServer.exe' #iedriver路径
os.environ["webdriver.ie.driver"] = iedriver #设置环境变量
driver = webdriver.Ie(iedriver)
driver.get(url)
driver.close()