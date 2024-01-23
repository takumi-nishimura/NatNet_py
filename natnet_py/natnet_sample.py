from OptiClient import OptiClientManager

if __name__ == "__main__":
    opti_manager = OptiClientManager()
    opti_manager.stream_run()

    while True:
        try:
            print(opti_manager.rigid_body)
        except KeyboardInterrupt:
            opti_manager.streaming_client.shutdown()
            break
        except:
            pass
