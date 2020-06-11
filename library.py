#!/usr/bin/python
#filename    : library 
#aurthor     : ashish varshney


# import necessary modules
from tkinter import *
from selenium import webdriver
import logging
import time

from action import *
from gui import *


logging.basicConfig(format='%(message)s', filename='debug.log', level=logging.ERROR)