from django.db import models

class PolygonModel(models.Model):
    # Define fields according to your database schema
    pin = models.CharField(max_length=100)
    geomjson = models.CharField(max_length=100)
    # field_2 = models.CharField(max_length=100)
    # field_5 = models.CharField(max_length=100)
    # propertycity = models.CharField(max_length=100)

    class Meta:
        managed = True  # This model does not have a database table as it's a view
    #     db_table = 'allegheny_polygons'  # Replace 'your_polygon_table' with your actual table name
    def __str__(self):
        return self.pin
class PolyModel(models.Model):
    # Define fields according to your database schema
    pin = models.CharField(max_length=100)
    geomjson = models.CharField(max_length=250)
    # field_2 = models.CharField(max_length=100)
    # field_5 = models.CharField(max_length=100)
    # propertycity = models.CharField(max_length=100)

    class Meta:
        managed = True  # This model does not have a database table as it's a view
    #     db_table = 'allegheny_polygons'  # Replace 'your_polygon_table' with your actual table name
    def __str__(self):
        return self.pin
class Parcels(models.Model):
    doc_num = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    file_date = models.CharField(max_length=100)
    agmt_type = models.CharField(max_length=100)
    dv_url = models.CharField(max_length=100)
    classdesc = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    schooldesc = models.CharField(max_length=100)
    munidesc = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    bk_vol_pg = models.CharField(max_length=100)
    usedesc = models.CharField(max_length=100)
    calcacreag = models.CharField(max_length=100)
    fairmarkettotal = models.CharField(max_length=100)
    geomjson = models.CharField(max_length=250)

    class Meta:
        managed = True
    #     db_table = 'parcel_details'
    
    def __str__(self):
        return self.doc_num

class Parceldetails(models.Model):
    doc_num = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    file_date = models.CharField(max_length=100)
    agmt_type = models.CharField(max_length=100)
    dv_url = models.CharField(max_length=100)
    classdesc = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    schooldesc = models.CharField(max_length=100)
    munidesc = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    bk_vol_pg = models.CharField(max_length=100)
    usedesc = models.CharField(max_length=100)
    calcacreag = models.CharField(max_length=100)
    fairmarkettotal = models.CharField(max_length=100)
    geomjson = models.CharField(max_length=250)

    class Meta:
        managed = True
    #     db_table = 'parcel_details'
    
    def __str__(self):
        return self.doc_num

    
class Parceldetails2(models.Model):
    doc_num = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    file_date = models.CharField(max_length=100)
    agmt_type = models.CharField(max_length=100)
    dv_url = models.CharField(max_length=100)
    classdesc = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    schooldesc = models.CharField(max_length=100)
    munidesc = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    bk_vol_pg = models.CharField(max_length=100)
    usedesc = models.CharField(max_length=100)
    calcacreag = models.CharField(max_length=100)
    fairmarkettotal = models.CharField(max_length=100)
    geomjson = models.CharField(max_length=250)

    class Meta:
        managed = True
    #     db_table = 'parcel_details'
    
    def __str__(self):
        return self.doc_num


class Wellsu(models.Model):
    permit_num = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    geomjson = models.CharField(max_length=100)

    class Meta:
        managed = True
        # db_table = 'leasemap_wellsunc'
    
    def __str__(self):
        return self.permit_num
    
class Wellsc(models.Model):
    permit_num = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    geomjson = models.CharField(max_length=100)

    class Meta:
        managed = True
        # db_table = 'leasemap_wellscon'
    
    def __str__(self):
        return self.permit_num
    