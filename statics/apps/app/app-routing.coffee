((window, jQuery, angular) ->
    module = angular.module 'baseApp'

    module.config [
        '$stateProvider'
        '$urlRouterProvider'
        '$locationProvider'
        ($stateProvider, $urlRouterProvider, $locationProvider) ->
            $stateProvider.state 'article', {
                url: '/article',
                abstract: true,
                template: '<article></article>'
            }
            .state 'mypage', {
                url: '/mypage',
                template: '<mypage></mypage>'
            }
            .state 'account', {
                url: '/account',
                abstract: true,
                template: '<account></account>'
            }
            .state 'intro', {
                url: '/',
                template: '<intro></intro>'
            }
            $urlRouterProvider.otherwise 'intro'
            $locationProvider.html5Mode true
            return
    ]


) window, jQuery, angular
