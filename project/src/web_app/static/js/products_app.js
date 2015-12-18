var productsApp = angular.module('productsApp', []);

productsApp.controller('productsCtrl', function ($scope, $http) {
  $http.get('http://localhost:8000/api/list-products/').success(function(data) {
    $scope.products = data;
  });
});
