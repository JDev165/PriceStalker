var data = {};

async function postData(requestUrl, elementIds){
	const idsArray = elementIds.split(',');
	data = createDataFromElements(idsArray);
	const response = await fetch(requestUrl, {
	    method: 'POST', // *GET, POST, PUT, DELETE, etc.
	    mode: 'cors', // no-cors, *cors, same-origin
	    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
	    credentials: 'same-origin', // include, *same-origin, omit
	    headers: { 'X-CSRFToken': getCookie('csrftoken'), 'Accept': 'application/json','Content-Type': 'application/json' },
	    referrerPolicy: 'no-referrer', // no-referrer, *client
	    body: JSON.stringify(data) // body data type must match "Content-Type" header
	});
	const jsonResponse = await response.json();

	
}

function generateProduct(){
	const recentlyStalkedSection = document.getElementById('recently_stalked');
	const cardParentDiv = document.createElement('div');
	cardParentDiv.className = 'card';
	cardParentDiv.setAttribute('style', 'width: 18rem');
	const cardBodyDiv = document.createElement('div');
	cardBodyDiv.className = 'card-body';
	const cardTitle = document.createElement("h5");
	cardTitle.className = 'card-title';
	cardTitle.appendChild(document.createTextNode(data.name));
	const cardText = document.createElement('p');
	cardText.className = 'card-text';
	cardText.appendChild(document.createTextNode('coming soon...'));
	const cardButton = document.createElement('a');
	cardButton.className = 'btn btn-primary';
	cardButton.setAttribute('href', data.url);
	cardButton.setAttribute('target', '_blank');
	cardButton.appendChild(document.createTextNode('View Product'));
	cardBodyDiv.append(cardTitle);
	cardBodyDiv.append(cardText);
	cardBodyDiv.append(cardButton);
	cardParentDiv.append(cardBodyDiv);
	recentlyStalkedSection.prepend(cardParentDiv);
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


function swapImages(imgElement){
	const imgSrc = imgElement.getAttribute('src');
	if(imgSrc == '/static/icons/bookmark.svg'){
		imgElement.setAttribute('src', '/static/icons/bookmarked.svg');
	}
	else{
	 	imgElement.setAttribute('src', '/static/icons/bookmark.svg');
	}
}

