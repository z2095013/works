# -*- coding: utf-8 -*-


def zabA(tree):
	##### ホストステータス
	# 
	hosttree = tree.find('hosts/host')
	hostname = hosttree.get('name')
	#print hostname
	
	hosts = tree.find('hosts/host/status')
	hoststatus = hosts.text
	#print hoststatus
	
	print '''
### ホスト'''
	if hoststatus == '1':
		print hostname + ' : ' + u'無効'
	else:
		print hostname + ' : ' + u'有効'
	
	##### ツリー構造
	# triggerツリー
	print '''
### トリガー '''
	triggers = tree.findall('hosts/host/triggers/trigger')
	for t in triggers:
	
	###
	# トリガー名
		name = t.findall('./description')
		for n in name:
			tname = n.text
	###
	# status
		stat = t.findall('./status')
		for s in stat:
			tstat = s.text
	###
	# プリント
		if tstat == '0':
			print tname + ' : ' + u'有効'
	#	else:
	#		print tname + ' : ' + u'無効'
	
	##### ツリー構造
	# templateツリー
	print '''
### アイテム '''
	items = tree.findall('hosts/host/items/item')
	for i in items:
	
	###
	# アイテム名
		name = i.findall('./description')
		for n in name:
			iname = n.text
	###
	# status
		stat = i.findall('./status')
		for s in stat:
			istat = s.text
	###
	# プリント
		if istat == '1':
			print tname + ' : ' + u'無効'
	#	else:
	#		print tname + ' : ' + u'有効'


def zabB(tree):
	##### ホストステータス
	# 
	host = tree.find('hosts/host/name')
	#hostname = host.text
	#print hostname
	
	hosts = tree.find('hosts/host/status')
	hoststatus = hosts.text
	#print hoststatus
	
	print '''
### ホスト'''
	if hoststatus == '1':
		print hostname + ' : ' + u'無効'
	else:
		print hostname + ' : ' + u'有効'
	
	##### ツリー構造
	# triggerツリー
	print '''
### トリガー '''
	triggers = tree.findall('triggers/trigger')
	for t in triggers:
	
	###
	# トリガー名
		name = t.findall('./name')
		for n in name:
			tname = n.text
	###
	# status
		stat = t.findall('./status')
		for s in stat:
			tstat = s.text
	###
	# プリント
		if tstat == '0':
			print tname + ' : ' + u'有効'
	#	else:
	#		print tname + ' : ' + u'無効'
	
	##### ツリー構造
	# templateツリー
	print '''
### アイテム '''
	items = tree.findall('hosts/host/items/item')
	for i in items:
	
	###
	# アイテム名
		name = i.findall('./name')
		for n in name:
			iname = n.text
	###
	# status
		stat = i.findall('./status')
		for s in stat:
			istat = s.text
	###
	# プリント
		if istat == '1':
			print tname + ' : ' + u'無効'
	#	else:
	#		print tname + ' : ' + u'有効'

def zabbix():
	import sys
	from xml.etree.ElementTree import Element, SubElement, Comment, tostring, dump, parse, ElementTree
	
	file = sys.argv[1]
	
	# ファイルを指定
	tree = parse(file)
	#dump(tree)
	
	### バージョン差分
	# Zabbixバージョン確認
	ver = tree.find('./version')
	if ver == None:
		zabA(tree)
	else:
		zabB(tree)


if __name__ == '__main__':
	zabbix()
