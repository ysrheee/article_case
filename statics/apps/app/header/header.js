((window, angular) => {
    const module = angular.module('baseApp');
    
    module.directive('appHeader', () => {
        var scope = {};

		var templateUrl = '/static/apps/app/header/header.html';
        
		var controller = ['$scope', '$state', '$element', ($scope, $state) => {


            $scope.goLogin = () => {
                if ($state.current.name == 'account.login')
                    $state.reload();
                else
                    $state.go('account.login');
                }

        
            $scope.goArticle = () => {
                if ($state.current.name == 'article.list')
                    $state.reload();
                else
                    $state.go('article.list');
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