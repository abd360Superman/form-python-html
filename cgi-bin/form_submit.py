print("HTTP/1.0 200 OK\n")
import cgi, sqlite3, html
form = cgi.FieldStorage()

conn = sqlite3.connect('data.sqlite3')
cur = conn.cursor()

languages = []

try:
    first_name=form["f_name"].value
except :
    first_name=' First name is blank ' 
	
try:
    second_name=form["s_name"].value
except :
    second_name=' Second name is blank ' 
	
try:
    gender=form["r1"].value
except :
    gender=' No selection of  Gender'

if form.getvalue('js'):
    languages.append('JavaScript')
if form.getvalue('html'):
    languages.append('HTML')
if form.getvalue('css'):
    languages.append('CSS')
if form.getvalue('sql'):
    languages.append('SQL')
if form.getvalue('php'):
    languages.append('PHP')
if form.getvalue('python'):
    languages.append('Python')
if form.getvalue('java'):
    languages.append('Java')
if form.getvalue('c'):
    languages.append('C')
if form.getvalue('c++'):
    languages.append('C++')
if form.getvalue('c#'):
    languages.append('C#')
if form.getvalue('oc'):
    languages.append('Objective-C')
if form.getvalue('swift'):
    languages.append('Swift')
if form.getvalue('ruby'):
    languages.append('Ruby')
if form.getvalue('rails'):
    languages.append('Rails')
if form.getvalue('perl'):
    languages.append('Perl')
if form.getvalue('go'):
    languages.append('Go')

if len(languages) == 0:
    lang_str = 'No Programming Languages'
else:
    lang_str = ', '.join(languages)

cur.execute('INSERT INTO Data (fname, lname, gender, languages) VALUES (?, ?, ?, ?)', (first_name, second_name, gender, lang_str))

conn.commit()
cur.close()

htm = '''<html>

<head>
    <title>CGI Form</title>
</head>

<body>
    <div class='blue_back'>
        <br><b>First Name</b> {0}
        <br><b>Last Name</b> {1}
        <br><b>Gender</b> {2}
        <br><b>Programming Languages Known</b> {3}
    </div>
</body>

</html>
'''.format(html.escape(first_name), html.escape(second_name), html.escape(gender), html.escape(lang_str))

print(htm)

