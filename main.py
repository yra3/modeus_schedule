import os
import shutil

from shedule_loader import download_schedule
from shedule_reader import display_sleep_and_fall_up_times


def delete_temp_files():
    root_dir_name = os.path.dirname(__file__)
    schedule_dir = os.path.join(root_dir_name, "schedule_ics_files")
    # delete schedule files if they exist
    for i, filename in enumerate(os.listdir(schedule_dir)):
        file_name = os.path.join(schedule_dir, filename)
        try:
            os.remove(file_name)
        except IsADirectoryError:  # все папки удаляем рекурсивно
            shutil.rmtree(file_name)
        except FileNotFoundError:
            pass


def main():
    download_schedule()
    display_sleep_and_fall_up_times()
    delete_temp_files()


if __name__ == "__main__":
    main()
