((window, $, angular) ->
    module = angular.module 'baseApp'

    module.provider 'req2Svr', ->
        map = {}

        @register = (name, func) ->
            map[name] = func
            return

        @$get = [
            '$injector'
            ($injector) ->
                (name, paramObj) ->
                    func = map[name]
                    if !func
                        throw Error 'Not Registered'
                    $injector.invoke func, undefined, paramObj
        ]
        return

    module.config [
        '$qProvider'
        ($qProvider) ->
            $qProvider.errorOnUnhandledRejections(false)
            return
    ]

    module.directive 'account', ->
        scope = {}
        templateUrl = '/static/apps/account/account.html'
        controller = [
            '$scope'
            '$element'
            'req2Svr'
            '$state'
            '$rootScope'
            ($scope, $element, req2Svr, $state, $rootScope) ->
                req2Svr = req2Svr 'account'
                



                return
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
