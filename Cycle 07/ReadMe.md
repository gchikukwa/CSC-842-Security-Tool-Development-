
<h1>Cycle 07 </h1>
<h2>Purpose</h2>
This script detects all live hosts on a network in which the machine that is running it is attached. I took the commennts I got from from Cycle 01 and rebuilt the script. The first script had a few lines of code , hardcoded ip's and it was not using multiprocessing or threading.

New Script has the following functions  :
def get_host_ip()
def ping_ips(job_queue, results_queue)
def map_network(pool_size = 255)
