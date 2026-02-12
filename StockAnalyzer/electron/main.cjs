const { app, BrowserWindow } = require('electron')
const { spawn } = require('child_process')
const path = require('path')

let backendProcess

function createWindow() {
  const win = new BrowserWindow({
    width: 1000,
    height: 800
  })

 win.loadFile("index.html")
}

app.whenReady().then(() => {
// const backendPath = path.join(__dirname, "../backend/main.py")
// backendProcess = spawn("python", [backendPath])

  createWindow()
})

app.on('window-all-closed', () => {
  if (backendProcess) backendProcess.kill()
  if (process.platform !== 'darwin') app.quit()
})
