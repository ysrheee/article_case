((window, jQuery, angular) ->
    module = angular.module 'baseApp'

    module.config [
        'req2SvrProvider'
        (req2SvrProvider) ->
            req2SvrProvider.register 'account', [
                '$http'
                ($http) ->
                    {
                        signup: (user) ->
                            payload =
                                email: user.email
                                password: user.password
                            $http(
                                method: 'POST'
                                url: '/api/user/signup/'
                                data:  JSON.stringify(payload)
                                headers: 'Content-Type': 'application/json; charset=utf-8'
                            )

                        login: (user) ->
                            payload =
                                email: user.email
                                password: user.password
                            $http(
                                method: 'POST'
                                url: '/api/user/login/'
                                data:  JSON.stringify(payload)
                                headers: 'Content-Type': 'application/json; charset=utf-8'
                            )

                        
                        
                        
                    }
            ]
            return
    ]
) window, jQuery, angular
