#!/usr/bin/env python3

import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException as NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException as ElementNotInteractableException
import threading
import sys
# define driver
chromedriver = '/usr/local/bin/chromedriver'
#chromedriver = '/opt/homebrew/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)
cart_url = "https://store.isseymiyake.com/p/cart?type=purchase"

options = [
	{
		'url': 'https://store.isseymiyake.com/c/ha_all_all/HA15JT111', 
		'item_to_buy': {
			(0,0): 1,
			(1,0): 1
		},
		'account':'www777.hung@gmail.com',
		'password':'777seven',
		'description': 'testing'
	},
	{
		'url': 'https://store.isseymiyake.com/c/la_all_all/LA13FC185',
		'item_to_buy': {
			(0, 1): 1,
			(1, 1): 2
		},
		'account':'qwerty8608301@gmail.com',
		'password':'9FMp3.!.2mE6e6u',
		'description': 'testing'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JH157',
		'item_to_buy': {
			(0, 1): 4,
			(0, 2): 4,
			(0, 3): 2
		},
		'account': 'www111.hung@gmail.com',
		'password': '777seven',
		'description': ''
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JC152',
		'item_to_buy': {
			(0, 1): 2
		},
		'account': 'www222.hung@gmail.com',
		'password': '777seven',
		'description': ''
	}
]

#login
def login(account, password):
	start_time = time.time()
	print("try to login!")
	driver.get('https://store.isseymiyake.com/my/top')
	driver.find_element_by_name('mailAddress').send_keys(account)
	driver.find_element_by_name('password').send_keys(password)
	print("click login button!")
	try:
		loginButton = driver.find_elements_by_class_name("fs-c-button--login")
		loginButton[0].click()
	except ElementNotInteractableException:
		pass
		
	print('---%s seconds ---' % (time.time() - start_time))
	
def check_items_quantity(item_to_buy, url):
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
						print("quantity to buy: ", item_to_buy[(i,j)])
						button = items[j].find_elements_by_tag_name("button")
						if(button[1].text != "入荷お知らせメール"):
							try:
								button[1].click()
								item_cnt += 1
								item_to_buy[(i,j)] -= 1
							except selenium.common.exceptions.ElementNotInteractableException: 
								print('element not exist!')
#		productButton = driver.find_elements_by_class_name("fs-c-button--addToCart--variation")
		print("There are " + str(item_cnt) + " items you can buy!")
		print('---%s seconds ---' % (time.time() - start_time))
		return item_cnt
	except NoSuchElementException:
		print("No product list!")
		
	print('---%s seconds ---' % (time.time() - start_time))
	return 0
	
def finish_buy(confirm):
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
			cnt = 0
			print('no purchase button! close toast!')
			closeButton = driver.find_elements_by_class_name('iziToast-close')
			try:
				for i in closeButton:
					i.click()
					cnt += 1
					
			except selenium.common.exceptions.StaleElementReferenceException:
				break
			if cnt > 10:
				return False
			
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
	
def clear_cart():
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
	
def main(idx=0, restart=False):	
	url = options[idx]['url']
	item_to_buy = options[idx]['item_to_buy']
	account = options[idx]['account']
	password = options[idx]['password']
	if not restart:
		login(account=account, password=password)
		clear_cart()

	item_need_to_buy_count = sum(item_to_buy.values())

	while item_need_to_buy_count > 0:
		item_need_to_buy_count = sum(item_to_buy.values())
		print("item need to buy count: ", item_need_to_buy_count)
		print("item_to_buy: ", item_to_buy)
		item_quantity = check_items_quantity(item_to_buy, url)
		print("quantity: ", item_quantity)
		while item_quantity == 0:
			print("No product to buy! sleep 10 secs")
			time.sleep(5)
			driver.refresh()
			item_quantity = check_items_quantity(item_to_buy, url)
			print("current quantity: ", item_quantity)
			
		if item_quantity:
			print ('real buy: ', sys.argv[2])
			finish_buy(sys.argv[2]) 
			clear_cart() 
			
if __name__ == '__main__':
	if (len(sys.argv) < 3):
		print ('wrong number of argv!')
		driver.close()
		exit(-1)
	idx = int(sys.argv[1])
	print('idx is: ', idx)
	main(idx=idx, restart=False)
	while True:
		pass
	
