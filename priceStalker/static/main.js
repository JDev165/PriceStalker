async function postData(requestUrl, elementIds){
	const idsArray 				= elementIds.split(',');
	const data 					= createDataFromElements(idsArray);
	const response 		= await fetch(requestUrl, {
	    method: 'POST', // *GET, POST, PUT, DELETE, etc.
	    mode: 'cors', // no-cors, *cors, same-origin
	    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
	    credentials: 'same-origin', // include, *same-origin, omit
	    headers: { 'X-CSRFToken': getCookie('csrftoken'), 'Accept': 'application/json','Content-Type': 'application/json' },
	    referrerPolicy: 'no-referrer', // no-referrer, *client
	    body: JSON.stringify(data) // body data type must match "Content-Type" header
	});
	const jsonResponse	= await response.json();

	
}

function createDataFromElements(keysArray){
	var	data = {};
	for(var index = 0; index < keysArray.length; index++){
		var id 		= keysArray[index].trim();
		var element = document.getElementById(id);
		var key 	= id.split('_')[1];
		var value	= element.value;
		data[key] 	= value;
	}

	return data;
}

function getCookie(name){
	const cookieValue = document.cookie.match(name + '=[^;]*')[0].split('=')[1];
	return cookieValue;
}