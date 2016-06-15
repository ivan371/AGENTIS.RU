function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
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
function deploy_message()
{
	document.getElementById("mess_off").style.display="none";
}
function appear_message()
{
	document.getElementById("mess_off").style.display="block";
}
function more(user)
{
	$.ajax({
	  	type: 'POST',
	  	url: "/more/",
		data: {'user': user,},
		dataType: 'json',
  		error: function(xhr, errmsg, err){
			alert(xhr.status + ": " + xhr.responseText);
			//window.addEventListener('keydown', whatKey, true);
			}	
	 });
}

deploy_mess(0, 0, 0, 0);
var block = 0;
var old_name;
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
			this.arr[res] = 1;
			document.getElementById("sleep_name" + name).style.backgroundColor = "#fbceb1";
			block = 0;}, 1000)
		}
		else
		{
			if(block == 0)
			{
				document.getElementById("sleep" +res).style.display = "block"
				this.arr[res] = 0;
				animation("sleep" +res, "fadeInDown");
				document.getElementById("sleep_name" + name).style.backgroundColor = "orange";
				block = res + 1;
				old_name = name;
			}
			else
			{
				block = block - 1;
				animation("sleep" + block, "bounceOut");
				document.getElementById("sleep" + block).style.display = "none";
				this.arr[block] = 1;
				document.getElementById("sleep_name" + old_name).style.backgroundColor = "#fbceb1";
				document.getElementById("sleep" +res).style.display = "block"
				this.arr[res] = 0;
				animation("sleep" +res, "fadeInDown");
				document.getElementById("sleep_name" + name).style.backgroundColor = "orange";
				block = res + 1;
				old_name = name;
			}
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



