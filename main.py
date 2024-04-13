from parser.Consumer import Consume
import boto3

consumer = Consume()
kvs_client = boto3.client("kinesisvideo",
                          region_name='ap-southeast-1',
                          aws_access_key_id="AKIAV77QVY6UH47T4DM7",
                          aws_secret_access_key="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")

kvs_endpoint = kvs_client.get_data_endpoint(
    StreamName="testozabesto",
    APIName='GET_MEDIA'
)['DataEndpoint']

consumer.run()