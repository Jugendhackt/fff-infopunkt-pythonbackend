from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
import json
data = json.load(open('config.json'))

class StrikeModel(Model):
    """
    A DynamoDB Strike
    """
    class Meta:
        table_name = "FFF-Strikes"
        # AWS Config Specifies the region
        region = 'eu-central-1'
        # Access keys
        aws_access_key_id = data['aws']['access_key']
        aws_secret_access_key = data['aws']['private_key']
        '''
        # If hosted by us :-) host = "http://116.203.195.66:4567"
        host = data['aws']['host']
        aws_access_key_id = data['aws']['access_key']
        aws_secret_access_key = data['aws']['private_key']
        '''
    # The model:
    strikeId = NumberAttribute(hash_key=True)
    date = UnicodeAttribute()
    startTime = UnicodeAttribute()
    organisation = UnicodeAttribute()
    title = UnicodeAttribute()
    latitude = NumberAttribute()
    longitude = NumberAttribute()
    url = UnicodeAttribute()
    description = UnicodeAttribute()
    meetingPoint = UnicodeAttribute()
    endPoint = UnicodeAttribute()
    routeLength = UnicodeAttribute()
    searchTitle = UnicodeAttribute()
    source = UnicodeAttribute()
    groupSource = UnicodeAttribute()
