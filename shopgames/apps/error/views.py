from django.shortcuts import render

ERROR_404_TEMPLATE_NAME = "404.html"
ERROR_403_TEMPLATE_NAME = "403.html"
ERROR_400_TEMPLATE_NAME = "400.html"
ERROR_500_TEMPLATE_NAME = "500.html"


def bad_request(request, exception, template_name=ERROR_400_TEMPLATE_NAME):
    print("bad_request")
    response = render(request, "error/" + template_name)
    response.status_code = 400
    return response


def permission_denied(request, exception, template_name=ERROR_403_TEMPLATE_NAME):
    print("permission_denied")
    response = render(request, "error/" + template_name)
    response.status_code = 403
    return response


def server_error(request, template_name=ERROR_500_TEMPLATE_NAME):
    print("server_error")
    response = render(request, "error/" + template_name)
    response.status_code = 500
    return response


def page_not_found(request, exception, template_name=ERROR_404_TEMPLATE_NAME):
    print("page_not_found")
    response = render(request, "error/" + template_name)
    response.status_code = 404
    return response
