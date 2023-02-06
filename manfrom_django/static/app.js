new Vue({
    el: '#visitor_app',
    data: {
    visitors: []
    },
    created: function () {
        const vm = this;
        axios.get('/api/visitors/')
        .then(function (response){
        vm.visitors = response.data
        })
    }
}
)