# coding=utf-8
"""

__created__ =  2017/5/4 15:48
__author__ = 'baishaohua'
# @Site    : https://github.com/bashhu
"""

# -*- coding: utf-8 -*-
"""
开发框架公用方法
1. 页面输入内容转义（防止xss攻击）
from common.utils import html_escape, url_escape, texteditor_escape
2. 转义html内容
html_content = html_escape(input_content)
3. 转义url内容
url_content = url_escape(input_content)
4. 转义富文本内容
texteditor_content = texteditor_escape(input_content)
"""


def html_escape(html, is_json=False):
    """
    Replace special characters "&", "<" and ">" to HTML-safe sequences.
    If the optional flag quote is true, the quotation mark character (")
    is also translated.
    rewrite the cgi method
    @param html: html代码
    @param is_json: 是否为json串（True/False） ，默认为False
    """
    # &转换
    if not is_json:
        html = html.replace("&", "&amp;")  # Must be done first!
    # <>转换
    html = html.replace("<", "&lt;")
    html = html.replace(">", "&gt;")
    # 单双引号转换
    if not is_json:
        html = html.replace(' ', "&nbsp;")
        html = html.replace('"', "&quot;")
        html = html.replace("'", "&#39;")
    return html


def url_escape(url):
    url = url.replace("<", "")
    url = url.replace(">", "")
    url = url.replace(' ', "")
    url = url.replace('"', "")
    url = url.replace("'", "")
    return url