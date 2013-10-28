import xmltodict
from collections import defaultdict,OrderedDict
from gzip import GzipFile


def extract_vendor_product_version(line):
	return line.split(':')[2:]


def handle_nvd(_,item):
	if 'vuln:references' in item: 
			for i in item['vuln:references']:
				if 'vuln:source' in i and type(i) == OrderedDict:
					if i['@reference_type'] == 'VENDOR_ADVISORY':
						print item['vuln:cve-id']
						if 'vuln:vulnerable-software-list' in item:
							if type(item['vuln:vulnerable-software-list']['vuln:product']) == list:
								 print [ extract_vendor_product_version(prod) for prod in item['vuln:vulnerable-software-list']['vuln:product'] ]
							else:
								print extract_vendor_product_version(item['vuln:vulnerable-software-list']['vuln:product'])
	return True


items = xmltodict.parse(GzipFile('cve.xml.gz'),item_depth=2,item_callback=handle_nvd)
