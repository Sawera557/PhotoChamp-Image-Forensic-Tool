import PIL.Image as PILimage
from PIL.ExifTags import TAGS, GPSTAGS


class Worker(object):
    def __init__(self, img):
        self.img = img
        self.exif_data = self.get_exif_data()
        self.raw_exif = self.exif()
        self.lat = self.get_lat()
        self.lon = self.get_lon()
        self.date = self.get_date_time()
        super(Worker, self).__init__()

    @staticmethod
    def get_if_exist(data, key):
        if key in data:
            return data[key]
        return None

    @staticmethod
    def convert_to_degress(value):
        """Helper function to convert the GPS coordinates
        stored in the EXIF to degress in float format"""
        d0 = value[0][0]
        d1 = value[0][1]
        d = float(d0) / float(d1)
        m0 = value[1][0]
        m1 = value[1][1]
        m = float(m0) / float(m1)

        s0 = value[2][0]
        s1 = value[2][1]
        s = float(s0) / float(s1)

        return d + (m / 60.0) + (s / 3600.0)

    def exif(self):
        """Return EXIF metatdata from image"""
        exif_data = {}
        try:
            tags = self.img._getexif()
            for tag, value in tags.items():
                decoded = TAGS.get(tag, tag)
                exif_data[decoded] = value
        except:
            pass
        return exif_data

    def get_exif_data(self):
        """Returns a dictionary from the exif data of an PIL Image item. Also
        converts the GPS Tags"""
        exif_data = {}
        info = self.img._getexif()
        if info:
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                if decoded == "GPSInfo":
                    gps_data = {}
                    for t in value:
                        sub_decoded = GPSTAGS.get(t, t)
                        gps_data[sub_decoded] = value[t]

                    exif_data[decoded] = gps_data
                else:
                    exif_data[decoded] = value
        return exif_data

    def get_lat(self):
        """Returns the latitude and longitude, if available, from the
        provided exif_data (obtained through get_exif_data above)"""
        # print(exif_data)
        if 'GPSInfo' in self.exif_data:
            gps_info = self.exif_data["GPSInfo"]
            gps_latitude = self.get_if_exist(gps_info, "GPSLatitude")
            gps_latitude_ref = self.get_if_exist(gps_info, 'GPSLatitudeRef')
            if gps_latitude and gps_latitude_ref:
                lat = self.convert_to_degress(gps_latitude)
                if gps_latitude_ref != "N":
                    lat = 0 - lat
                lat = str(f"{lat:.{5}f}")
                return lat
        else:
            return None

    def get_lon(self):
        """Returns the latitude and longitude, if available, from the
        provided exif_data (obtained through get_exif_data above)"""
        # print(exif_data)
        if 'GPSInfo' in self.exif_data:
            gps_info = self.exif_data["GPSInfo"]
            gps_longitude = self.get_if_exist(gps_info, 'GPSLongitude')
            gps_longitude_ref = self.get_if_exist(gps_info, 'GPSLongitudeRef')
            if gps_longitude and gps_longitude_ref:
                lon = self.convert_to_degress(gps_longitude)
                if gps_longitude_ref != "E":
                    lon = 0 - lon
                lon = str(f"{lon:.{5}f}")
                return lon
        else:
            return None

    def get_date_time(self):
        if 'DateTime' in self.exif_data:
            date_and_time = self.exif_data['DateTime']
            return date_and_time


def extractPIL(image_path):
    try:
        img = PILimage.open(image_path)
        image = Worker(img)
        lat = image.lat
        lon = image.lon
        date = image.date
        exifdataGPS = image.exif_data
        tags = image.raw_exif
        print(lat, lon)
        return lat, lon, date, tags
    except Exception as e:
        return e, e, e, e
