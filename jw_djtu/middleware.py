from django.http import HttpResponseRedirect


class UserAuthMiddleware():

    def process_response(self, request, response):
        if request.path != '/signin/' and request.path != '/dosignin/':
            try:
                status = request.session['signin_status']
                username = request.session['signin_username']
                user_id = request.session['signin_id']
            except KeyError:
                response = HttpResponseRedirect('/signin/')
            else:
                if not status or username is None or user_id is None:
                    response = HttpResponseRedirect('/signin/')

        return response
