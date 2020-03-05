//Bookmark functions
function toggleBookmark(requestUrl, data, imgElement){
	const bookmarkState = setBookmarkState(data, imgElement);
	data['bookmark'] = bookmarkState;
	// const response = postData(requestUrl, data);
	//if (response != -1){
	//	swapImages(bookmarkState);
	//}
}

function setBookmarkState(data, imgElement){
	let state = 0;
	if(imgElement.getAttribute('src') == '/static/icons/bookmark.svg'){
		state = 1;
	}
	else{
		state = 0;
	}

	return state;
}

// Request functions
function postData(requestUrl, data){
	const response = makeRequest(requestUrl, data);

	return response;
}

function swapImages(state){
	if(state){
		imgElement.setAttribute('src', '/static/icons/bookmark.svg');
	}
	else{
	 	imgElement.setAttribute('src', '/static/icons/bookmarked.svg');
	}
}

function postFieldsData(requestUrl, elementIds){
	const idsArray = elementIds.split(',');
	data = createDataFromElements(idsArray);
	const response = makeRequest(requestUrl, data);

	return response
}

function createDataFromElements(keysArray){
	let	data = {};
	for(let index = 0; index < keysArray.length; index++){
		let id 		= keysArray[index].trim();
		let element = document.getElementById(id);
		let key 	= id.split('_')[1];
		let value	= element.value;
		data[key] 	= value;
	}

	return data;
}

async function makeRequest(requestUrl, data){
	try{
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
	catch(error){
		const jsonResponse = -1; 
		console.error(error);
	}

	return jsonResponse
}

function getCookie(name){
	const cookieValue = document.cookie.match(name + '=[^;]*')[0].split('=')[1];
	return cookieValue;
}

//Generic functions

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


