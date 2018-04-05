((window, jQuery, angular) ->
    module = angular.module 'baseApp'

    module.config [
        'req2SvrProvider'
        (req2SvrProvider) ->
            req2SvrProvider.register 'article', [
                '$http'
                ($http) ->
                    {
                        getArticles: () ->
                            $http(
                                method: 'GET'
                                url: '/api/article/list'
                            )

                        createArticle: (article) ->
                            payload =
                                name: article.name
                                link: article.link
                                will_summary: article.willSummary
                                summary: article.summary
                                tags: article.tags.join(",")
                                rate: article.rate
                            $http(
                                method: 'POST'
                                url: '/api/article/create'
                                data:  JSON.stringify(payload)
                                headers: 'Content-Type': 'application/json; charset=utf-8'
                            )

                        createTag: (tagName) ->
                            payload = 
                                name: tagName
                            $http(
                                method: 'POST'
                                url: '/api/article/tag/create'
                                data:  JSON.stringify(payload)
                                headers: 'Content-Type': 'application/json; charset=utf-8'
                            )

                        getTagsUsed: () ->
                            $http(
                                method: 'GET'
                                url: '/api/article/tag/get'
                            )


                        
                        
                        
                    }
            ]
            return
    ]
) window, jQuery, angular
