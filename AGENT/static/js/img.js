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
function animationz(id, effect){
    		//var effect = elem.data("effect");
    		//alert(effect);
    		//if(!effect || elem.hasClass(effect)) return false;
    //elem.addClass(effect);
    document.getElementById(id).classList.remove('pulseout');
    document.getElementById(id).classList.add(effect);
    //alert(0);
}
function animationzr(id, effect, neweffect){
    		//var effect = elem.data("effect");
    		//alert(effect);
    		//if(!effect || elem.hasClass(effect)) return false;
    //elem.addClass(effect);   
    document.getElementById(id).classList.remove('pulseto');
    document.getElementById(id).classList.add(effect);
}
