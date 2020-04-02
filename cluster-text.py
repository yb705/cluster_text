from selenium import webdriver
import time
#import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome("chromedriver.exe")
driver.maximize_window()
driver.get("http://oa.58.com.cn")
password=input("是否已经登录58盾与oa账号密码（是/否）：")
if password=='是':
	driver.get("http://union.vip.58.com/bsp/index")
#wait = ui.WebDriverWait(driver,50)#程序每隔500毫秒看一眼
#wait.until(lambda driver:driver.find_element_by_xpath('//*[text()='产品管理后台']'))#如果条件成立了，则执行下一步；否则继续等待，直到超过设置的最长时间，然后抛出TimeoutException异常。
cluster_text = driver.find_element_by_id("bt9")
cluster_text.click()
cluster_text_0 = driver.find_element_by_id("bt9_0")#id元素定位
cluster_text_0.click()
#cluster_text_1= driver.find_element_by_id("iauditwebnewweiliaotextcheck")
#cluster_text_1.click()
driver.get("http://clustercheckweb.union.vip.58.com/weiliaoNewclustercheck/weiliaotextcheck")
#driver.find_element_by_link_text('新微聊文本聚类审核').click()#超链接文本定位
driver.find_element_by_xpath("//select[@class='scope']/option[text()='vip用户']").click()#select是标签
time_0=input("请输入工作时间（分钟）：")
time_1=int(time_0)*60
def Single_work():
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#将整个页面拉到底部
	driver.find_element_by_id("checkALL").click()
while time_1!=0:
	time.sleep(3)
	Single_work()
	time_1-=3
