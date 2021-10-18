#!/usr/bin/env python3

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException as NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException as ElementNotInteractableException
import threading

# define driver
chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)
cart_url = "https://store.isseymiyake.com/p/cart?type=purchase"
url = 'https://store.isseymiyake.com/c/ha_all_all/HA15JT111'

item_to_buy = {
	(0,0):1,
	(1,0):1
}

#login
def login(driver):
	start_time = time.time()
	print("try to login!")
	driver.get('https://store.isseymiyake.com/my/top')
	driver.find_element_by_name('mailAddress').send_keys("www777.hung@gmail.com")
	driver.find_element_by_name('password').send_keys("777seven")
	print("click login button!")
	try:
		loginButton = driver.find_elements_by_class_name("fs-c-button--login")
		loginButton[0].click()
	except ElementNotInteractableException:
		pass
		
	print('---%s seconds ---' % (time.time() - start_time))

	
def check_items_quantity(driver, url):
	start_time = time.time()
	driver.get(url)
	print("item name you're checking is: ", driver.title.split('|')[0])
	print("product names are: ")
	item_cnt = 0
	try:
		html_list = driver.find_elements_by_class_name("fs-c-variationList__item__cart")
		for i in range(len(html_list)):
			items = html_list[i].find_elements_by_tag_name("li")
			for j in range(len(items)):
				if (i,j) in item_to_buy:
					if(item_to_buy[(i,j)] > 0):
						print((i,j))
						print("quantity: ", item_to_buy[(i,j)])
						button = items[j].find_elements_by_tag_name("button")
						if(button[1].text != "入荷お知らせメール"):
							button[1].click()
							item_cnt += 1
							item_to_buy[(i,j)] -= 1
#		productButton = driver.find_elements_by_class_name("fs-c-button--addToCart--variation")
		print("There are " + str(item_cnt) + " items you can buy!")
		print('---%s seconds ---' % (time.time() - start_time))
		return item_cnt
	except NoSuchElementException:
		print("no product name!")
		
	print('---%s seconds ---' % (time.time() - start_time))
	return 0
	
def finish_buy(driver, confirm):
	start_time = time.time()
	finish_flag = False
	print("go to cart!")
	while not finish_flag:
		driver.get(cart_url)
		print("purchase!")
		purchaseButton = driver.find_elements_by_class_name("fs-c-button--purchaseHere")
		print(len(purchaseButton))
		try:
			purchaseButton[0].click()
			print('finish!')
			finish_flag = True
		except IndexError:
			print('no purchase button! close toast!')
			closeButton = driver.find_elements_by_class_name('iziToast-close')
			try:
				for i in closeButton:
					i.click()
					
			except selenium.common.exceptions.StaleElementReferenceException:
				break
				pass
			
	try:
		Cash_on_delivery_button = driver.find_element_by_xpath(("//label[@for='fs_input_payment_cashOnDelivery']"));
		print(Cash_on_delivery_button)
		Cash_on_delivery_button.click()
	except selenium.common.exceptions.NoSuchElementException:
		print("no button!")
		
	print('confirm button!')
	confirmButton = driver.find_elements_by_class_name("fs-c-button--confirmOrder")
	if confirm:
		confirmButton[0].click()
	print('---%s seconds ---' % (time.time() - start_time))
	
def clear_cart(driver):
	start_time = time.time()
	print("go to cart!")
	driver.get(cart_url)
	print("clear cart start!")
	clear_flag = False
	while not clear_flag:
		clearButton = driver.find_elements_by_class_name("fs-c-button--cancel--cart")
		if len(clearButton) == 0:
			print("clear Done!")
			return True
		try:
			clearButton[0].click()
			print("cleared one product!")
			time.sleep(1)
		except selenium.common.exceptions.StaleElementReferenceException:
			print("element missing!")
		except IndexError:
			print("no clear Button! ")
			clear_flag = True
	print('---%s seconds ---' % (time.time() - start_time))
	
def main(driver, url=url,restart=False):	
	if not restart:
		login(driver)
		clear_cart(driver)
		#clear_cart()
		
	item_quantity = check_items_quantity(driver, url)
	print("quantity: ", item_quantity)
	while item_quantity == 0:
		print("No product to buy! sleep 10 secs")
		time.sleep(5)
		clear_cart(driver)
		driver.refresh()
		item_quantity = check_items_quantity(driver, url)
		print("quantity: ", item_quantity)
		
	if item_quantity:
		finish_buy(driver, False)  
			
if __name__ == '__main__':
	main(url=url,driver=driver, restart=False)
	while True:
		pass
	
