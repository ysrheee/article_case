((window, jQuery, angular) ->
    module = angular.module 'baseApp'

    module.directive 'articleList', () ->
        scope = {}
        templateUrl = '/static/apps/article/list/list.html'
        controller = [
            '$scope'
            '$element'
            'req2Svr'
            '$state'
            '$rootScope'
            '$timeout'
            ($scope, $element, req2Svr, $state, $rootScope, $tiemout) ->
                req2Svr = req2Svr 'article'

                


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

