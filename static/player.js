
function playpause() {
  if (!song.paused) {
    song.pause();
  } else {
    song.play();
  }
}


function mute() {
  if (muted) {
    song.volume = vol;
    muted = false;
    document.getElementById('mute').innerHTML = '<i class="fa fa-volume-up"></i>';
  } else {
    song.volume = 0;
    muted = true;
    document.getElementById('mute').innerHTML = '<i class="fa fa-volume-off"></i>';
  }
}

function setVolume(volume) {
  song.volume = volume;
  vol = volume;
}
