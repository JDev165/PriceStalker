async function postData(requestUrl, elementIds){
	const idsArray 				= elementIds.split(',');
	const data 					= createDataFromElements(idsArray);
	// add Django CSRFToken or else request won't go through
	const headersData			= { 'X-CSRFToken': getCookie('csrftoken'), 'Content-Type': 'application/json' };
	const initData 				= { method: 'POST', credentials: 'same-origin', headers: headersData, body: JSON.stringify(data) }
	const request 				= new Request(requestUrl, initData);
	const response 				= await fetch(request);
	
	const reponseData 			= await response.json();
	console.log(reponseData);
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