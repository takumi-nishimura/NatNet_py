import itertools
import time

import pandas as pd
from OptiClient import OptiClientManager

if __name__ == "__main__":
    opti_manager = OptiClientManager()
    opti_manager.stream_run()

    save_data = None
    time.sleep(1)

    _columns = []
    for n in opti_manager.rigid_body.keys():
        for i, j in enumerate(["x", "y", "z", "rx", "ry", "rz", "rw"]):
            _columns.append(j + n)
    save_data = pd.DataFrame(columns=_columns)

    while True:
        # print(opti_manager.rigid_body.keys())
        try:
            _d = [list(body.values()) for body in opti_manager.rigid_body.values()]
            save_data = pd.concat(
                [
                    save_data,
                    pd.DataFrame(data=[list(itertools.chain(*_d))], columns=_columns),
                ]
            )
        except KeyboardInterrupt:
            print(save_data)
            opti_manager.streaming_client.shutdown()
            break
        except:
            pass
