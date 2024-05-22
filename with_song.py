import time
import main
try:
    import vlc
except ModuleNotFoundError:
    print('Установите модуль python-vlc командой `python -m pip install python-vlc`')
    exit(1)

def time_ms():
    return time.monotonic_ns() // 1000000

class SongPlayer:
    def __init__(self, songname: str):
        self.stop_playing_time: int | None = None
        self.player: vlc.MediaPlayer = vlc.MediaPlayer(songname) # type: ignore
    
    def ensure(self):
        if self.stop_playing_time and self.stop_playing_time < time_ms():
            self.player.stop()
            self.stop_playing_time = None
    
    def continue_playing(self, playtime_ms: int):
        if not self.stop_playing_time:
            self.stop_playing_time = time_ms() + playtime_ms
            self.player.play()
        else:
            if not self.player.is_playing():
                self.player.play()
            self.stop_playing_time += playtime_ms
    
    def stop(self):
        self.stop_playing_time = None
        self.player.stop()

PLAYTIME_MS = 3000
player = SongPlayer('chiki-briki-i-v-damki.mp3')

def event_handler(event: main.Event):
    if event == 'wait':
        player.ensure()
    elif event == 'correct':
        player.continue_playing(PLAYTIME_MS)
    elif event == 'wrong':
        player.stop()
    else:
        raise ValueError(f'Unknown event {event}')
    
main.main(event_handler)
