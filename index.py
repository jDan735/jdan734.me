import coloredlogs, logging

from ftp import *
from server import *
from app import app


if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)
    # logger = logging.getLogger(__name__)
    # coloredlogs.install(fmt="%(asctime)s %(levelname)s %(message)s",
    #                     level="INFO",
    #                     logger=logger)
    
    app.run(port=5050) # debug=True
