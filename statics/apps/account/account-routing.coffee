((window, jQuery, angular) ->
    module = angular.module 'baseApp'

    module.config [
        '$stateProvider'
        '$urlRouterProvider'
        '$locationProvider'
        ($stateProvider, $urlRouterProvider, $locationProvider) ->
            $stateProvider.state 'account.signup', {
                url: '/signup'
                template: '<account-signup></account-signup>'
            }
            .state 'account.login', {
                url: '/login'
                template: '<account-login></account-login>'
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
