((window, jQuery, angular) ->
    module = angular.module 'baseApp'

    module.directive 'accountLogin', () ->
        scope = {}
        templateUrl = '/static/apps/account/login/login.html'
        controller = [
            '$scope'
            '$element'
            'req2Svr'
            '$state'
            '$rootScope'
            '$timeout'
            ($scope, $element, req2Svr, $state, $rootScope, $tiemout) ->
                req2Svr = req2Svr 'account'
                $scope.user = 
                    email: ""
                    password: ""

                $scope.login = () ->
                    req2Svr.login($scope.user).then ((response) ->
                        $state.go 'article.list'
                        ), (error) ->
                            console.log error


                


        ]

        return {
            restrict: 'E'
            scope: scope
            templateUrl: templateUrl
            replace: true
            controller: controller
        }
    return
) window, jQuery, angular

