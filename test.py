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
sleep_sec = 1

options = [
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JK662', 
		'item_to_buy': {
			(0, 0): 7, # No. 22 SIZE 3
			(1, 0): 9  # No. 72 SIZE 3
		},
		'account':'www111.hung@gmail.com',
		'password':'777seven',
		'description': 'testing'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JT663', 
		'item_to_buy': {
			(0, 0): 12, # No. 22 SIZE 3
			(1, 0): 5  # No. 72 SIZE 3
		},
		'account':'www222.hung@gmail.com',
		'password':'777seven',
		'description': 'testing'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JF665', 
		'item_to_buy': {
			(1, 0): 14  # No. 72 SIZE 3
		},
		'account':'www333.hung@gmail.com',
		'password':'777seven',
		'description': 'testing'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13KK741', 
		'item_to_buy': {
			(1, 0): 4, # GRAISH BLUE （no.70）
		},
		'account':'www444.hung@gmail.com',
		'password':'777seven',
		'description': 'testing'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JF664', 
		'item_to_buy': {
			(0, 2): 1, # No. 22 SIZE 4
			(1, 1): 2, # No. 72 SIZE 3
		},
		'account':'www555.hung@gmail.com',
		'password':'777seven',
		'description': 'testing'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JG653', 
		'item_to_buy': {
			(0, 1): 3, # NO 32色   SIZE 3
			(0, 3): 1, # NO 32色   SIZE 5
			(1, 0): 2, # NO 62色   SIZE 2
			(1, 1): 10, # NO 62色   SIZE 3
			(1, 3): 2 # NO 62色   SIZE 5
		},
		'account':'www666.hung@gmail.com',
		'password':'777seven',
		'description': 'testing'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP11JK941', 
		'item_to_buy': {
			(1, 0): 20, # NO 40色   SIZE 3
			(2, 0): 20, # NO 65色   SIZE 3
			(3, 0): 20, # NO 72色   SIZE 3
			(4, 0): 20, # NO 75色   SIZE 3
		},
		'account':'www777.hung@gmail.com',
		'password':'777seven',
		'description': 'testing'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP11JK942', 
		'item_to_buy': {
			(0, 0): 3, # NO 22色   SIZE 3
			(1, 0): 1, # NO 40色   SIZE 3
			(2, 0): 2, # NO 65色   SIZE 3
			(3, 0): 10, # NO 72色   SIZE 3
			(4, 0): 2 # NO 75色   SIZE 3
		},
		'account':'www888.hung@gmail.com',
		'password':'777seven',
		'description': 'testing'
	},

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
						#if(button[1].text != "入荷お知らせメール"):
						for k in range(len(button)):
							if button[k].text == 'カートに入れる':
								try:
									print('button text: ', button[k].text)
									print('click button!')
									button[k].click()
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
	cnt = 0
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
			print(cnt)
			# return False
			if cnt > 5:
				return False
			closeButton = driver.find_elements_by_class_name('iziToast-close')
			try:
				cnt += 1
				for i in closeButton:
					i.click()
					
					
			except selenium.common.exceptions.StaleElementReferenceException:
				print('stale element!')
				break
			
	time.sleep(1)
	i = 10
	while i > 0:	
		i = i - 1	
		try:
			Cash_on_delivery_button = driver.find_element_by_xpath(("//label[@for='fs_input_payment_cashOnDelivery']"));
			print(Cash_on_delivery_button)
			Cash_on_delivery_button.click()

			break
		except selenium.common.exceptions.NoSuchElementException:
			print("no cash on delivery button!")
		
	print('confirm : ', confirm)
	if confirm:
		for i in range(10):
			
			try:
				print('confirm!')
				confirmButton = driver.find_elements_by_class_name("fs-c-button--confirmOrder")
				time.sleep(1)

				print(confirmButton[0].text)
				confirmButton[0].click()
				time.sleep(2)
				return True
			except selenium.common.exceptions.StaleElementReferenceException:
				print('stale element! try again!')
	
	print('---%s seconds ---' % (time.time() - start_time))
	return False
	
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
	driver.maximize_window()
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
			item_need_to_buy_count = sum(item_to_buy.values())
			print("No product to buy! sleep " + str(sleep_sec) + " secs")
			time.sleep(sleep_sec)
			driver.refresh()
			item_quantity = check_items_quantity(item_to_buy, url)
			print("current quantity: ", item_quantity)
			if item_need_to_buy_count == 0:
				print('bye!')
				driver.quit()
				exit(-1)
			
		if item_quantity:
			print ('real buy: ', sys.argv[2])
			if not finish_buy(int(sys.argv[2])):
				# time.sleep(1)
				clear_cart() 

		# driver.quit()
			
if __name__ == '__main__':

	if (len(sys.argv) < 3):
		print ('wrong number of argv!')
		driver.quit()
		exit(-1)
	idx = int(sys.argv[1])
	print('idx is: ', idx)
	try:
		main(idx=idx, restart=False)
	except selenium.common.exceptions.NoSuchWindowException:
		print('bye!')
		driver.quit()
		exit(-1)
	# while True:
	# 	pass
	
