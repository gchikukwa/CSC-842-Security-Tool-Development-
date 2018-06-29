
<h1>Cycle 07 </h1>
<h2>Purpose</h2>
This script detects all live hosts on a network in which the machine that is running it is attached. I took the comments and recommendations I got from from Cycle 01 and rebuilt the script. The first script had a few lines of code , hardcoded ip's and it was not using multiprocessing or threading.

<h3>New Script has the following functions  :</h3>
def get_host_ip()<br>
def ping_ips(job_queue, results_queue)<br>
def map_network(pool_size = 255)<br>

<h3>Techinical Specifications</h3>
* Python 3 and above <br>
* Linux Platform <br>

<h3>Instructions</h3>
* This script will only run on linux machines <br>
* Run the script has following :<br>
$python networkscope.py 
