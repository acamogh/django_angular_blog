var sampleApp = angular.module('myApp', ['ngCookies','ui.bootstrap']);

sampleApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/', {
                templateUrl: '/static/views/home.html',
                controller: 'index_ctrl'
            })
            .when('/:id', {
                templateUrl: '/static/views/detail.html',
                controller: 'detail_ctrl'
            })
    }
])

sampleApp.config(['$httpProvider', function($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    }])

sampleApp.run( function run( $http, $cookies ){
        $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
    })

sampleApp.filter('cut', function () {
        return function (value, wordwise, max, tail) {
            if (!value) return '';

            max = parseInt(max, 10);
            if (!max) return value;
            if (value.length <= max) return value;

            value = value.substr(0, max);
            if (wordwise) {
                var lastspace = value.lastIndexOf(' ');
                if (lastspace != -1) {
                    value = value.substr(0, lastspace);
                }
            }

            return value + (tail || ' …');
        };
    });
sampleApp.filter('startFrom',function(){
    return function (data,start){
        return data.slice(start);
    }
})