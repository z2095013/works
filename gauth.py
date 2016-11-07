# -*- coding: cp932 -*-

"""

 [2016/10/18] Ver 1.01
 [2016/10/28] Ver 1.02 - リモアク台帳 確認メッセージ追加

"""

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from Tkinter import Tk, Label, IntVar, Radiobutton, Button
import base64, sys, os, subprocess, time, ctypes

os.environ["PATH"] += "C:\\Program Files\\Mozilla Firefox;C:\\Program Files\\Cisco Systems\\VPN Client;"


class OneTime:
    ''' This is a instance of onetime password '''
    
    def __init__(self):
        pass
        
    
    def vpn_con(self, target='NULL'):
        self.cmd = '"C:\\Program Files\\Cisco Systems\\VPN Client\\vpngui.exe" -c -sd'
        self.otp = str(self.target)
        self.entry = self.ent.encode('cp932')
        
        if self.otp != 'NULL':
            self.con = self.cmd + self.usr + self.pwd + self.otp + self.entry
            
        else:
            self.con = self.cmd + self.usr + self.pwd + self.entry
        
        self.mbox = ctypes.windll.user32.MessageBoxW
        
        try:
            self.proc = subprocess.check_output(self.con, shell = True)
            
        except subprocess.CalledProcessError:
            self.rep = self.mbox(None, u'既に誰かが接続してます', u'注意', 0)
            sys.exit()
            
        except:
            self.rep = self.mbox(None, u'接続していません。再接続する場合は、設備名から選択してください', u'エラー', 0)
            
    
    def fx_crow(self, uri):
        self.binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        self.driver = webdriver.Firefox(executable_path="geckodriver.exe", firefox_binary=self.binary)
        self.driver.set_window_size(100, 320)
        
        self.driver.get(uri)
        
        ''' timer '''
        self.timer = self.driver.find_element_by_id('updatingIn')
        self.wait = self.timer.text
        
        while str(self.wait) == '..':
            time.sleep(1)
            self.wait = self.timer.text
        
        while int(self.wait) < 9:
            time.sleep(1)
            self.wait = self.timer.text
            
        ''' password '''
        self.password = self.driver.find_element_by_class_name('ui-li-heading')
        self.target = self.password.text
        self.driver.quit()
        
        return self.target
        
    
    def ele_get(self):
        self.val = self.n.get()
        self.cur = os.getcwd()
        if self.val == 0:
            self.uri = 'file:///' + self.cur.replace("\\", "/").replace("dist", "") + 'index_a.html'
            self.usr = ' -user XXXXX'
            self.pwd = ' -pwd XXXXX'
            self.ent = u' "XXXXXXXXXX"'
            self.fx_crow(self.uri)
            
        elif self.val == 1:
            self.uri = 'file:///' + self.cur.replace("\\", "/").replace("dist", "") + 'index_b.html'
            self.usr = ' -user XXXXX'
            self.pwd = ' -pwd XXXXX'
            self.ent = u' "XXXXXXXXXX"'
            self.fx_crow(self.uri)
            
        elif self.val == 2:
            self.uri = 'None'
            self.usr = ' -user XXXXX'
            self.pwd = ' -pwd XXXXX'
            self.ent = u' "XXXXXXXXXX"'
            self.target = 'NULL'
            
        else:
            print('NG')
        
        self.vpn_con()
    
    def service_select(self):
        self.root = Tk()
        self.label = Label(text = u'接続先(設備)を選択してください', font=(u'ＭＳ 明朝', 10), bg = 'green').pack()
        self.n = IntVar()
        self.n.set(0)
        self.name_table = (u'A設備', u'B設備', u'C設備')
        for m, name in enumerate(self.name_table):
            Radiobutton(self.root, text = name, font=(u'ＭＳ ゴシック', 14), variable = self.n, value = m).pack()
        Button(self.root, text = 'OK', font=(u'ＭＳ ゴシック', 12), command = lambda: self.ele_get()).pack(fill = 'both')
        self.root.mainloop()



if __name__ == '__main__':
    mbox = ctypes.windll.user32.MessageBoxA
    rep = mbox(None, 'リモートアクセス管理台帳を記載しましたか ?', 'Check', 4)
    if rep == 6:
        run = OneTime()
        run.service_select()
        
    elif rep == 7:
        mbox(None, '終了後にリモートアクセス管理台帳を記載してください。', '警告', 0)
        run = OneTime()
        run.service_select()
        
    else:
        STOP = True;
        sys.exit()
