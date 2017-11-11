def wind_speed(u,v,w = 0):
    ''' calculates wind speed from u and v, and w components.'''
    return sqrt(u * u + v * v + w * w)

def get_wind_direction(u,v):
    return 90 - atan2(u,v, degrees=True)


def CRAZZZYYY(LOL):
   print('HELL YA DUDE')
   return LOL * 10