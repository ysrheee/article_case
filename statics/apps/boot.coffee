((window, $, angular) ->
#    module = angular.module 'baseApp', ['ui.router']
#    module.config [
#        '$httpProvider'
#        ($httpProvider) ->
#            $httpProvider.defaults.xsrfCookieName = 'csrftoken'
#            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'
#            return
#    ]  
#    return

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
    return
) window, jQuery, angular