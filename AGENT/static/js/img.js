function animation(id, effect){
    		//var effect = elem.data("effect");
    		//alert(effect);
    		//if(!effect || elem.hasClass(effect)) return false;
    //elem.addClass(effect);
    document.getElementById(id).classList.add(effect);
    setTimeout( function(){
        document.getElementById(id).classList.remove(effect);
    }, 1000);
    //alert(0);
}
