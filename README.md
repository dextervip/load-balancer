Simple Load Balancer for Windows 7
==================================

This is a script python which works switching network card metrics (see http://support.microsoft.com/kb/315088 and http://support.microsoft.com/kb/258487) , making Windows 7 use two network adapters at same time.


#Usage

Open using a text editor load_balancer.py file and change values of adapterName, SecundaryAdapterName and speed_limit. 

 - adapterName - This is the name of main network adapter Ex.: Wireless Network Connection
 - SecundaryAdapterName - This is the name of secundary network adapter Ex.: Wireless Network Connection 2
 - speed_limit - This is the speed limit of main network adapter in KB/s
          
Adapter names can be seen in Control Panel > Network and Internet 

After editing, That's it, run and enjoy!
  
    python load_balancer.py
    
 Load Balancer in Action

![Statistics usage sample](http://img28.imageshack.us/img28/259/sampleloadbalancer.png)
  
#Requirements

  - Python 2.6+ Installed 
  
#Limitations
	
It only works for two network adapters;