# Lennicam

Raspberry pi local webcam setup

## Setup
Make sure you have a raspberry pi with a camera connected, then
copy the files to the raspberry pi, register and enable the systemd target:

```bash
$ scp ./* pi@raspberrypi:~/lennicam/
$ ssh pi@raspberrypi
# cd lennicam
# cp lennicam.service ~/.config/systemd/user
# systemctl --user daemon-reload
# systemctl --user enable lennicam.service
# systemctl --user start lennicam.service
```

then go to [http://raspberrypi:8000](http://raspberrypi:8000)
and you should be able to see the camera feed.
