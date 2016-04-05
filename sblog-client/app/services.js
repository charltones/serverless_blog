angular.module('myApp.services', [])
.factory('SBlog',
  function($resource){
      return $resource('https://hug3zt8kyj.execute-api.eu-west-1.amazonaws.com/prod/sblog_backend');
  })
