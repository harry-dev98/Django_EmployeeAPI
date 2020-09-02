

def cors_middleware(get_response):
    '''
        middleware to all request from all origins

        get_response : function to get request response :: function ::
    '''
    def middleware(request):
        '''
            core of cors_middleware called on the request before
            views are called

            request : request received :: object ::
        '''

        # this part is executed before views are called
        response = get_response(request)
        # this part is executed after views are called
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "*"
        return response

    return middleware