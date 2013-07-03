import webapp2

class Main(webapp2.RequestHandler):
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('this is say')
        
    def post(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('this is say')


app = webapp2.WSGIApplication([('/', Main)])