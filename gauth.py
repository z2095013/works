# -*- coding: cp932 -*-

"""

 [2016/10/18] Ver 1.01
 [2016/10/28] Ver 1.02 - �����A�N�䒠 �m�F���b�Z�[�W�ǉ�

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
            self.rep = self.mbox(None, u'���ɒN�����ڑ����Ă܂�', u'����', 0)
            sys.exit()
            
        except:
            self.rep = self.mbox(None, u'�ڑ����Ă��܂���B�Đڑ�����ꍇ�́A�ݔ�������I�����Ă�������', u'�G���[', 0)
            
    
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
        self.label = Label(text = u'�ڑ���(�ݔ�)��I�����Ă�������', font=(u'�l�r ����', 10), bg = 'green').pack()
        self.n = IntVar()
        self.n.set(0)
        self.name_table = (u'A�ݔ�', u'B�ݔ�', u'C�ݔ�')
        for m, name in enumerate(self.name_table):
            Radiobutton(self.root, text = name, font=(u'�l�r �S�V�b�N', 14), variable = self.n, value = m).pack()
        Button(self.root, text = 'OK', font=(u'�l�r �S�V�b�N', 12), command = lambda: self.ele_get()).pack(fill = 'both')
        self.root.mainloop()



if __name__ == '__main__':
    mbox = ctypes.windll.user32.MessageBoxA
    rep = mbox(None, '�����[�g�A�N�Z�X�Ǘ��䒠���L�ڂ��܂����� ?', 'Check', 4)
    if rep == 6:
        run = OneTime()
        run.service_select()
        
    elif rep == 7:
        mbox(None, '�I����Ƀ����[�g�A�N�Z�X�Ǘ��䒠���L�ڂ��Ă��������B', '�x��', 0)
        run = OneTime()
        run.service_select()
        
    else:
        STOP = True;
        sys.exit()
