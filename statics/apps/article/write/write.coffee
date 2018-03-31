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

                $scope.users = 
                    tagsUsed: []

                $scope.article = 
                    name: ""
                    link: ""
                    willSummary: false
                    summary: ""
                    tags: []
                    rate: ""

                $scope.init = () ->
                    $scope.getTagsUsed()
                    

                $scope.submit = () ->
                    req2Svr.createArticle($scope.article).then ((response) ->
                        console.log response
                        ), (error) ->
                            console.log error

                $scope.getTagsUsed = () ->
                    req2Svr.getTagsUsed().then ((response) ->
                        for tag in response.data
                            $scope.users.tagsUsed.push tag
                        console.log $scope.users.tagsUsed
                        ), (error) ->
                            console.log error

                $scope.createNewTag = () ->
                    req2Svr.createTag($scope.newTag).then ((response) ->
                        $scope.article.tags.push $scope.newTag
                        console.log response
                        ), (error) ->
                            console.log error

                $scope.addTag = (tag) ->
                    idx = $scope.article.tags.indexOf(tag)
                    if idx == -1
                        $scope.article.tags.push tag
                    else
                        $scope.article.tags.splice(idx)






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

