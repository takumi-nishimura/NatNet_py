from NatNetPy import NatNetClient


class OptiClientManager:
    def __init__(
        self,
        OptiServerIP: str = "127.0.0.1",
        OptiClientIP: str = "0.0.0.0",
    ):
        self.server_ip = OptiServerIP
        self.client_ip = OptiClientIP

        self.rigid_body = {}

    def receive_rigid_body_frame(self, new_id, position, rotation):
        self.rigid_body[str(new_id)] = {
            "x": position[2],
            "y": position[0],
            "z": position[1],
            "rx": rotation[3],
            "ry": rotation[1],
            "rz": -rotation[0],
            "rw": -rotation[2],
        }

    def stream_run(self):
        self.streaming_client = NatNetClient()
        self.streaming_client.set_client_address(self.client_ip)
        self.streaming_client.set_server_address(self.server_ip)
        # self.streaming_client.set_use_multicast(True)
        self.streaming_client.rigid_body_listener = self.receive_rigid_body_frame
        self.streaming_client.run()
