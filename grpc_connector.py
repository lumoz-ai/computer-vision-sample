import json
from time import time

from bricksdk.configurations import Configuration
from bricksdk.connectors.grpc.grpc_output_connector import GrpcOutputConnector
from protos import image_1_pb2 as image_pb2

config = Configuration()
config.load(configuration_json=json.load(open("sample_configuration.json", "r")))


connector = GrpcOutputConnector(config = config, proto_file_path = 'protos/image_detection_3.proto')
#connector = get_connector(config=config, brick_processor=BrickProcessor(), input_proto_file_path="protos/image_detection_3.proto",
 #                         output_proto_file_path="protos/image_detection_3.proto")
connector.initialize()
connector.start()

with open('car.jpg', 'rb') as car_image_bytes:
    car_bytes = car_image_bytes.read()
    image = image_pb2.Image(imageID=1, imageBytes=car_bytes, imageWidth=256, imageHeight=256, numberOfChannels=3,
                        sentAt=time())
    images = image_pb2.Images(images=[image])

    res = connector.send(images)
    print(res)
