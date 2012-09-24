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
  - run as administrator
  
#Limitations
	
It only works for two network adapters;

#License

Simple Load Balancer for Windows 7
Copyright (C) 2012  Rafael Amorim 

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.