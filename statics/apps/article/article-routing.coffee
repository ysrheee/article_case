((window, jQuery, angular) ->
    module = angular.module 'baseApp'

    module.config [
        '$stateProvider'
        '$urlRouterProvider'
        '$locationProvider'
        ($stateProvider, $urlRouterProvider, $locationProvider) ->
            $stateProvider.state 'article.list', {
                url: ''
                template: '<article-list></article-list>'
            }
            .state 'article.write', {
                url: '/write'
                template: '<article-write></article-write>'
            }
            $locationProvider.html5Mode true
            return
    ]
    

    module.run ($rootScope) ->
        $rootScope.$on '$stateChangeSuccess', (event, toState, toParams, fromState, fromParams) ->
            $rootScope.prviousState = fromState.name
            
            return
        return

    return

) window, jQuery, angular
