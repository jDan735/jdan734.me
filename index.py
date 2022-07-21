from server import *

import uvicorn


if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)
    # logger = logging.getLogger(__name__)
    # coloredlogs.install(fmt="%(asctime)s %(levelname)s %(message)s",
    #                     level="INFO",
    #                     logger=logger)

    uvicorn.run("app:app", port=8080, reload=True)
