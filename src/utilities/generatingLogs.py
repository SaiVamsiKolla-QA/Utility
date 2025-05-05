import logging
import os


def generate_logs():
    # Get base directory by going up one level from utilities
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    logs_dir = os.path.join(base_dir, "logs")
    os.makedirs(logs_dir, exist_ok=True)

    # Create log file path
    log_file_path = os.path.join(logs_dir, "Demo.log")

    # Print to console where we're trying to create the log file
    print(f"\n\nCheck logs at:{log_file_path}\n\n")
    logging.basicConfig(

        filename=log_file_path,
        level=logging.INFO,
        format='%(asctime)s-%(levelname)s-%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p'

    )
    return logging.getLogger()


logger = generate_logs()
logger.info("Program Execution Started")
a = 21
b = 31
if a > b:
    print("Vamsi")
    logger.info("a is greater than b, hence Vamsi got printed in output")
else:
    print("Kolla")
    logger.info("a is not greater than b, hence Kolla got printed in output")
logger.info("Program ended")
