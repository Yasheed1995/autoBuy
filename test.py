#!/usr/bin/env python3

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException as NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException as ElementNotInteractableException
import threading
import sys

import json

from ast import literal_eval
# define driver
ser = Service('/opt/homebrew/bin/chromedriver')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
cart_url = "https://store.isseymiyake.com/p/cart?type=purchase"
sleep_sec = 4
program_start_time = 0


def write_options():
    with open ('options.json', 'w') as f:
      for item in options:
        item['item_to_buy'] = {str(k): v for k, v in item['item_to_buy'].items()}
    json.dump(options, f)

def read_options():
    with open ('options.json', 'r') as f:
      obj = json.load(f)

    for item in obj:
      item['item_to_buy'] = {literal_eval(k): v for k, v in item['item_to_buy'].items()}

    return obj

#login
def login(account, password):
	start_time = time.time()
	print("try to login!")
	driver.get('https://store.isseymiyake.com/my/top')
	driver.find_element(By.NAME, 'mailAddress').send_keys(account)
	driver.find_element(By.NAME, 'password').send_keys(password)
	print("click login button!")
	try:
		loginButton = driver.find_elements(By.CLASS_NAME, "fs-c-button--login")
		loginButton[0].click()
	except ElementNotInteractableException:
		pass
		
	print('---%s seconds ---' % (time.time() - start_time))
	
def check_items_quantity(item_to_buy, url):
	start_time = time.time()
	driver.get(url)
	print("item name you're checking is: ", driver.title.split('|')[0])
	if (driver.title.split('|')[0] == ''):
		print("ip blocked!")
		print("elapsed time: ", time.time() - program_start_time)
	print("product names are: ")
	item_cnt = 0
	try:
		html_list = driver.find_elements(By.CLASS_NAME, "fs-c-variationList__item__cart")
		for i in range(len(html_list)):
			items = html_list[i].find_elements(By.TAG_NAME, "li")
			for j in range(len(items)):
				if (i,j) in item_to_buy:
					if(item_to_buy[(i,j)] > 0):
						print((i,j))
						print("quantity to buy: ", item_to_buy[(i,j)])
						button = items[j].find_elements(By.TAG_NAME, "button")
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
		purchaseButton = driver.find_elements(By.CLASS_NAME, "fs-c-button--purchaseHere")
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
			closeButton = driver.find_elements(By.CLASS_NAME, 'iziToast-close')
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
			Cash_on_delivery_button = driver.find_element(By.XPATH, ("//label[@for='fs_input_payment_cashOnDelivery']"));
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
				confirmButton = driver.find_elements(By.CLASS_NAME, "fs-c-button--confirmOrder")
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
		clearButton = driver.find_elements(By.CLASS_NAME, "fs-c-button--cancel--cart")
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
	options = read_options()
	print(options)
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
				clear_cart() 

		# driver.quit()
			
if __name__ == '__main__':

	program_start_time = time.time()
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
	
