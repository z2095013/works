# -*- coding: cp932 -*-

"""

 [2016/11/08] Ver 1.00

"""

import webbrowser, sys, os, subprocess, time, ctypes
os.environ["PATH"] += "C:\\Windows\\System32;C:\\Program Files\\Internet Explorer;"

def rdp_con(svr, mbox):
    cmd = '"C:\\Windows\\System32\\mstsc.exe" /f /v:'
    con = cmd + svr
    
    rep = mbox(None, svr + u' へ接続しますか ?', u'確認', 4)
    if rep == 6:
        try:
            proc = subprocess.check_output(con, shell = True)
            sys.exit()
            
        except:
            rep = mbox(None, u'接続を終了しました。', u'終了', 0)
            sys.exit()
    else:
        STOP = True;
        sys.exit()
    

if __name__ == '__main__':
    svr = '10.208.67.175'
    uri = 'http://131.248.238.28/66.9/remote/herodb/herodb.cgi?table=remote_kanshi_jcom'
    
    mbox = ctypes.windll.user32.MessageBoxW
    rep = mbox(None, u'リモートアクセス管理台帳を記載しますか ?', u'Check', 4)
    if rep == 6:
        webbrowser.open(uri)
        time.sleep(30)
        rdp_con(svr, mbox)
        
    elif rep == 7:
        rdp_con(svr, mbox)
        
    else:
        STOP = True;
        sys.exit()
