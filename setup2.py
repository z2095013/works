# -*- coding: utf-8 -*- 

from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

wd_path = 'C:\\Python27\\Lib\\site-packages\\selenium\\webdriver'
required_data_files = [('selenium/webdriver/firefox',
                        ['{}\\firefox\\webdriver.xpi'.format(wd_path), '{}\\firefox\\webdriver_prefs.json'.format(wd_path)])]

option = {
    'skip_archive': True,
    'unbuffered': True,
    'optimize': 2
}

setup(
    data_files = required_data_files,
    options = {'py2exe': option},
    console=['gauth.py']
    )

