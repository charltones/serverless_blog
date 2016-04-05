'use strict';

angular.module('myApp.view1', ['ngRoute', 'myApp.services'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/view1', {
    templateUrl: 'view1/view1.html',
    controller: 'View1Ctrl'
  });
}])

.controller('View1Ctrl', function($scope, $timeout, SBlog) {
    $scope.loading = false;

    $scope.update = function() {
	var blogs = SBlog.save({'operation':'list'}, function(data) {
	    //console.log(data);
	    $scope.sblogs = data.Items;
	}, function(error) {
	});
	// update once per second
	$scope.update_timeout = $timeout($scope.update, 3000);
    };

    $scope.blog = function() {
	$scope.loading = true;
	SBlog.save({'operation':'create',
		    'name':$scope.entry.name,
		    'sblog':$scope.entry.sblog}, function(data) {
	    console.log(data);
            $scope.loading = false;
	}, function(error) {
	});
    };

    $scope.$on('$destroy', function(){
	$timeout.cancel($scope.update_timeout);
    });

    $scope.update();
});
