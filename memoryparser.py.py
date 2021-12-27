'''This memory parsing tool parses a Cisco WebEx memory dump to extract memory artifacts enumerated in the code.

Dependencies include 1) Python, 2) Linux's strings.exe and 3) grep.
The subject tool is to be executed on a Linux Operating System with python installed.
'''

import subprocess
import sys
def extraction(command):
    p = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE)
    while True:
        out = p.stderr.read(1)
        decoded=out.decode()
        if decoded == '' and p.poll() != None:
            break
        if decoded != '':
            sys.stdout.write(decoded)
            sys.stdout.flush()
print('''1. User Account Information
2. Search Keywords
3. Text Files and Media Files Exchanged
4. URLs Exchanged
5. URLs Exchanged Deleted
6. Chat Messages
7. Chat Messages Deleted
8. Scheduled Meetings
9. Contacts''')
print('Extrating artifacts...')
extraction("strings memdump.mem | grep 'Personal Room' > UserAccountInformation.txt")
extraction("strings memdump.mem | grep 'query' > SearchKeywords.txt")
extraction("strings memdump.mem | grep 'sparkShareInfo' > TextFilesandMediaFilesExchanged.txt")
extraction("strings memdump.mem | grep 'a href' > URLsExchanged.txt")
extraction("strings memdump.mem | grep '[]' > URLsExchangedDdeleted.txt")
extraction("strings memdump.mem | grep 'sparkMessageGroup' > ChatMessages.txt")
extraction("strings memdump.mem | grep '<p>' > ChatMessagesDeleted.txt")
extraction("strings memdump.mem | grep 'WebExMeetingData' > ScheduledMeetings.txt")
extraction("strings memdump.mem | grep '/spark-contact' > Contacts.txt")
print('done')
