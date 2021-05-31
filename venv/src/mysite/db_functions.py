from mysite.models import Coords

def get_coords_from_db():
    coords_object = Coords.objects.first()
    if coords_object is None:
        return False
    coords = [str(coords_object.latitude), str(coords_object.longitude)]
   
    return coords

    
def remove_and_replace_coords(lat_val, long_val):
    _remove_coords()
    _add_coords(lat_val, long_val)


def _remove_coords():
    # Delete the entry that exists in coords table
    coords_to_delete = Coords.objects.first()
    if coords_to_delete is not None:
        coords_to_delete.delete()


def _add_coords(lat_val, long_val):
    # Add new coords
    new_coords = Coords(id=1, latitude=lat_val, longitude=long_val)
    new_coords.save()