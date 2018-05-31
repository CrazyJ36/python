#!/usr/bin/env python3

import web

urls = ('/','index')
renderPointer = web.template.render('templates/')

class index:
  def GET(self):
    return renderPointer.index()

if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()
