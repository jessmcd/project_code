def wind_speed(u,v,w = 0):
    ''' calculates wind speed from u and v, and w components.'''
    return sqrt(u * u + v * v + w * w)