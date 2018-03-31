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

                $scope.user = 
                    articles: []

                $scope.init = () ->
                    $scope.getArticles()

                $scope.getArticles = () ->
                    req2Svr.getArticles().then ((response) ->
                        console.log response
                        for article in response.data
                            $scope.user.articles.push new  Article(article)
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


class Article
    constructor: (articleData) ->
        @id = articleData.id
        @name = articleData.name
        @link = articleData.link
        @rate = articleData.rate
        @willSummary = articleData.will_summary
        @summary = articleData.summary
        @tags = []
        for tag in articleData.tags
            @tags.push tag
        @createdAt = articleData.created_at


