# coding: utf-8
# from Fizz.plugins import db_handle
from queue import Queue
import nmap
import threading

'''
    端口扫描子任务，根据获取的子域名分发进行端口扫描，返回新增端口和所有结果
'''

lock = threading.Lock()


class MyThread(threading.Thread):

    def __init__(self, func, args):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result  # 如果子线程不使用join方法，此处可能会报没有self.result的错误
        except Exception as e:
            return e


def port_scan(target, options, ports) -> list:
    # 子域名表外键id
    global lock
    _res = []
    print("开始扫描端口: {}".format(ports))
    # 1
    # subdomain_id = SubDomain.objects.get(pk=target).subdomain
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments=options, ports=ports)
    # 处理结果
    try:
        for host in nm.all_hosts():
            # 判断host是否up
            if nm[host]['status']['state'] == 'up':
                for port in nm[host]['tcp']:
                    # 判断端口是非open
                    if nm[host]['tcp'][port]['state'] == 'open':
                        db_dict = {'port': port,
                                   'state': 'open',
                                   'product': nm[host]['tcp'][port]['product'],
                                   'ip': nm[host]['addresses']['ipv4'],
                                   'version': nm[host]['tcp'][port]['version'],
                                   'name': nm[host]['tcp'][port]['name'],
                                   }
                        # with lock:
                        #     print(db_dict)
                        #     _res.append(db_dict)
                        #     db_handle.handle_port(subdomain=target, **db_dict)
                        #     pass
                    else:
                        pass
            else:
                print("[!] host is down")
                pass
        print("[+]扫描完了: {}".format(ports))
        return _res

    except Exception as e:
        print("[x]扫描完了，无结果: {}".format(ports))
        return _res


def run(targets, options) -> list:
    result = list()
    q = Queue()
    for i in range(1, 65536, 1285):
        q.put('{}'.format(i)+'-'+'{}'.format(i+1284))
    threads = [MyThread(port_scan, (targets, options, q.get(), ))
               for i in range(1)]
    list(map(lambda x: x.start(), threads))
    for t in threads:
        t.join()
        if t.get_result():
            result.append(t.get_result())
            print(result)
    return result


if __name__ == '__main__':
    targets = 'www.allsec.cn'
    options = '-sV –host-timeout 200'
    ports = '22, 80'
    # a = port_scan(targets, options, ports)
    a = run(targets, options)
    print("结果：{}".format(a))
