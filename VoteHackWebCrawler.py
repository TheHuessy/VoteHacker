#URL to land on: 'https://www.poll-maker.com/poll2213211x54D342cd-63'

from selenium.webdriver import Firefox
import time
import random

#url where the poll is located
p_m = 'https://www.poll-maker.com/poll2213211x54D342cb-63'

#The button we want to vote for
xbut = '//input[@type="radio" and @name="qp_v2213211" and @value="1"]'

#The submit button
vbut = '//input[@type="submit" and @name="qp_b2213211"]'

#Set a sort of counter to decrease until 0 from 1000
#Means we will be voting 1000 times
voting = 1000

#open firefox
browser = Firefox()
#minimize the window instantly so no one from work can see that you're cheating if they walk by
##NOTE, it turned out that other people in the office were mannually cheating, whereas I was the only one cheating nobley
browser.minimize_window()

#Set up a while loop that will keep voting until we reach voting = 0

while voting > 0:
    #navigate to poll page
    browser.get(p_m)
    #point to the correct button to vote
    butt = browser.find_element_by_xpath(xbut)
    #click the button
    butt.click()
    #point to the submit button
    vbutt = browser.find_element_by_xpath(vbut)
    #click the submit button
    vbutt.click()            
    #decrease our vote counter
    voting = voting -1
    #put a random pause in it before it reiterates
    time.sleep(random.randint(1,3))

#close the window
browser.quit()
    
