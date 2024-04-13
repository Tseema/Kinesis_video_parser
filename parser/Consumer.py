import io
import time
import cv2
import imageio as iio
import boto3
import timeit
import MKV_tags as mkv

class Consume:
    def transcode_frame(frame):
        # Encode frame into bytes for job submission
        img_str = cv2.imencode('.jpg', frame)[1].tobytes()
        return img_str


    def get_frame(chunk):
        try:
            fragment = iio.v3.imread(io.BytesIO(chunk), format_hint=".mkv")
            for num, im in enumerate(fragment):
                if num % 10 == 0:
                    sts = 0
                    print("Frame captured")
                    break
            print("Returning result")
            return im, sts
            # print(f'Finish one chunk took: {timeit.default_timer() - start_time}')
        except OSError as e:
            print("Broken fragment received")
            sts = 1
            return None, sts


    def read_chunk(fragment):
        chunk = fragment['Payload'].read(1024 * 8 * 8)
        mkv.getMkvTagVal(chunk)
        return chunk


    def get_fragment(self):
        media_client = boto3.client('kinesis-video-media', endpoint_url=kvs_endpoint, region_name='ap-southeast-1',
                                    aws_access_key_id="AKIAV77QVY6UH47T4DM7",
                                    aws_secret_access_key="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")
        fragment = media_client.get_media(
            StreamName="testozabesto",
            StartSelector={
                'StartSelectorType': 'NOW'
            }
        )
        # print(f'Downloading one chunk took: {timeit.default_timer() - start_time}')
        print('Fragment downloaded ', fragment)
        return fragment


    def run(self):
        while True:
            start_time = timeit.default_timer()
            fragment = self.get_fragment()
            chunk = self.read_chunk(fragment)
            if not chunk:
                break

            im, sts = self.get_frame(chunk)

            if sts != 0:
                time.sleep(0.25)
                continue
            img_str = self.transcode_frame(im)
            try:
                # put_queue(img_str)
                time.sleep(0.25)
                end_time = timeit.default_timer()
            except:
                print('Cannot connect to RabbitMQ')
                time.sleep(3)
                continue
            # print('Time between fragment download and frame processing: {overalltime}'.format(overalltime))