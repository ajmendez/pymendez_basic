import os, ConfigParser, sys
AUTHFILE = '~/.limited/auth'


def auth(service=None, items=None, authfile=AUTHFILE):
    '''Returns the username/password for a basic serivce. while bad, this is 
    kept here so that I can github things.  
    can pass in items -- a list of items to grab from the the config'''
    config = ConfigParser.ConfigParser()
    config.read(os.path.expanduser(authfile))
    if items is None:
        items = ['username', 'password']
    
    if isinstance(items,str):
      return config.get(service,items)
    else:
      return [config.get(service,item) for item in items]

