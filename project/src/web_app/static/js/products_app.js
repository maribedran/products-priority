if (!Object.toparams) {
    Object.toparams = function ObjectToParams(obj) {
        var p = [];
        for (var key in obj) {
            p.push(key + '=' + obj[key])
        }
        return p.join('&')
    };
}

var productsApp = angular.module('productsApp', []);

productsApp.controller('productsCtrl', function ($scope, $http) {

  var page = {}
  page.update_ids = []

  page.set_loading = function(bool){
    page.loading = !!bool;
  }

  page.get_products = function(){
    page.set_loading(true);

    $http.get('http://localhost:8000/api/list-products/')
      .success(function(data){
        page.products = data;
        page.set_loading(false);
      })
      .error(function(){
        page.set_loading(false);
      });
  }

  page.toggle_mark_update = function(product){
    var index = page.update_ids.indexOf(product.id)
    if (index === -1){
      page.update_ids.push(product.id)
    } else {
      page.update_ids.splice(index, 1)
    }
  }

  page.clean_update = function(){
    page.update_ids = [];
  }

  page.check_update = function(product){
    var index = page.update_ids.indexOf(product.id)
      if (index === -1) return false
    return true;
  }

  page.toggle_priority = function(product){
    var new_priority = !product.priority
    page.update_product(product, {priority: new_priority})
  }

  page.update_product = function(product, data){
    page.set_loading(true);
    $http.post('http://localhost:8000/api/update-product/' + product.id + '/', data).success(function(data) {
      product.priority = data.priority
      page.set_loading(false);
      page.clean_update();
    });
  }

  page.bulk_update = function(priority){
    data = {update_ids: page.update_ids, priority: priority}
    page.set_loading(true);
    $http.post('http://localhost:8000/api/update-many/', data).success(function(data) {
      page.get_products();
      page.set_loading(false);
      page.clean_update();
    });
  }

  $scope.page = page;
});
