var baseApp;

baseApp = angular.module("baseApp", ['ui.router']);

baseApp.config(function($interpolateProvider, $sceProvider, $httpProvider) {
  $interpolateProvider.startSymbol("{$");
  return $interpolateProvider.endSymbol("$}");
});

baseApp.controller("BaseCtrl", [
  "$scope", "$rootScope", "$http", function($scope, $rootScope, $http) {
    "list에 해당 value가 있는지 체크하는 함수";
    return $scope.containsValue = function(obj, list) {
      var i;
      i = 0;
      while (i < list.length) {
        if (list[i] === obj) {
          return true;
        }
        i++;
      }
      return false;
    };
  }
]);

window.getParameterByName = function(name) {
  var regex, results, url;
  url = window.location.href;
  name = name.replace(/[\[\]]/g, "\\$&");
  regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)");
  results = regex.exec(url);
  if (results === null) {
    return null;
  }
  if (results[2] === null) {
    return '';
  }
  return decodeURIComponent(results[2].replace(/\+/g, " "));
};

window.notMobile = function() {
  if ($(window).width() < 992) {
    return false;
  } else {
    return true;
  }
};




