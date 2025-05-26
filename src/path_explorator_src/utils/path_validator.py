from ..exceptions import PathGoesBeyondLimits

def raise_if_path_goes_beyond_limits(limit_path: str, path: str):
    if not path.startswith(limit_path):
        raise PathGoesBeyondLimits(path)
    return False