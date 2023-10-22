from datetime import datetime


def get_obj_datetime(string: str) -> datetime:
    """ Returns a datetime object from string with format %Y-%m-%dT%H:%M:%S.%fZ"""
    return datetime.strptime(string, '%Y-%m-%dT%H:%M:%S.%fZ')