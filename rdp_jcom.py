# -*- coding: cp932 -*-

"""

 [2016/11/08] Ver 1.00

"""

import webbrowser, sys, os, subprocess, time, ctypes
os.environ["PATH"] += "C:\\Windows\\System32;C:\\Program Files\\Internet Explorer;"

def rdp_con(svr, mbox):
    cmd = '"C:\\Windows\\System32\\mstsc.exe" /f /v:'
    con = cmd + svr
    
    rep = mbox(None, svr + u' �֐ڑ����܂��� ?', u'�m�F', 4)
    if rep == 6:
        try:
            proc = subprocess.check_output(con, shell = True)
            sys.exit()
            
        except:
            rep = mbox(None, u'�ڑ����I�����܂����B', u'�I��', 0)
            sys.exit()
    else:
        STOP = True;
        sys.exit()
    

if __name__ == '__main__':
    svr = '10.208.67.175'
    uri = 'http://131.248.238.28/66.9/remote/herodb/herodb.cgi?table=remote_kanshi_jcom'
    
    mbox = ctypes.windll.user32.MessageBoxW
    rep = mbox(None, u'�����[�g�A�N�Z�X�Ǘ��䒠���L�ڂ��܂��� ?', u'Check', 4)
    if rep == 6:
        webbrowser.open(uri)
        time.sleep(30)
        rdp_con(svr, mbox)
        
    elif rep == 7:
        rdp_con(svr, mbox)
        
    else:
        STOP = True;
        sys.exit()
