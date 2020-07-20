var updateBtn =document.getElementsByClassName('update-cart')

for(var i =0; i< updateBtn.length; i++){

    updateBtn[i].addEventListener('click',function(){
        var itemid = this.dataset.item
        var action =this.dataset.action
        console.log('itemid:',itemid,'action:',action)
        updateOrder(itemid, action)

    
       
    })
}

function updateOrder(itemid,action){

    console.log('User is authenticated, sending data...')

		var url = '/update/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'itemid':itemid, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
    
    
}