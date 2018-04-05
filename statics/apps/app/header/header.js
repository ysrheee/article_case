((window, angular) => {
    const module = angular.module('baseApp');

    module.provider('req2Svr', function() {
        var map;
        map = {};
        this.register = function(name, func) {
          map[name] = func;
        };
        this.$get = [
          '$injector', function($injector) {
            return function(name, paramObj) {
              var func;
              func = map[name];
              if (!func) {
                throw Error('Not Registered');
              }
              return $injector.invoke(func, void 0, paramObj);
            };
          }
        ];
      });
      
      module.config([
        '$qProvider', function($qProvider) {
          $qProvider.errorOnUnhandledRejections(false);
        }
    ]);
    
    module.directive('appHeader', () => {
        var scope = {};

		var templateUrl = '/static/apps/app/header/header.html';
        
		var controller = ['$scope', '$state', '$element', 'req2Svr', ($scope, $state, $element, req2Svr) => {
            req2Svr = req2Svr('account');

            $scope.user = {
                email: userInfo.email
            }

            $scope.isAuthenticated = isAuthenticated
                


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

            $scope.goLogout = () => {
                req2Svr.logout().then((function(response) {
                    window.location.href = '/';
                  }), function(error) {
                    return console.log(error);
                  });

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