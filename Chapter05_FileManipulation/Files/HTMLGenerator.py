with open("page.html", "w") as page:
    page.write("<body> <h1> This is a TEST </h1> </body>")
    page.write("<br> <h2> You can see some important programming languages below: </h2> </br>")
    page.write("<h3>")
    name = ""
    while name != "Q":
        name = input("Enter a name or type 'Q' to quit").upper()
        if name!= "Q":
            page.write("<br>" + name)
            page.write("</h3></body>")