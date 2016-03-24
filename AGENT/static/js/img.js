function animation(id, effect){
    document.getElementById(id).classList.add(effect);
    setTimeout( function(){
        document.getElementById(id).classList.remove(effect);
    }, 1000);
}
function animationz(id, effect){
    document.getElementById(id).classList.remove('pulseout');
    document.getElementById(id).classList.add(effect);
}
function animationzr(id, effect, neweffect){
    document.getElementById(id).classList.remove('pulseto');
    document.getElementById(id).classList.add(effect);
}

