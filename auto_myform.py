from selenium import webdriver
import time
import random

#時間のばらつきを作る
random_time = random.randint(0,10)
time.sleep(random_time)

driver = webdriver.Chrome("./chromedriver.exe")

#学校のホームページ
url = "https://forms.office.com/Pages/ResponsePage.aspx?id=T6978HAr10eaAgh1yvlMhK2wyXK178VNrGuxYcyhURJUQjE4RlJJQThWSzZTU1FBOUk4U0xNVDk0OS4u"
driver.get(url)

driver.maximize_window()
time.sleep(10)

# #フォームへアクセス
# element = driver.find_element_by_class_name("window-icon")
# element.click()
# time.sleep(10)
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(5)

# #サインイン
# element = driver.find_elements_by_tag_name("input")[0]
# key = "4330506961@utac.u-tokyo.ac.jp"
# element.send_keys(key)

# element = driver.find_element_by_id("idSIButton9")
# element.click()
# time.sleep(10)

# #学校のログイン画面
# element = driver.find_elements_by_tag_name("input")[1]
# key = "MSGmsg32016743@"
# element.send_keys(key)

# element = driver.find_element_by_id("submitButton")
# element.click()
# time.sleep(10)

# #サインインの状態を維持しますか
# element = driver.find_element_by_id("idSIButton9")
# element.click()
# time.sleep(10)


#フォーム

# #mail
element = driver.find_elements_by_tag_name("input")[0]
element.click()

#入構先
element = driver.find_elements_by_tag_name("input")[3]
element.click()

#滞在場所(未定)
element = driver.find_element_by_class_name("office-form-question-textbox")
key = "工2号館"
element.send_keys(key)


#温度
element = driver.find_elements_by_tag_name("input")[8]
element.click()

# ##input欄の数が異なる場合、提出をやめる
# input_number = driver.find_elements_by_tag_name("input")
# if len(input_number) != 13:
#     driver.close()

time.sleep(10)

#最後に送信ボタンを押す
# driver.execute_script(
#     "var element = document.documentElement;var bottom = element.scrollHeight;window.scrollTo(0, bottom);")
element = driver.find_elements_by_class_name('button-content')[1]

element.click()
time.sleep(5)

#ウィンドウを閉じる
driver.close()
