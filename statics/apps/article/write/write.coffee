((window, jQuery, angular) ->
    module = angular.module 'baseApp'

    module.directive 'articleWrite', () ->
        scope = {}
        templateUrl = '/static/apps/article/write/write.html'
        controller = [
            '$scope'
            '$element'
            'req2Svr'
            '$state'
            '$rootScope'
            '$timeout'
            ($scope, $element, req2Svr, $state, $rootScope, $tiemout) ->
                req2Svr = req2Svr 'article'

                $scope.article = 
                    name: ""
                    link: ""

                $scope.submit = () ->
                    req2Svr.createArticle($scope.article).then ((response) ->
                        console.log response
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

