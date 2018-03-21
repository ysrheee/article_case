((window, jQuery, angular) ->
    module = angular.module 'baseApp'

    module.config [
        'req2SvrProvider'
        (req2SvrProvider) ->
            req2SvrProvider.register 'article', [
                '$http'
                ($http) ->
                    {
                        createArticle: (article) ->
                            payload =
                                name: article.name
                                link: article.link
                            console.log payload
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
