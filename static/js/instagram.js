window.addEventListener('DOMContentLoaded', function() {

    const user_id = '220991691';
    const access_token = '13794908.5b9e1e6.4dcb21a1681a46cfb918650b3593b456';
    const url = 'https://api.instagram.com/v1/users/' + user_id + '/media/recent/?access_token=' + access_token;

    request(url, 'json').get(function(data, status) {

        // var data = JSON.parse(data);
        console.info( data );
        // console.info(this);
        // console.info( status );

    });

});
