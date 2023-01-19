import requests
import simpleaudio
from time import sleep

goal_rate = 20000 #example


def get_current_rate():
    url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
    headers = {'X-CoinAPI-Key': 'GetFreeAPIKeyFrom_CoinApi.io'}
    response = requests.get(url, headers=headers)

    current_rate = response.json()['rate']

    return current_rate


def notify_user():
    print(f'Der Kurs hat das Goal von {goal_rate} USD erreicht!')

    wave_object = simpleaudio.WaveObject.from_wave_file(
        '/home/dci-student/projects/private_project/crypto_tracker/sounds/kaching.wav')
    play_object = wave_object.play()
    play_object.wait_done()

    exit()


def compare_current_rate_with_goal():
    current_rate = get_current_rate()

    if current_rate >= goal_rate:
        notify_user()

    print(f'Aktueller Kurs: {round(current_rate)} USD')


def track_rate():
    while True:
        print('\nTracke den aktuellen Kurs...')
        compare_current_rate_with_goal()
        sleep(5)


if __name__ == "__main__":
    track_rate()

compare_current_rate_with_goal()
