def wind_speed(u,v,w):
    ''' calculates wind speed from u and v, and w components.'''
    return sqrt(u * u + v * v + w * w)