const fs = require('fs');
const http = require('http');
const qs = require('querystring');

const server = http.createServer((req, res) => {
  if (req.method === 'POST') {
    let body = '';
    req.on('data', chunk => {
      body += chunk.toString();
    });
    req.on('end', () => {
      const formData = qs.parse(body);
      const jsonData = JSON.stringify(formData);
      
      fs.writeFile('data.json', jsonData, 'utf8', (err) => {
        if (err) {
          console.error(err);
          res.writeHead(500, {'Content-Type': 'text/plain'});
          res.end('Internal Server Error');
          return;
        }
        console.log('Data saved successfully');
        res.writeHead(200, {'Content-Type': 'text/plain'});
        res.end('Data saved successfully');
      });
    });
  } else {
    res.writeHead(405, {'Content-Type': 'text/plain'});
    res.end('Method Not Allowed');
  }
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
