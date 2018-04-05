((window, jQuery, angular) ->
    module = angular.module 'baseApp'

    module.directive 'accountSignup', () ->
        scope = {}
        templateUrl = '/static/apps/account/signup/signup.html'
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

                $scope.signup = () ->
                    req2Svr.signup($scope.user).then ((response) ->
                        alert("가입이 완료되었습니다.")
                        window.location.href = '/article'
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

