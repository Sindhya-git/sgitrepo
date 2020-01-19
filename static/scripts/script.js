
let recorder;


const recordMic = document.getElementById('mic');
recordMic.onclick = function() {
  const fullPath = recordMic.src;
  const filename = fullPath.replace(/^.*[\\/]/, '');
  if (filename == 'mic.gif') {
    try {
      
      startRecording();
      console.log('recorder started');
      $('#q').val('I am listening ...');
    } catch (ex) {
      // console.log("Recognizer error .....");
    }
  } 
};

function stopRecording(button) {
  recorder && recorder.stop();
  console.log('Stopped recording.');

  recorder &&
    recorder.exportWAV(function(blob) {
      console.log(blob);
      const url = '/api/speech-to-text';
      const request = new XMLHttpRequest();
      request.open('POST', url, true);
      // request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

      // Decode asynchronously
      request.onload = function() {
        callConversation(request.response);
        displayMsgDiv(request.response, 'user');
      };
      request.send(blob);
    });

  recorder.clear();
}

window.onload = function init() {
  try {
    // webkit shim
    window.AudioContext = window.AudioContext || window.webkitAudioContext;
    navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia;
    // eslint-disable-next-line
    window.URL = window.URL || window.webkitURL;

    context = new AudioContext();
    console.log('Audio context set up.');
    console.log('navigator.getUserMedia ' + (navigator.getUserMedia ? 'available.' : 'not present!'));
  } catch (e) {
    alert('No web audio support in this browser!');
  }

  navigator.getUserMedia(
    {
      audio: true
    },
    startUserMedia,
    function(e) {
      console.log('No live audio input: ' + e);
    }
  );
};
