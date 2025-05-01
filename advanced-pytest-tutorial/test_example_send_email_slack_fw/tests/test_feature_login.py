import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(format='%(name)s-%(levelname)s-%(message)s')
def test_feature_login():
    logger.info("Test Feature Login")
    assert True