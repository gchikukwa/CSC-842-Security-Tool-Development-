
#Gerald Chikukwa 
#This script detects all live hosts on a network in which the machine that is running it is attached.
import os
import socket    
import multiprocessing
import subprocess
import os

#find host IP address
def get_host_ip():
   
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

#ping ip addresses
def ping_ips(job_queue, results_queue):
    
    DEVNULL = open(os.devnull, 'w')
    while True:

        ip = job_queue.get()

        if ip is None:
            break

        try:
            subprocess.check_call(['ping', '-c1', ip],
                                  stdout=DEVNULL)
            results_queue.put(ip)
        except:
            pass

# Map the network / return list of valid addresses 
def map_network(pool_size=255):
    
    ip_list = list()

    # get host IP, cconstruct it like 192.168.1.xxx
    ip_parts = get_host_ip().split('.')
    base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'

    # queueing jobs
    jobs = multiprocessing.Queue()
    results = multiprocessing.Queue()

    ip_pool = [multiprocessing.Process(target=ping_ips, args=(jobs, results)) for i in range(pool_size)]

    for p in ip_pool:
        p.start()

    # ping processes range
    for i in range(1, 255):
        jobs.put(base_ip + '{0}'.format(i))

    for p in ip_pool:
        jobs.put(None)

    for p in ip_pool:
        p.join()

    # return IP addess list 
    while not results.empty():
        ip = results.get()
        ip_list.append(ip)

    return ip_list


if __name__ == '__main__':

    print('Mapping Active IP Addresses...')
    lst = map_network()
    print(lst)
    

