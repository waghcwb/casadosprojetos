var instagram = instagram() || function() {
	
	var user = {
		id: '560879016',
		token: '3794908.5b9e1e6.4dcb21a1681a46cfb918650b3593b456'
	};

	ajax.request('https://api.instagram.com/v1/users/' + user.id + '/media/recent?access_token=' + user.token);
};