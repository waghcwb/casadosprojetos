window.addEventListener('DOMContentLoaded', function() {

    const url = 'https://api.instagram.com/v1/users/search?q=waghcwb&access_token=13794908.5b9e1e6.4dcb21a1681a46cfb918650b3593b456';

    request('http://ip.jsontest.com/').get(function(data, status) {

        // var data = JSON.parse(data);
        console.info( data );
        console.info(this);
        // console.info( status );

    });

    console.info(request.teste);
});
