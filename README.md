---------

Tired of manually creating JIRA issues for every issue you receive from Zabbix (or any other monitoring tool)?
Automate the issue creation using this script as your custom alert script in zabbix.

----------
```
If Zabbix sends out an alert:
	if status is "Resolved For Now":
		changes status to "To-Do"
	if status is not "Done":
		adds the new alert body as a comment to existing issue

if Zabbix sends out a Recovery message:
	for all issues:
		if issue exists in jira issues:
			if status is "To-Do":
				changes status to "Done"

if issue not found in jira:
	creates a new issue
```
----------


Prerequisite
-------------------


* **$ git clone** the repository.

	` $ git clone https://github.com/abhijith0505/JIRA-ticket-creationg-using-zabbix-alerts.git`

* Install the required modules using,

	`$ pip install -r requirements.txt`

> If you do not have pip installed, install it using:  
	> `$ easy_install pip`

 

Usage
-------------------

- Create a custom alert-script in your Zabbix server that uses this **jira.py**.
 > **Note:**
        Refer this link to make custom alert-script.
> https://www.zabbix.com/documentation/3.4/manual/config/notifications/media/script
> But we'll be using our own script instead of the example script given.

- While adding the created *Media type* (using the alert-script) to an event, make sure that you enable the Recovery message in the Action.
>**Note:**
	>Refer this link for more help.
	>https://www.zabbix.com/documentation/2.2/manual/config/notifications/action

- Create a **JIRA** administrator account that you'll be using to authenticate the script's API calls.

 > **Note:**
        Ideally, create a JIRA project and use this project to populate your issues from zabbix.
        > That way, you can easily keep track of non-zabbix issues too.


#LICENSE

```
MIT License

Copyright (c) 2016 Abhijith C

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

