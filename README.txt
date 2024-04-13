README

What is this repository for?
    This repository contains the python script to consume a KVS stream using boto3's "GET_MEDIA" API.
    On consumption , we try and regex some mkv tags present as part of the response payload required for down stream processes.
    The following link sheds more light on of the above api and the detail response syntax.
        https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_dataplane_GetMedia.html

How do I get set up?
    As there is no setup file this repo would need the below packages installed before running the code.
    boot3
    imageio
    opencv

Dependencies
    Since this is only the consumer code,to test the values in local we would also require to have the AWS producer SDK.

How to run
    once the KVS producer is up and running and streaming the video simply run the consumer.py file (no arguments).
    It should read the response and process frame by frame data and print the values for the following mkv tags from metadata :
    AWS_KINESISVIDEO_FRAGMENT_NUMBER
    AWS_KINESISVIDEO_SERVER_TIMESTAMP
    AWS_KINESISVIDEO_PRODUCER_TIMESTAMP

Other guidelines
    Since amazon gives the flexibility to add custom tags into the metadata, in the future the MKV_tags.py can
    be extended to regex for more tags from the producer.

Other community or team contact
       source from github:
       https://github.com/aws/amazon-kinesis-video-streams-parser-library/issues/87