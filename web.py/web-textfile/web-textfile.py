import web
urls = ('/','index')

class index:
  def GET(self):
    my_file = open('file.txt')
    read_file = my_file.read()
    return read_file
    my_file.close()


if __name__ == "__main__":
  app = web.application(urls, globals())
  app.run()
