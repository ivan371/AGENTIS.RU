//setInterval(animation('mymess', 'shake'), 1500);
//while(1)
setInterval(function(){
	id = 'mymess';
	effect = 'shake';
	 document.getElementById(id).classList.add(effect);
    setTimeout( function(){
        document.getElementById(id).classList.remove(effect);
    }, 1000);
}, 2000);
