# -*- coding: utf-8 -*-


def zabA(tree):
	##### ツリー構造
	# templateツリー
	items = tree.findall('hosts/host/items/item')
	for i in items:
	
	###
	# アイテム名
		name = i.findall('./description')
		for n in name:
			iname = n.text
	###
	# キー
		ikey = i.get('key')

	###
	# param
		params = i.findall('./params')
		for p in params:
			iparams = p.text
			if iparams == None:
				iparams = '-'
			#print type(iparams)
	###
	# プリント
		print iname + '@@@@@' + ikey
	#	print iname + '@@@@@' + ikey + '@@@@@' + iparams
	
	##### ツリー構造
	# triggerツリー
	triggers = tree.findall('hosts/host/triggers/trigger')
	for t in triggers:
	
	###
	# トリガー名
		name = t.findall('./description')
		for n in name:
			tname = n.text
	
	###
	# expression
		exp = t.findall('./expression')
		for e in exp:
			texp = e.text
	###
	# プリント
	#	print tname + '@@@@@' + texp
	#	print tname


def zabB(tree):
	##### ツリー構造
	# templateツリー
	items = tree.findall('templates/template/items/item')
	for i in items:
	
	###
	# アイテム名
		name = i.findall('./name')
		for n in name:
			iname = n.text
	###
	# キー
		key = i.findall('./key')
		for k in key:
			ikey = k.text
	###
	# プリント
	#	print iname + '@@@@@' + ikey
		print ikey
	
	##### ツリー構造
	# triggerツリー
	triggers = tree.findall('triggers/trigger')
	for t in triggers:
	
	###
	# トリガー名
		name = t.findall('./name')
		for n in name:
			tname = n.text
	
	###
	# expression
		exp = t.findall('./expression')
		for e in exp:
			texp = e.text
	###
	# プリント
	#	print tname + '@@@@@' + texp
	#	print tname

def zabbix():
	import sys
	import xml.etree.ElementTree as et
	
	file = sys.argv[1]
	
	# ファイルを指定
	tree = et.parse(file)
	
	### バージョン差分
	# Zabbixバージョン確認
	ver = tree.find('./version')
	if ver == None:
		zabA(tree)
	else:
		zabB(tree)


if __name__ == '__main__':
	zabbix()
