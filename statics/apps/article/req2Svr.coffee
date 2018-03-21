((window, jQuery, angular) ->
    module = angular.module 'baseApp'

    module.config [
        'req2SvrProvider'
        (req2SvrProvider) ->
            req2SvrProvider.register 'article', [
                '$http'
                ($http) ->
                    {
                        createArticle: () ->
                            payload =
                                title: ''
                                url: ''
                            $http(
                                method: 'POST'
                                url: '/api/article/create'
                                data:  JSON.stringify(payload)
                                headers: 'Content-Type': 'application/json; charset=utf-8'
                            )
                    }
            ]
            return
    ]
) window, jQuery, angular
