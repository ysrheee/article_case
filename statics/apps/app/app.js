;(function (window, $, angular, undefined) {
	var module = angular.module('baseApp');

	module.directive('articleCase', function () {
		var scope = {};

		var templateUrl = '/static/apps/app/app.html';

		var controller = ['$scope', '$element', function ($scope, $element, locale, $http) {}];

		return {
			restrict: 'E',
			scope: scope,
			templateUrl: templateUrl,
			replace: true,
			controller: controller
		};
	});

})(window, jQuery, angular);