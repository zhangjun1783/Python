#coding=utf-8
#coding=utf-8
from selenium import webdriver
import os

url='http://www.baidu.com'
#iedriver ='C:\Program Files (x86)\Python37-32\IEDriverServer.exe' #iedriver路径
os.environ["webdriver.ie.driver"] = iedriver #设置环境变量
driver = webdriver.Ie(iedriver)
driver.get(url)
driver.close()
#2024-12-10 10:30:00  今天开始测试推送github，虽然不知道怎么操作，但是还是成功了，哈哈
#这是一个测试版本，后续会继续完善，今天看到了6年前提交的版本，真是惭愧啊，当初开始学习python，学习了两天就放弃了，现在失业了才知道当初应该好好学习技能的。
#今天下午，我又开始学习python，虽然很慢，但是还是很有收获，我会努力学习的，加油！
#想起了一句话，书到用时方恨少，事非经过不知难。000000