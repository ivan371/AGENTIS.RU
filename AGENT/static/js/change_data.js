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
deploy_mess(0, 0);
function deploy_mess(res, what)
{
	if(what == 0)
	{
		this.arr = new Array();
	}
	else
	{
		if(this.arr[res] == 0)
		{
			document.getElementById("sleep" + res).style.display = "none"
			this.arr[res] = 1;
		}
		else
		{
			document.getElementById("sleep" +res).style.display = "block"
			this.arr[res] = 0;
		}
	}
}
