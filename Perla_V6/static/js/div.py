from browser import document, window




def copier(ev):
    premier = document.getElementById('caftansnoms')
    deuxieme = document.getElementById('caftansdates')
    troisieme = document.getElementById('caftansprixs')
    selection = document.getElementById('selection').value
    if selection == "Position":
        print("lalla")
        premier.style.display  = "none"
        deuxieme.style.display  = "block"
        troisieme.style.display  = "none"
    elif selection == "Nom":
        print("yayayay")
        premier.style.display  = "block"
        deuxieme.style.display  = "none"
        troisieme.style.display  = "none"
    elif selection == "Prix":
        print("wwwwww")
        premier.style.display  = "none"
        deuxieme.style.display  = "none"
        troisieme.style.display  = "block"


document.getElementById('selection').addEventListener('change', copier)
