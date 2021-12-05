
var socket = io('ws://localhost:5001');

socket.on('connect', function() {
  console.log('connected');
  socket.emit('getState');
});

socket.on('startedProcessing', function() {
  console.log('startedProcessing');
  socket.emit('getState');
});

socket.on('receivingFiles', function() {
  console.log('receivingFiles');
  document.getElementById('loading').style.visibility = 'visibile';
  document.getElementById('loadingText').innerText = 'Uploading';
});

socket.on('currentState', function(state) {
  console.log('currentState:', state);
  switch (state) {
    case 'sleeping':
      document.getElementById('ready').style.visibility = 'hidden';
      document.getElementById('fileDrop').style.visibility = 'visibile';
      document.getElementById('loading').style.visibility = 'hidden';
      document.getElementById('loadingText').innerText = '';
      break;
    case 'ready':
      document.getElementById('ready').style.visibility = 'visibile';
      document.getElementById('fileDrop').style.visibility = 'visibile';
      document.getElementById('loading').style.visibility = 'hidden';
      document.getElementById('loadingText').innerText = '';
      break;
    case 'processing':
      document.getElementById('ready').style.visibility = 'hidden';
      document.getElementById('fileDrop').style.visibility = 'hidden';
      document.getElementById('loading').style.visibility = 'visibile';
      document.getElementById('loadingText').innerText = 'Processing spreadsheet';
      break;
    default:
  }
});

function startProcessing() {
  console.log('startProcessing');
  socket.emit('startProcessing');
  socket.emit('getState');
};

// $('#submitFiles').on('click', function() {
//   console.log('fileSubmitted...');
//   socket.emit('fileSubmitted');
// });

function clearFiles() {
  console.log('clearFiles');
  socket.emit('clearFiles');
  socket.emit('getState');
};

setInterval(function() {
  console.log('getState');
  socket.emit('getState');
}, 5000);

Dropzone.options.myDropzone = {
  autoProcessQueue: false,
  uploadMultiple: true,
  parallelUploads: 10,
  maxFiles: 10,
  init: function() {
    myDropzone = this; // closure
    this.element.querySelector('button[type=submit]').addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      myDropzone.processQueue();
      //socket.emit('fileSubmitted');
    });
  }
};

// $(document).ready(function() {
//   document.getElementById('processing').style.visibility = 'hidden';
// });
// $(document).ready(function() {
//   var socket = io.connect('http://localhost:5001/');
//   socket.on('connect', function() {
//     console.log('connected')
//   });
//   socket.on('message', function(msg) {
//     console.log('Received message');
//   });
//   $('#submitmsg').on('click', function() {
//     socket.send($('#usermsg').val());
//     $('#usermsg').val('');
//   });
//   $('#test1').on('click', function() {
//     socket.send($('#test1').val());
//     $('#test1').val('');
//   });
// });
