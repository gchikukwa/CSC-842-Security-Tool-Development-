<h1>Remote Command Execution C2</h1>

The tool is a client and server remote command execution C2 . The main purpose of the tool is to demonstrate how command and control 
works BUT my goal was to run commands from the server to the client machine , once the commands have been executed on the client machine
the results are displayed on the server.

<b>Server</b>: The server is always listening for a connection from the client. Once the connection is established , you can run command from 
the server.

<b>Client</b> : The client connects to the server and receives command and executes them ,then send back the results of the command to be 
displayed on the server side.

<h2>Technical Spefications</h2>

*  Python 3 and above <br>
*  Linux Platform  

<h3>Instructions</h3>

* This tool was programmed using python 3.5 on a linux machine. <br>
* It will not run on a windows machine <br>
* You have to run the server first followed by the client(since the client connects to the server)  <br><br>
<b> $python server.py </b>  <br><br>
<b>$python client.py </b>

<h3>Future Direction</h3>

* To encrypt the communication between the client and server

