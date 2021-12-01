#!/usr/bin/env python3

import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException as NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException as ElementNotInteractableException
import threading
import sys
# define driver
#chromedriver = '/usr/local/bin/chromedriver'
chromedriver = '/opt/homebrew/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)
#driver = webdriver.Chrome(ChromeDriverManager().install())
cart_url = "https://store.isseymiyake.com/p/cart?type=purchase"
sleep_sec = 1

options = [
  # first
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JK662', 
		'item_to_buy': {
			(0, 0): 10, # No. 22 SIZE 3
			(1, 0): 10  # No. 72 SIZE 3
		},
		'account':'www111.hung@gmail.com',
		'password':'777seven',
		'description': '1-1'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JT663', 
		'item_to_buy': {
			(0, 0): 8, # No. 22 SIZE 3
			(1, 0): 3  # No. 72 SIZE 3
		},
		'account':'www222.hung@gmail.com',
		'password':'777seven',
		'description': '1-2'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JF665', 
		'item_to_buy': {
			(1, 0): 12,  # No. 72 SIZE 3
		},
		'account':'www333.hung@gmail.com',
		'password':'777seven',
		'description': '1-3'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JK661', 
		'item_to_buy': {
			(0, 0): 2, # 22 size 3
      (0, 0): 2, # 72, 3
      (0, 1): 2 # 72, 4
		},
		'account':'www444.hung@gmail.com',
		'password':'777seven',
		'description': '1-4'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JF664', 
		'item_to_buy': {
			(0, 2): 1, # No. 22 SIZE 4
		},
		'account':'www555.hung@gmail.com',
		'password':'777seven',
		'description': '1-5'
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
		'description': '1-6'
	},
  # second
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JF165', 
		'item_to_buy': {
		},
		'account':'www777.hung@gmail.com',
		'password':'777seven',
		'description': '2-1'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JH166', 
		'item_to_buy': {
			(3, 1): 1, # NO 76色   SIZE 3
			(4, 3): 1, # NO 81色   SIZE 5
		},
		'account':'www888.hung@gmail.com',
		'password':'777seven',
		'description': '2-2'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JH573', 
		'item_to_buy': {
			(2, 1): 2, # NO 76色   SIZE 3
		},
		'account':'www999.hung@gmail.com',
		'password':'777seven',
		'description': '2-3'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JT162', 
		'item_to_buy': {
			(2, 0): 1, # NO 70色   SIZE 3
			(4, 0): 2, # NO 81色   SIZE 3
		},
		'account':'www1111.hung@gmail.com',
		'password':'777seven',
		'description': '2-4'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JK161', 
		'item_to_buy': {
			(1, 0): 3, # NO 55色   SIZE 3
			(1, 1): 1, # NO 55色   SIZE 4
			(2, 0): 3, # NO 70色   SIZE 3
			(2, 1): 1, # NO 70色   SIZE 4
		},
		'account':'www2222.hung@gmail.com',
		'password':'777seven',
		'description': '2-5'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JF164', 
		'item_to_buy': {
        (3, 2): 6, # 76 size 3
        (3, 3): 1, # 76 size 4
        (4, 2): 1, # 81 size 3
		},
		'account':'www3333.hung@gmail.com',
		'password':'777seven',
		'description': '2-6'
	},
  # third
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP11JK942', 
		'item_to_buy': {
        (0, 0): 10,
        (1, 0): 10,
        (2, 0): 10,
        (3, 0): 10,
        (4, 0): 10,
		},
		'account':'www4444.hung@gmail.com',
		'password':'777seven',
		'description': '3-1'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP11JK941', 
		'item_to_buy': {
        (1, 0): 10,
        (2, 0): 10,
        (3, 0): 10,
        (4, 0): 10,
		},
		'account':'www5555.hung@gmail.com',
		'password':'777seven',
		'description': '3-2'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JF673', 
		'item_to_buy': {
        (0, 0): 2,
        (1, 0): 2, 
		},
		'account':'www6666.hung@gmail.com',
		'password':'777seven',
		'description': '3-3'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JH675', 
		'item_to_buy': {
        (0, 0): 3,
        (0, 1): 2,
        (1, 0): 1,
		},
		'account':'www7777.hung@gmail.com',
		'password':'777seven',
		'description': '3-4'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JH683', 
		'item_to_buy': {
        (0, 0): 1,
        (0, 2): 1,
		},
		'account':'www8888.hung@gmail.com',
		'password':'777seven',
		'description': '3-5'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP13JK671', 
		'item_to_buy': {
        (0, 0): 4,
        (1, 0): 1,
		},
		'account':'www9999.hung@gmail.com',
		'password':'777seven',
		'description': '3-6'
	},
  # fourth
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP11JK942', 
		'item_to_buy': {
        (0, 0): 10,
        (1, 0): 10,
        (2, 0): 10,
        (3, 0): 10,
        (4, 0): 10,
		},
		'account':'www0000.hung@gmail.com',
		'password':'777seven',
		'description': '4-1'
	},
	{
		'url': 'https://store.isseymiyake.com/c/pl_all_all/PP11JK941', 
		'item_to_buy': {
        (1, 0): 10,
        (2, 0): 10,
        (3, 0): 10,
        (4, 0): 10
		},
		'account':'www1122.hung@gmail.com',
		'password':'777seven',
		'description': '4-2'
	},
	{
		'url': 'https://store.isseymiyake.com/c/at_all_all/AT13FD221', 
		'item_to_buy': {
        (0, 0): 1,
        (1, 0): 1,
        (2, 0): 1
		},
		'account':'www3344.hung@gmail.com',
		'password':'777seven',
		'description': '4-3'
	},
	{
		'url': 'https://store.isseymiyake.com/c/at_all_all/AT13FH223', 
		'item_to_buy': {
        (0, 0): 5,
        (1, 0): 4,
        (2, 0): 1
		},
		'account':'www5566.hung@gmail.com',
		'password':'777seven',
		'description': '4-4'
	},
	{
		'url': 'https://store.isseymiyake.com/c/at_all_all/AT13FJ226', 
		'item_to_buy': {
        (0, 0): 2,
        (1, 0): 8,
        (2, 0): 1
		},
		'account':'www7788.hung@gmail.com',
		'password':'777seven',
		'description': '4-5'
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
	