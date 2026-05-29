const http = require("http");
const fs = require("fs");
const path = require("path");
const __dir = __dirname;

const server = http.createServer((req, res) => {
  let urlPath = req.url.split("?")[0];
  let filePath = urlPath === "/" ? "/index.html" : urlPath;
  filePath = path.join(__dir, filePath);
  const ext = path.extname(filePath);
  const mime = { ".html": "text/html", ".css": "text/css", ".js": "application/javascript", ".json": "application/json" };
  try {
    const content = fs.readFileSync(filePath);
    res.writeHead(200, { "Content-Type": mime[ext] || "text/plain" });
    res.end(content);
  } catch(e) {
    res.writeHead(404);
    res.end("Not Found");
  }
});
server.listen(8765, () => console.log("Server on http://localhost:8765"));
