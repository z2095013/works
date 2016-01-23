# -*- coding: utf-8 -*-

class zabbix:

	def zabA():
		##### アイテムツリー構造
		# itemツリー
		items = tree.findall('hosts/host/items/item')
		for i in items:
		###
		# アイテム名
			iname = i.findall('./description')
			for n in iname:
				name = n.text
		###
		# キー
			ikey = i.get('key')

		print name + ',' + oid


	def zabB():
		##### アイテムツリー構造
		# itemツリー
		items = tree.findall('hosts/host/items/item')
		for i in items:
		###
		# アイテム名
			iname = i.findall('./name')
			for n in iname:
				name = n.text
		###
		# キー
			key = i.findall('./key')
			for k in key:
				ikey = k.text


	def zabbix():
		import sys
		import xml.etree.ElementTree as et
		
		file = sys.argv[1]
		
		# ファイルを指定
		tree = et.parse(file)
		
		##### アイテムツリー構造
		# itemツリー
		items = tree.findall('hosts/host/items/item')
		for i in items:
		###
		# アイテムタグ
		#temp = tree.find('hosts/host/items/item')
		#itags =  temp.getchildren()
		#for itag in itags:
		#	print itag.tag  # 出力
		#	tags = i.findall(itag.tag)
		###
		# タグの値取得
		#	for data in tags:
		#		row = data.text
		#		print row
		###
		# SNMPOID
			ioid = i.findall('./snmp_oid')
			for c in ioid:
				oid = c.text
		###
		# 単位
			iunits = i.findall('./units')
			for c in iunits:
				units = c.text
		###
		# 乗数
			imultiplier = i.findall('./multiplier')
			for c in imultiplier:
				multiplier = c.text
			iformula = i.findall('./formula')
			for c in iformula:
				formula = c.text
		###
		# 更新間隔
			idelay = i.findall('./delay')
			for c in delay:
				delay = c.text
		###
		# ヒストリの保存期間
			ihistory = i.findall('./history')
			for c in history:
				history = c.text
		###
		# トレンドの保存期間
			itrends = i.findall('./trends')
			for c in itrends:
				trends = c.text
		###
		# 保存の計算
			idelta = i.findall('./delta')
			for c in idelta:
				delta = c.text
		###
		# ステータス
			istatus = i.findall('./status')
			for c in istatus:
				status = c.text

		### バージョン差分
		# Zabbixバージョン確認
		ver = tree.find('./version')
		if ver == None:
			zabA(tree)
		else:
			zabB(tree)



if __name__ == '__main__':
	zabbix()
