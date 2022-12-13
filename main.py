from fetch_nasa_apod import fetch_nasa_apod
from fetch_spacex_images import fetch_spacex_last_launch
from fetch_nasa_epic import fetch_nasa_epic


def main():
    fetch_spacex_last_launch()
    fetch_nasa_apod()
    fetch_nasa_epic()


if __name__ == "__main__":
    main()
