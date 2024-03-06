import requests
from rich import print

host = "127.0.0.1"
port = "50021"

def get_speakers():
    res = requests.get(f"http://{host}:{port}/speakers")
    print(res.json())

if __name__ == "__main__":
    get_speakers()

"""'name': 'もち子さん',
        'speaker_uuid': '9f3ee141-26ad-437e-97bd-d22298d02ad2',
        'styles': [
            {'name': 'ノーマル', 'id': 20, 'type': 'talk'},
            {'name': 'セクシー／あん子', 'id': 66, 'type': 'talk'},
            {'name': '泣き', 'id': 77, 'type': 'talk'},
            {'name': '怒り', 'id': 78, 'type': 'talk'},
            {'name': '喜び', 'id': 79, 'type': 'talk'},
            {'name': 'のんびり', 'id': 80, 'type': 'talk'}"""