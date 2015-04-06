;(function( global, undefined ) {
    'use strict';

var
    kettu = function( selector ) {
        return new kettu.fn.init( selector );
    },

    breakpoints = {
        'mobile': 320,
        'mobile-md': 480,
        'desktop-sm': 767,
        'desktop-md': 979,
        'desktop': 1200
    },

    document = window.document;

    kettu.fn = kettu.prototype = {};

    var init = kettu.fn.init = function( selector ) {
        return window.kettu = window.$ = kettu;
    }

    init.prototype = kettu.fn;

})(typeof window !== 'undefined' ? window : this);
