import cgi

def process_form(self):
  form = cgi.FieldStorage()

  name = form.getvalue('submit-link')

  print(name)

if __name__ == '__main__':
  process_form()