from pyscript import display, document

def add_member(event):

    members = {
    "krishna kiyomi pascua",
    "adriana averilla",
    "anthony cases",
    "ayrton co",
    "ciara r de guzman",
    "cloud toribio",
    "corral lara georgina",
    "curbi charlene faith",
    "duchess baetiong",
    "dustin cunanan",
    "enrique gerard jocson",
    "ethan feudo",
    "ethan james de leon",
    "gianna entrada",
    "hannah galapon",
    "ian salangsang",
    "jaeden elequin",
    "juan carlos paguio espiritu",
    "lacaya frances venice",
    "liam lopez",
    "nicole repolona",
    "noelle acuna",
    "rafael iñigo roncal",
    "reese ancheta",
    "riso salapunen",
    "sean obcemea",
    "sofia guevarra",
    "sophia georgina celi",
    "zoe zabala",
    "zyrene nieto",
}

first_name = document.getElementById("first_name").value.strip().lower()
last_name = document.getElementById("last_name").value.strip().lower()
full_name = f"{first_name} {last_name}"
    
if full_name in members:
     display("Member already exists.")
else:
    members.add(full_name)
    display(f"Member '{full_name}' added successfully.")