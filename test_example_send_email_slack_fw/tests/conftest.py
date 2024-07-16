import logging
import pytest
from datetime import datetime
from test_example_send_email_slack_fw.utils.send_email import EmailUtils
from test_example_send_email_slack_fw.utils.send_slack import SlackUtils

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(format='%(name)s-%(levelname)s-%(message)s')

class BaseTest:
    testStartTime = ""

def get_current_time():
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H-%M-%S")
    return formatted_time

@pytest.fixture(scope="session")
def before_test():
    BaseTest.testStartTime = get_current_time

def pytest_sessionfinish(session, exitstatus):
    """
    Called after the whole test run finished, right before returning the exit status to the system.
    """
    # Get the summary of test results
    terminal_reporter = session.config.pluginmanager.get_plugin('terminalreporter')
    if terminal_reporter:
        summary = terminal_reporter.stats
        passed_tests = len(summary.get('passed', []))
        failed_tests = len(summary.get('failed', []))

        logger.info(f"Number of passed tests: {passed_tests}")
        logger.info(f"Number of failed tests: {failed_tests}")

        # Optionally, you can write these results to a file
        with open('test_summary.txt', 'w') as f:
            f.write(f"Number of passed tests: {passed_tests}\n")
            f.write(f"Number of failed tests: {failed_tests}\n")

        SlackUtils.send_slack_message(f":white_check_mark: Passed Tests: {passed_tests} \n :x: Failed Tests: {failed_tests}")
        EmailUtils.send_email("Test Email",
                              f"Testing Slack Test was started at: {BaseTest.testStartTime} \n "
                              f"Passed Tests: {passed_tests} \n Failed Tests: {failed_tests}")
