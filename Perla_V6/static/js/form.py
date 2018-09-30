from browser import document, window

document.getElementById('valide').disabled = True


def copier(ev):
    premier = document.getElementById('auth_user_password')
    valeur = premier.value
    double = document.getElementById('auth_user_password_two')
    double.value = valeur


document.getElementById('auth_user_password').addEventListener('keypress', copier)
document.getElementById('auth_user_password').addEventListener('keyup', copier)
document.getElementById('auth_user_password').addEventListener('blur', copier)
document.getElementById('auth_user_password').addEventListener('focus', copier)
document.getElementById('auth_user_email').addEventListener('keypress', copier)



def verification(ev):
    nome = document.getElementById('auth_user_first_name')
    nom =  window.RegExp('^([a-zA-Z0-9_-]){4,20}$').test(nome.value)
    print(nom, 'nom')
    password = document.getElementById('auth_user_password')
    patt = window.RegExp("^([a-zA-Z0-9_-]){4,20}$")
    res = patt.test(password.value)
    print(res, 'res')
    validmobile = document.getElementById('valid-msg')
    email = document.getElementById('auth_user_email')
    emailtest =  window.RegExp('^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$').test(email.value)
    ler = validmobile.classList.contains("hide")
    print(ler, 'ler')
    print(emailtest)
    print(res)
    print(nom)
    if nom == True and res == True and ler == False and emailtest == True:
         document.getElementById('valide').disabled = False
    else:
        document.getElementById('valide').disabled = True
        print('ok')



document.getElementById('auth_user_email').addEventListener('keypress', verification)
document.getElementById('auth_user_email').addEventListener('keyup', verification)
document.getElementById('auth_user_email').addEventListener('blur', verification)
document.getElementById('auth_user_email').addEventListener('focus', verification)
document.getElementById('auth_user_email').addEventListener('keypress', verification)

document.getElementById('auth_user_first_name').addEventListener('keypress', verification)
document.getElementById('auth_user_first_name').addEventListener('keyup', verification)
document.getElementById('auth_user_first_name').addEventListener('blur', verification)
document.getElementById('auth_user_first_name').addEventListener('focus', verification)
document.getElementById('auth_user_first_name').addEventListener('keypress', verification)

document.getElementById('auth_user_password').addEventListener('keypress', verification)
document.getElementById('auth_user_password').addEventListener('keyup', verification)
document.getElementById('auth_user_password').addEventListener('blur', verification)
document.getElementById('auth_user_password').addEventListener('focus', verification)
document.getElementById('auth_user_password').addEventListener('keypress', verification)


document.getElementById('mobile-number').addEventListener('keypress', verification)
document.getElementById('mobile-number').addEventListener('keyup', verification)
document.getElementById('mobile-number').addEventListener('blur', verification)
document.getElementById('mobile-number').addEventListener('focus', verification)
document.getElementById('mobile-number').addEventListener('keypress', verification)


def mobileblur(ev):
    validmobile = document.getElementById('valid-msg')
    ler = validmobile.classList.contains("hide")
    if ler == True:
        document.getElementById('mobile-number').focus()




document.getElementById('auth_user_first_name').addEventListener('keypress', mobileblur)

document.getElementById('auth_user_first_name').addEventListener('keyup', mobileblur)
document.getElementById('auth_user_first_name').addEventListener('blur', mobileblur)
document.getElementById('auth_user_first_name').addEventListener('focus', mobileblur)
document.getElementById('auth_user_first_name').addEventListener('keypress', mobileblur)


document.getElementById('auth_user_password').addEventListener('keypress', mobileblur)

document.getElementById('auth_user_password').addEventListener('keyup', mobileblur)
document.getElementById('auth_user_password').addEventListener('blur', mobileblur)
document.getElementById('auth_user_password').addEventListener('focus', mobileblur)
document.getElementById('auth_user_password').addEventListener('keypress', mobileblur)


document.getElementById('auth_user_email').addEventListener('keypress', mobileblur)

document.getElementById('auth_user_email').addEventListener('keyup', mobileblur)
document.getElementById('auth_user_email').addEventListener('blur', mobileblur)
document.getElementById('auth_user_email').addEventListener('focus', mobileblur)
document.getElementById('auth_user_email').addEventListener('keypress', mobileblur)
