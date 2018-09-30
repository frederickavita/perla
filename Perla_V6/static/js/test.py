from browser import document, window

def annulle(ev):
	parsed = json.loads(window.localStorage.cart)
	print(parsed)
	id = ev.target.id
	print(type(id))
	rt = id.find('ber')
	if rt == 0:
		id = str(id[3:])
		#del parsed[id]
		#window.localStorage.setItem("cart", window.JSON.stringify(parsed)) 
		print('ok')
		#window.localStorage.setItem("cart", window.JSON.stringify(parsed))  
		#window.jQuery.ajax({'url':"{{=URL('echo')}}", 'type': 'POST', 'context': 'document.body', 'data': {"cart": #window.JSON.stringify(cart)},"dataType": "json",'success': print('ok')})
		#window.location.reload()
    
	



bns = window.jQuery("div")
bns.on("click", annulle )    
