function Change_email()
{
	document.getElementById("email").style.display="None";
	document.getElementById("new_email").style.display="block";
}
function Change_number()
{
	document.getElementById("phone").style.display="None";
	document.getElementById("new_phone").style.display="block";
}
function Change_prof()
{
	document.getElementById("prof").style.display="None";
	document.getElementById("new_prof").style.display="block";
}
function Change_initial()
{
	document.getElementById("initials").style.display="None";
	document.getElementById("new_initials").style.display="block";
}
function Add_offer()
{
	document.getElementById("new_offerz").style.display="None";
	document.getElementById("offer").style.display="None";
	document.getElementById("new_offer").style.display="block";
}
function deploy_offer(a, b)
{
	document.getElementById(a).style.display="None";
	document.getElementById(b).style.display="block";
}
function collapce_offer(a, b)
{
	document.getElementById(a).style.display="block";
	document.getElementById(b).style.display="none";
}
deploy_mess(0, 0, 0, 0);
function deploy_mess(res, what, num, name)
{
	if(num != 0)
	{
	$.ajax({
	  		type: 'POST',
	  		url: "/change_status/",
			data: {'name': name,},
			dataType: 'json',
  			error: function(xhr, errmsg, err){
						alert(xhr.status + ": " + xhr.responseText);
						//window.addEventListener('keydown', whatKey, true);
					}	
	  	});
	 }
	if(what == 0)
	{
		this.arr = new Array();
	}
	else
	{
		if(this.arr[res] == 0)
		{
			animation("sleep" +res, "bounceOut");
			setTimeout(function(){document.getElementById("sleep" + res).style.display = "none"
			this.arr[res] = 1;}, 1000)
		}
		else
		{
			document.getElementById("sleep" +res).style.display = "block"
			this.arr[res] = 0;
			animation("sleep" +res, "fadeInDown");
		}
	}
}

function animation_delay(id, effect, href)
{
	animation(id, effect);
	document.getElementById(id).classList.add(effect);
    setTimeout( function(){
        document.getElementById(id).classList.remove(effect);
        location.href = href;
    }, 1000);
}

