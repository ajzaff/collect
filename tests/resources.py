import os

res_dir = os.path.abspath('res')


def get_res(name, path=None):
    """Gets a resource from the res/ directory

    :param name: (str) resource name
    :param path: (str) relative path to resource (from res/)
        default: None
    :return:
    """
    if path:
        return '%s/%s/%s' % (res_dir, path, name)
    else:
        return '%s/%s' % (res_dir, name)