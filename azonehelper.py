import urllib, urllib2, cookielib, random, json
from pprint import pprint



class AzoneHelper:

    def __init__(self, username="", password=""):

        if(username is not ""):
            self.log_in(username, password)


    def log_in(self, username, password):

        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        self.username = username

        login_data = urllib.urlencode({'username' : username, 'password' : password})
        
        print "AZONE_MODULE :: logging into Azone as: <" + username + ">..."

        try:

            self.opener.open('http://azone.guggenheim.org/login', login_data)

            resp = self.opener.open('http://azone.guggenheim.org/portfolio/' + username)
            #print resp.read()

            print "AZONE_MODULE :: logged in! "
        except:

            print "LOGIN FAILED: ", self.username


    def create_account(self, username, email, password):

        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        self.username = username

        login_data = urllib.urlencode({'username' : username, 'email' : email, 'password' : password})
        
        print "AZONE_MODULE :: creating Azone account as: <" + username + ">..."

        try:

            self.opener.open('http://azone.guggenheim.org/signup', login_data)

            resp = self.opener.open('http://azone.guggenheim.org/portfolio/' + username)
            #print resp.read()

            print "AZONE_MODULE :: signed up! "
        except:

            print "SIGNUP FAILED: ", self.username


    def load_json_file(self, filename):

        with open(filename) as data_file:    
            data = json.load(data_file)

        return data
        



    def perform_transaction(self, verb, symbol, quantity, tipIDs):

        if(verb is not "buy" and verb is not "sell"):
            return -1

        print "AZONE_MODULE :: performing transaction as ", self.username, ": " + verb + "ing " + str(quantity) + " shares of " + symbol + "..."

        for i in xrange(quantity):
            purchase_data = urllib.urlencode({'comment' : "", 'block_id': random.choice(tipIDs[symbol])})   
            try:
                resp = self.opener.open('http://azone.guggenheim.org/investing/futures/' + symbol + '/' + verb + '/confirm', purchase_data)
            except:
                print "PURCHASE FAILED: ", self.username

        print "AZONE_MODULE :: performed transaction as ", self.username, "!"
        #print resp.read()

    if __name__ == "__main__":
        main()

