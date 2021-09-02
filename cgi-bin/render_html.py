html = """
<html>

<head>
    <title>CGI Form</title>
    <style>
        * {
            margin: 10px;
        }
        body {
            background-color: red;
        }
        .green_back {
            background-color: greenyellow;
        }
        .blue_back {
            background-color: blue
        }
        td {
            padding: 10px;
        }
        #btn {
            background-color: orange;
            border: 4px solid orange;
            border-radius: 20px;
        }
        #btn:hover {
            cursor: pointer;
        }
    </style>
</head>

<body>
    <form name='f1' method='post' action='form_submit.py'>
        <table>
            <tr class='blue_back'>
                <td>First Name </td>
                <td><input type='text' name='f_name'>
                <td>
            </tr>
            <tr class='green_back'>
                <td>Last Name</td>
                <td> <input type='text' name='s_name'></td>
            </tr>
            <tr class='blue_back'>
                <td>Gender</td>
                <td> <input type='radio' name='r1' value='male'> Male
                    <input type='radio' name='r1' value='female'> Female
                </td>
            </tr>
            <tr class='green_back'>
                <td>Programming Languages you know</td>
                <td> 
                    <input type='checkbox' name='js' value='JavaScript'>
                    <label>JavaScript</label><br>
                    <input type='checkbox' name='html' value='HTML'>
                    <label>HTML</label><br>
                    <input type='checkbox' name='css' value='CSS'>
                    <label>CSS</label><br>
                    <input type='checkbox' name='sql' value='SQL'>
                    <label>SQL</label><br>
                    <input type='checkbox' name='php' value='PHP'>
                    <label>PHP</label><br>
                    <input type='checkbox' name='python' value='Python'>
                    <label>Python</label><br>
                    <input type='checkbox' name='java' value='Java'>
                    <label>Java</label><br>
                    <input type='checkbox' name='c' value='C'>
                    <label>C</label><br>
                    <input type='checkbox' name='c++' value='C++'>
                    <label>C++</label><br>
                    <input type='checkbox' name='c#' value='C#'>
                    <label>C#</label><br>
                    <input type='checkbox' name='oc' value='Objective-C'>
                    <label>Objective-C</label><br>
                    <input type='checkbox' name='swift' value='Swift'>
                    <label>Swift</label><br>
                    <input type='checkbox' name='ruby' value='Ruby'>
                    <label>Ruby</label><br>
                    <input type='checkbox' name='rails' value='Rails'>
                    <label>Rails</label><br>
                    <input type='checkbox' name='perl' value='Perl'>
                    <label>Perl</label><br>
                    <input type='checkbox' name='go' value='Go'>
                    <label>Go</label><br>
                </td>
            </tr>
            <tr>
                <td><input type='submit' value='Submit' id='btn'></td>
                <td> </td>
            </tr>
        </table>
    </form>
</body>

</html>
"""

print(html)
