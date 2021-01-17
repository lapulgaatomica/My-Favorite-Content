dark = document.getElementById('dark');

document.body.onload = function () {
	if(localStorage.getItem('backgroundColor') === 'black'){
		dark.checked = true;
		document.body.style.background = 'black';
	}else{
		dark.checked = false;
		document.body.style.background = 'white';
	}
}

dark.addEventListener('change', function(){
	if (dark.checked){
		localStorage.setItem('backgroundColor', 'black')
		document.body.style.background = 'black';
	}else{
		localStorage.removeItem('backgroundColor')
		document.body.style.background = 'white';
	}
});
