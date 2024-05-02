def decorator(decorator_function_object):

    def replacement_function(*args, **kwargs):

        # PREPROCESSING CODE

        ret = decorated_function_object(*args, **kwargs)

        # POSTPROCESSING CODE

    return replacement_function

#--------------------------------------------------------------


@decorator
def any_function(....):
    st
    st
    st
    st

#-----------------------------------------------------------

