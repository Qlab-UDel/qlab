var PythonShell = require('python-shell');

PythonShell.run('ssl_042617.py', function (err) {
  if (err) throw err;
  console.log('finished');
});