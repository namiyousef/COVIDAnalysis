import hashlib


def hello_world():
    return 'Hello World!'

def echo_message(body, message, encrypt, repeat):
    """ Function to return the message passed. Note that the variable name
    `message` must be the same as that defined in your yaml file
    """

    return_msg = ''
    if body:
        return_msg += f'HEADER: {body.decode()}, '

    if encrypt:
        hash_object = hashlib.md5(message.encode())
        message = hash_object.hexdigest()

    return_msg += f'YOUR ECHO MESSAGE: {message*repeat}'
    return return_msg
