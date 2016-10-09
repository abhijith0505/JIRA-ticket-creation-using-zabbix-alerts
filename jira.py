import re
import os
import sys
from jira import JIRA

#PARAMS RECEIVED FROM ZABBIX SERVER:
#sys.argv[1] = TO
#sys.argv[2] = SUBJECT
#sys.argv[3] = BODY



options_server = {'server': 'YOUR-DOMAIN-JIRA-SERVER'}

jira = JIRA(options=options_server, basic_auth=('USERNAME', 'PASSWORD'))


#Get all the issues
issues = jira.search_issues('project="PROJECT-NAME"')

flag=0

if "Recovery" in sys.argv[2]:
        extractedSubject=sys.argv[2][10:]
        for issue in issues:
                if issue.fields.summary==extractedSubject:
                        if "To Do" == str(issue.fields.status):
                                jira.transition_issue(issue, '61')
                                jira.add_comment(issue, sys.argv[3])
else:
        for issue in issues:
                if issue.fields.summary==sys.argv[2]:
                        if "Resolved For Now" == str(issue.fields.status):
                                jira.transition_issue(issue, '81')
                        if "Done" != str(issue.fields.status):
                                flag=1
                                jira.add_comment(issue, sys.argv[3])

        if(flag==0):
                jira.create_issue(project='PROJECT-NAME', summary=sys.argv[2],
                              description=sys.argv[3], issuetype={'name': 'Task'})
