# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 23:28:09 2021

@author: User
"""

import pyautogui

print("Current Mouse Position:",pyautogui.position()) #커서위치확인

#pyautogui.screenshot('./test.png',region=(14,144,500,300)) #region= 커서위치x,y& x,y길이