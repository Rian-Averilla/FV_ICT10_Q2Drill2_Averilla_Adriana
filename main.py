from pyscript import display, document

grade_8 = {"ayrton co", "duchess baetiong", "jaeden elequin", "zoe zabala", "sophia georgina celi", "reese ancheta"}
grade_9 = {"krishna kiyomi pascua", "anthony cases", "cloud toribio", "corral lara georgina", "curbi charlene faith", "ethan feudo", "ethan james de leon", "hannah galapon", "juan carlos paguio espiritu", "lacaya frances venice", "nicole repolona", "noelle acuna", "sean obcemea"}
grade_10 = {"adriana averilla", "ciara r de guzman", "dustin cunanan", "ian salangsang", "rafael iñigo roncal", "zyrene nieto"}
grade_11 = {"gianna entrada", "liam lopez", "riso salapunen", "sofia guevarra"}
grade_12 = {"enrique gerard jocson"}

members = grade_8 | grade_9 | grade_10 | grade_11 | grade_12
display(str(members), target="result")

def add_member():
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()
    full_name = f"{first_name} {last_name}"
    allmembers = grade_8 | grade_9 | grade_10 | grade_11 | grade_12 | full_name
    totalmembers = len(allmembers)

    if not first_name or not last_name:
        display("Please enter both names.")
        return

    if full_name in members:
        display("Member already exists.")
    else:
        members.add(full_name)
        display(allmembers, target="result")

  
  

