;(function(global, undefined) {

    'use strict';

    function kettu(params) {

        if( !(this instanceof kettu) ) {
            return new kettu(params);
        }

        this.params = params;
    }

    kettu.fn = kettu.prototype = {
        method: function() {
            console.info('Wow!!');
        }
    };

    window.kettu = kettu;

})(typeof window !== 'undefined' ? window : this);
