((window, angular) => {
    const module = angular.module('baseApp');
    
    module.directive('appHeader', () => {
        var scope = {};

		var templateUrl = '/static/apps/app/header/header.html';
        
		var controller = ['$scope', '$state', '$element', ($scope, $state) => {
            



            $scope.goArticle = () => {
                console.log("go article")
                if ($state.current.name.indexOf("article") != -1)
                    $state.reload();
                else
                    $state.go('article');
                }


            $scope.goMypage = () => {
                if ($state.current.name.indexOf("mypage") != -1)
                    $state.reload();
                else
                    $state.go('mypage');
                }

            
        }];

		return {
			restrict: 'E',
			scope: scope,
			templateUrl: templateUrl,
			replace: true,
			controller: controller
		};
    });
})(window, angular);