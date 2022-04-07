# equirectangular approximation
import math
#let dlat be the difference in the latitudes of the two points, in radians
#let dlon be the difference in the longitudes of the two points, in radians
#let alat be the average of the two latitudes, in radians
dlat = latitude1 - latitude2
dlon = longitude1 - longitude2
alat = (latitude1 + latitude2) / 2
x = dlon * math.cos(alat)
d = math.sqrt(x**2 + dlat**2) * 3958.8


def concentration_to_aqi(concentration: float) -> int:
# wip
    if 0 <= concentration < 12.1:
        if concentration == 0.0:
            aqi = 0
        elif concentration == 12.0:
            aqi = 50
        else:
            aqi = 
    
