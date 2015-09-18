#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import urllib
from optparse import OptionParser

def get_html(url):
    try:
        page = urllib.urlopen(url)
        html = page.read()
        return html
    except IOError as error:
        print "get html failed: %s" % str(error)
    return ""


def get_img(html, pic_type_list):
    for pic_type in pic_type_list:
        # print html
        img_reg = r'http[^ ]+\.'+pic_type
        p_img_reg = re.compile(img_reg, re.I)
        url_list = re.findall(p_img_reg, html)
        # print url_list
        index = 0
        for one_url in url_list:
            index += 1
            dst_name = "imag%d.%s" % (index, pic_type)
            print "downloading %s to %s" % (one_url, dst_name)
            try:
                urllib.urlretrieve(one_url, dst_name)
            except Exception as err:
                print "error: %s" % str(err)



ut = "http://www.duba.com/?f=liebaontc"


if __name__ == "__main__":
    parser = OptionParser(usage="usage: %prog [options] arg1")
    parser.add_option("-u", "--url", dest="url", help="url addr", default="")
    # parser.add_option("-o", "--once", action="store_true", dest="once", default=False, help="do sync once, then exit")
    (options, sys.argv) = parser.parse_args()

    if len(options.url) < 1:
        sys.exit(0)
    else:
        get_img(get_html(options.url), ["jpg", "png", "gif"])

