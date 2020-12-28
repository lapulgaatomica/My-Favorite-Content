dark = document.getElementById('dark')
dark.addEventListener('change', function(){
	if (dark.checked){
		document.body.style.background = 'black'
	}else{
		document.body.style.background = 'white'
	}
});