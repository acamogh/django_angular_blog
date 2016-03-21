sampleApp.controller('index_ctrl', function($scope, $http) {
    $scope.message = 'Follow-up';
    $scope.filteredTodos = []
   ,$scope.currentPage = 1
   ,$scope.numPerPage = 10
   ,$scope.maxSize = 5;

    $http.get("http://127.0.0.1:8000/api.json")
        .success(function(response) {
            $scope.data = response;
            //console.log($scope.data)
        });

});

sampleApp.controller('detail_ctrl', function($scope, $http, $routeParams, $cookies) {
    $scope.message = 'Follow-up';
    $scope.currentId = $routeParams.id;
    $scope.data123={}
    $scope.title_comment=[]

    $http.get("http://127.0.0.1:8000/api.json")
        .success(function(response) {
            $scope.data = response;
            for(i=0;i<$scope.data.length;i++){
                if($scope.data[i].id == $scope.currentId){
                    $scope.post=$scope.data[i];
                    $scope.title=$scope.data[i].title;
                    $scope.desc = $scope.data[i].description;
                }
            }
        });



    $http.get("http://127.0.0.1:8000/comments.json")
        .success(function(response) {
            $scope.post_comment = response;
            for(i=0;i<$scope.post_comment.length;i++){
                if($scope.post_comment[i].title == $scope.title){
                    $scope.title_comment.push($scope.post_comment[i].comments);
                }
            }
        });


    $scope.comment_form = function() {
        $scope.data123['comments']=$scope.form_comment
        $scope.data123['id']=$scope.post.id
        $scope.data123['title']=$scope.post.title

        $http({
            url: 'http://127.0.0.1:8000/add_comments/',
            data: $scope.data123,
            method: 'POST',
            headers: {
                'X-CSRFToken': $cookies['csrftoken']
            }
        }).
        success(function() {
            console.log('success');
            location.reload();

        }).
        error(function(data) {
            console.log(data);
        });
    }
});

