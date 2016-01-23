# -*- coding: utf-8 -*-

import sys
import xml.etree.ElementTree as et

file = sys.argv[1]

def zabA():
	#####
	# itemツリーを取得
	items = tree.findall('hosts/host/items/item')
	for i in items:
	###
	# アイテム名を取得
		iname = i.findall('./description')
		for n in iname:
			name = n.text
	#		print n.text	# 出力
	###
	# SNMPOIDを取得
		ioid = i.findall('./snmp_oid')
		for o in ioid:
			oid = o.text
	#		print type(oid)	# 出力
	#		print oid	# 出力
	###
	# キーを取得
		ikey = i.get('key')
	#	print ikey	# 出力
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
		for c in idelay:
			delay = c.text
	###
	# history
		ihistory = i.findall('./history')
		for c in ihistory:
			history = c.text
	###
	# trend
		itrends = i.findall('./trends')
		for c in itrends:
			trends = c.text
	###
	# 
		idelta = i.findall('./delta')
		for c in idelta:
			delta = c.text
	###
	# status
		istatus = i.findall('./status')
		for c in istatus:
			status = c.text

	###
	# アイテムとキーを出力
	#	print name + ',' + str(oid) + ',' + ikey
	#	print name + ',' + ikey
		item = [name,oid,ikey]
	#####
	# itemツリーを取得
	triggers = tree.findall('hosts/host/triggers/trigger')
	for t in triggers:
	###
	# トリガー名を取得
		tname = t.findall('./description')
		for n in tname:
	#		print n.text	# 出力
			triname = n.text
	# expressionを取得
		exp = t.findall('./expression')
		for n in exp:
	#		print n.text	# 出力
			expression = n.text
	###
	# トリガーを出力
		print triname + ',' + expression
		trigger = [triname,expression]

def zabB():
	#####
	# itemツリーを取得
	items = tree.findall('hosts/host/items/item')
	for i in items:
	###
	# アイテム名を取得
		iname = i.findall('./name')
		for n in iname:
			name = n.text
	#		print n.text	# 出力
	###
	# タイプを取得
		type = i.findall('./type')
		for t in type:
	#		print t.text	# 出力
			itype = t.text
	###
	# キーを取得
		key = i.findall('./key')
		for k in key:
	#		print k.text	# 出力
			ikey = k.text
	###
	# SNMPOIDを取得
		ioid = i.findall('./snmp_oid')
		for o in ioid:
			oid = o.text
	#		print type(oid)	# 出力
	#		print oid	# 出力
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
                for c in idelay:
                        delay = c.text
        ###
        # history
                ihistory = i.findall('./history')
                for c in ihistory:
                        history = c.text
        ###
        # trend
                itrends = i.findall('./trends')
                for c in itrends:
                        trends = c.text
        ###
        #
                idelta = i.findall('./delta')
                for c in idelta:
                        delta = c.text
        ###
        # status
                istatus = i.findall('./status')
                for c in istatus:
                        status = c.text

	###
	# アイテムとキーを出力
		print name + ',' + itype + ',' + ikey
        #        print name + ',' + oid + ',' + ikey + ',' + units + ',' + multiplier + ',' + formula + ',' + delay + ',' + history + ',' + trends + ',' + delta + ',' + status
		item = [name,oid,ikey]
	#####
	# itemツリーを取得
	triggers = tree.findall('triggers/trigger')
	for t in triggers:
	###
	# トリガー名を取得
		tname = t.findall('./name')
		for n in tname:
	#		print n.text	# 出力
			triname = n.text
	# expressionを取得
		exp = t.findall('./expression')
		for n in exp:
	#		print n.text	# 出力
			expression = n.text
	###
	# トリガーを出力
	#	print triname + ',' + expression
		trigger = [triname,expression]


# ファイルを指定
tree = et.parse(file)

# 要素の検索 ツリーの順を定義
#temp1 = tree.find('./templates')
#temp2 = temp1.find('./template')
#temp3 = temp2.find('./items')
#
# アイテムタグを取得
#temp = tree.find('hosts/host/items/item')
#tags =  temp.getchildren()
#for itag in tags:
#	print itag.tag	# 出力

# Zabbixバージョン確認
ver = tree.find('./version')
if ver == None:
	zabA()
else:
	zabB()
