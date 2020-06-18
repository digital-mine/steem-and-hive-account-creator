#!/usr/bin/python
from beem import Steem
from beem.account import Account
from beem.rc import RC
from beem.vote import Vote
from beem.instance import set_shared_steem_instance
from beem.exceptions import ContentDoesNotExistsException
from beem.comment import Comment
import time


def name():
    new_account=input('Enter the new account name:')
    try:
        acc=Account(str.lower(new_account),steem_instance=stm)
        print  (acc.name+' is UNAVAILABLE!')
        name()
    except Exception as e:
        print (new_account+' is AVAILABLE!')
        return new_account

def password_():  
    password = input('Enter the new password for the new account:')
    password2= input('Re-Enter the new password for the new account:')
    if password==password2:
        print(stm.create_claimed_account(new_account_name, creator='digital.mine', password=password))
        time.sleep(4)
        new_account = Account(new_account_name)
        new_account.print_info()
        print('CREATED')
    else:
        print ('Passwords are different please re-try')
        password_()

stm = Steem("https://anyx.io",keys='')#insert hive private active key
set_shared_steem_instance(stm)
account=Account("[YOUR ACCOUNT NAME]",steem_instance=stm)
new_account_name=name()
password_()
stm=0
stm = Steem("https://api.steemit.com",keys='')#insert steem private active key
set_shared_steem_instance(stm)
account=Account("[YOUR ACCOUNT NAME]",steem_instance=stm)
new_account_name=name()
password_()
