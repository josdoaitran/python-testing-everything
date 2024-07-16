import pytest

def pytest_sessionfinish(session, exitstatus):
    """
    Called after the whole test run finished, right before returning the exit status to the system.
    """
    # Get the summary of test results
    terminal_reporter = session.config.pluginmanager.get_plugin('terminalreporter')
    if terminal_reporter:
        summary = terminal_reporter.stats
        passed = len(summary.get('passed', []))
        failed = len(summary.get('failed', []))

        print(f"Number of passed tests: {passed}")
        print(f"Number of failed tests: {failed}")

        # Optionally, you can write these results to a file
        with open('test_summary.txt', 'w') as f:
            f.write(f"Number of passed tests: {passed}\n")
            f.write(f"Number of failed tests: {failed}\n")