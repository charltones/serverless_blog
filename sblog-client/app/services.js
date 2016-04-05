angular.module('myApp.services', [])
.factory('SBlog',
  function($resource){
      return $resource('https://<your API gateway endpoint>/prod/sblog_backend');
  })
