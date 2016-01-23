# _*_ coding: utf-8 _*_
#
# Zabbix 2.x用
#
def createxml():
	import sys
	xmlfile = str(sys.argv[1]).split('.')[0] + '.xml'
	
	# 作成日
	from datetime import datetime,date
	date = str(datetime.today()).split('.')[0]
	day = date.split(' ')[0]
	time = 'T' + date.split(' ')[1] + 'Z'
	# print day + time
	
	# xmlノード作成
	from xml.etree.ElementTree import Element, SubElement, Comment, tostring, dump, parse, ElementTree
	from xml.dom import minidom
	
	
	# ルート
	zabbix = Element('zabbix_export')
	
	# バージョン
	version = SubElement(zabbix, 'version')
	version.text = '2.0'
	
	# 日付
	date = SubElement(zabbix, 'date')
	date.text = day + time
	
	# グループ
	groups = SubElement(zabbix, 'groups')
	group = SubElement(groups, 'group')
	groupname = SubElement(group, 'name')
	groupname.text = u'管理テンプレート'
	
	# テンプレート
	templates = SubElement(zabbix, 'templates')
	template = SubElement(templates, 'template')
	templatechild = SubElement(template, 'template')
	templatechild.text = 'KKB_kanri_Template_StorageUseSB'
	
	templatename = SubElement(template, 'name')
	templatename.text = 'KKB_kanri_Template_StorageUseSB'
	
	templategroups = SubElement(template, 'groups')
	templategroupschild = SubElement(groups, 'group')
	templategroupname = SubElement(templategroupschild, 'name')
	templategroupname.text = u'管理テンプレート'
	
	templateapplications = SubElement(template, 'applications')
	templateapplicationschild = SubElement(templateapplications, 'application')
	templateapplicationname = SubElement(templateapplicationschild, 'name')
	templateapplicationname.text = 'RESOURCE'
	
	
	# アイテム
	templateitems = SubElement(template, 'items')
	item = SubElement(templateitems, 'item')
	
	itemname = SubElement(item, 'name')       # 可変
	itemname.text = 'AAAAAA'
	
	type = SubElement(item, 'type')           # 可変
	type.text = '0'
	
	snmpcommunity = SubElement(item, 'snmp_community')
	
	multiplier = SubElement(item, 'multiplier')
	multiplier.text = '0'
	
	snmpoid = SubElement(item, 'snmp_oid')
	
	key = SubElement(item, 'key')             # 可変
	key.text = 'BBBBB'
	
	delay = SubElement(item, 'delay')
	delay.text = '43200'
	
	history = SubElement(item, 'history')
	history.text = '90'
	
	trends = SubElement(item, 'trends')
	trends.text = '365'
	
	status = SubElement(item, 'status')
	status.text = '0'
	
	valuetype = SubElement(item, 'value_type')     # 可変
	valuetype.text = '0'
	
	allowedhosts = SubElement(item, 'allowed_hosts')
	
	units = SubElement(item, 'units')              # 可変
	units.text = 'GB'
	
	delta = SubElement(item, 'delta')
	delta.text = '0'
	
	snmpv3securityname = SubElement(item, 'snmpv3_securityname')
	
	snmpv3_securitylevel = SubElement(item, 'snmpv3_securitylevel')
	snmpv3_securitylevel.text = '0'
	
	snmpv3_authpassphrase = SubElement(item, 'snmpv3_authpassphrase')
	
	snmpv3_privpassphrase = SubElement(item, 'snmpv3_privpassphrase')
	
	formula = SubElement(item, 'formula')
	formula.text = '1'
	
	delay_flex = SubElement(item, 'delay_flex')
	
	params = SubElement(item, 'params')            # 可変
	#if param != None
	#	params.text = 'CCCCC'
	
	ipmi_sensor = SubElement(item, 'ipmi_sensor')
	
	data_type = SubElement(item, 'data_type')
	data_type.text = '0'
	
	authtype = SubElement(item, 'authtype')
	authtype.text = '0'
	
	username = SubElement(item, 'username')
	
	password = SubElement(item, 'password')
	
	publickey = SubElement(item, 'publickey')
	
	privatekey = SubElement(item, 'privatekey')
	
	port = SubElement(item, 'port')
	
	description = SubElement(item, 'description')
	
	inventory_link = SubElement(item, 'inventory_link')
	inventory_link.text = '0'
	
	applications = SubElement(item, 'applications')
	application = SubElement(applications, 'application')
	applicationname = SubElement(application, 'name')
	applicationname.text = 'RESOURCE'
	
	valuemap = SubElement(item, 'valuemap')
	
	
	
	#dump(zabbix)
	#print tostring(zabbix).encode('utf-8')
	
	# xmlファイル書き込み
	#tree = ElementTree(zabbix)
	#tree.write(xmlfile, 'UTF-8', 'True') #改行なし
	
#	f = open(xmlfile, 'w')
	tree = minidom.parseString(tostring(zabbix)).toprettyxml().encode('utf-8')
	print tree
#	f.write(tree)
#	f.close()


if __name__ == '__main__':
	createxml()
