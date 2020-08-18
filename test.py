# coding:utf-8
import nmap


nm = nmap.PortScanner()
nm.scan(hosts='127.0.0.1')
