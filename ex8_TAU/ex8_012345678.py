#####################################################
#           DO NOT DELETE THE NEXT 11 LINES         #
import time
from os.path import exists as path_ok

#Application gestures:
backup_succeeded = 'Data was backed up successfully to:\n'
backup_failed = 'Failed to backup you data. Please try again later.\n'
sending_succeeded_msg = 'Message was sent successfully!\n'
removing_succeeded_msg = 'Message was removed successfully!\n'
empty_conversation = 'Conversation either didn\'t start or all messages were removed.\n'
no_permissions_msg = 'Sorry! you are not a member of this conversation.\n'
no_such_msg = 'Message does not exist.\n'
thanks_msg = '\nThank you for using UpWhats! See you soon. Bye.\n'
#####################################################

0
class Date:
    
    def __init__(self, current_time):
        
        self.hour   = current_time[:2]
        self.minute = current_time[3:5]
        self.second = current_time[6:8]
        
    def __str__(self):           
        return (self.hour + ':' + self.minute + ':' + self.second) 



class Message:
    
    def __init__(self, sender, content, date, msg_id):
        self.sender    = sender
        self.content   = content
        self.date      = date
        self.msg_id    = msg_id

    def __len__(self):
        return len(self.content)
        
    def __str__(self):

        return ('(' + str(self.msg_id) +') ' + Date.__str__(self.date) + ' ' + self.sender +': ' + self.content)
    #cant concentrate str to date

    
class Conversation:
    
    def __init__(self, members, size_limit, backup_policy, cloud_account_prefix='./'):
        if Conversation.is_valid(self, members, size_limit, backup_policy, cloud_account_prefix='./') == None:    
            self.members              = members
            self.size_limit           = size_limit
            self.backup_policy        = backup_policy
            self.cloud_account        = cloud_account_prefix + members[0] + '.txt'
            self.size                 = 0 
            self.total_messages_sent  = 0
            self.content              = []
            
        
       
    def __len__(self):
            return len(self.content)        
        
    def __str__(self):
        strConv = ''
        for msg in self.content:
            strConv += Message.__str__(msg) + '\n'
        strConv = strConv[:-1]
        return strConv
    
    def is_valid(self, members, size_limit, backup_policy, cloud_account_prefix):
        if len(members)<2:
            raise ValueError("Must be at least 2 members in the group")
            
        if size_limit<= 10:
            raise ValueError("Maximal storage must be at least 10")
        
        if not path_ok(cloud_account_prefix):
            raise ValueError("Folder dosen't exist or ilegal!")
                             
        if  backup_policy< 1:
            raise ValueError("Backup after at least 1 message")
         
            
    def is_member(self,username):
        if username in self.members:
            return True
        
        return False
    
        
    
    def enough_space(self, msg):
        max_left = self.size_limit - self.size
        if len(msg)<=max_left:
            return True
        return False

        
    def is_empty(self):
        if len(self.content) == 0 :
            return True
        return False
           
    def time_for_backup(self):
        if self.total_messages_sent%self.backup_policy == 0:
            return True
        return False
        
    def backup_content(self):
        global backup_succeeded,backup_failed
        try:
            f = open(self.cloud_account,'w')
            f.write(Conversation.__str__(self) )
            print(backup_succeeded + self.cloud_account)
            
        except IOError:
            print(backup_failed)
            
        finally:
            f.close()
    
                 
    def get_conversation(self):
        if Conversation.is_empty(self):
            return empty_conversation
        else:
            return Conversation.__str__(self)
        
      
    def send_msg(self, username, msg_content, msg_time):
        global sending_succeeded_msg
        if not Conversation.enough_space(self, msg_content):
            raise MemoryError('There is not enought memory to send this message')
        self.total_messages_sent += 1
        self.content.append(Message(username, msg_content, msg_time, self.total_messages_sent))
        self.size += len(msg_content)
        if Conversation.time_for_backup(self):
            Conversation.backup_content(self)           
        return sending_succeeded_msg
            
    
    def find_msg_index(self, msg_id): 
        for i in range(len(self.content)):
            if self.content[i].msg_id == msg_id:
                return i
        
        return -1
   
    def delete_msg(self, msg_id_str):
        global removing_succeeded_msg
        msg_index = Conversation.find_msg_index(self,int(msg_id_str))
        if msg_index == -1:
            raise ValueError('nessage was not found - cannot delete it')
        
        self.size -= Message.__len__(self.content[msg_index])
        del self.content[msg_index]
        return removing_succeeded_msg
#####################################################
        
class Application:
    
    def __init__(self):
        '''
        Initializes the app. Think about it as an "installation".
        '''
        conversation_parameters = self.get_conversation_parameters_from_user()
        self.coversation = Conversation(*conversation_parameters)

        
    def get_conversation_parameters_from_user(self):
        '''
        Ask the user for parameters once as part of a conversation initialization.
        '''
        num_of_members = int(input('Please enter the number of members in the group.\n'))
        members = []
        for i in range(num_of_members):
            members.append(input('Please enter member number '+ str(i+1) +':\n'))
        size_limit = int(input('Please enter your storage limit (int):\n'))
        backup_policy = int(input('Please enter a desired backup policy (int):\n'))
        path = input('Please enter a file path for backing up your data:\n')
        return members, size_limit, backup_policy, path.rstrip('/') + '/'
        
    def show_options(self):
        '''
        Prints the available options to the user. Nothing is returned.
        '''
        print ('\n' + '#'*50 + '''\nWelcome to UpWhats! What would you like to do?
        [0] End conversation
        [1] Show full conversation
        [2] Send new message
        [3] Remove existing message\n''')
    
    
    def get_user_choice(self):
        '''
        Gets user's input for the expected operation and returns the choice number 
        if it is valid; -1 otherwise.
        '''    
        illegal_choice_msg = 'Choice is illegal. Please pick a number between 0 and 3'
        user_input = input('Please type your choice and press ENTER\n')
        try:
            choice = int(user_input)
            if (0 <= choice <= 3):
                return choice
        except ValueError:
            print (illegal_choice_msg)
        return -1
            
    def run(self):
        '''
        Runs an "infinite" dialog loop and executes users requests. Nothing is 
        returned.
        '''
        global no_permissions_msg, no_such_msg, thanks_msg
        while True:
            time.sleep(1.5)
            self.show_options()
            choice = self.get_user_choice()
            if choice == -1:
                continue
            elif choice == 0:
                print (thanks_msg)
                break
            else:
                username = input('Please enter username (only conversation\'s members are allowed to send/read messages).\n')
                if not self.coversation.is_member(username):
                    print (no_permissions_msg)
                    continue
                if choice == 1:
                    response = self.coversation.get_conversation()
                    print (response)
                elif choice == 2:
                    msg_content = input('Please type your message.\n')
                    msg_time = Date(time.strftime('%H,%M,%S'))
                    response = self.coversation.send_msg(username, msg_content, msg_time)
                    print (response)
                elif choice == 3:
                    msg_id_str = input('Please enter message id.\n')
                    try:
                        response = self.coversation.delete_msg(msg_id_str)
                    except ValueError:
                        response = no_such_msg
                    print (response)


########################################################
#     Optional: Paste the content of Tests.py below    #

########################################################
d = Date('hh,mm,ss')
assert d.hour=='hh'
assert d.minute=='mm'
assert d.second=='ss'
assert str(d)=='hh:mm:ss'
members = ('a', 'b', 'c')
m=Message(members[0], 'bla', d, 17)
assert len(m)==3
assert str(m)=='(17) ' + str(d) + ' a: bla' 
c=Conversation(members, 20, 3)
assert c.enough_space('$'*c.size_limit)    
assert not c.enough_space('$'*(c.size_limit+1))    
assert not c.is_member('non-existing member')
assert c.is_member('a')
assert c.is_member('c')
assert c.is_empty()
try:
    c.delete_msg(170)
    assert False
except ValueError:
    pass
assert c.get_conversation() == empty_conversation
try:
    c.send_msg(members[0], '$'*(c.size_limit+1), d)
    assert False
except MemoryError:
    pass
assert c.send_msg(members[0], '$'*(c.size_limit-1), d) == sending_succeeded_msg
assert c.find_msg_index(1) == 0
assert not c.is_empty()

assert sum([len(x) for x in c.content]) == c.size_limit-1
try:
    c.send_msg(members[0], '$$', d)
    assert False
except MemoryError:
    pass
assert sum([len(x) for x in c.content]) == c.size_limit-1

try:
    c.delete_msg(0)
    assert False
except ValueError:
    pass

tmp = c.total_messages_sent
assert c.delete_msg(tmp) == removing_succeeded_msg
try:
    c.delete_msg(1)
    assert False
except ValueError:
    pass

assert c.total_messages_sent == tmp
assert c.find_msg_index(0) == -1

assert c.is_empty()
assert sum([len(x) for x in c.content]) == 0
assert c.send_msg(members[0], 'Hi', d) == sending_succeeded_msg
assert c.send_msg(members[1], 'Bye', d) == sending_succeeded_msg
assert c.get_conversation() == '(2) hh:mm:ss a: Hi\n(3) hh:mm:ss b: Bye'
f = open('./'+members[0]+'.txt')
assert f.read() == '(2) hh:mm:ss a: Hi\n(3) hh:mm:ss b: Bye'
f.close()
assert c.size == 5
print ('\nCongrats!!! All preliminary tests passed!\n')
    
   
        

''' Main code. Do not change!'''
try:
    app = Application()
    app.run()
except ValueError:
    print ('\nOne (or more) of the parameter values is illegal.')
    time.sleep(1)
    print ('\nFailed to initialize the app.')
    time.sleep(1)
    print ('\nExiting'),
    for i in range(3):
        time.sleep(0.5)
        print ('.'),
    time.sleep(0.5)
    print ('\n')

    

#Assert statement throws an error if the expression after it evaluates to False

        
    
    