console.log("Working");

const electron = require("electron");
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const path = require("path");
const url = require("url");

let win;

function createWindow() {
    win = new BrowserWindow();
    win.loadURL(
        url.format({
            pathname: path.join("HTML", "Login.htm"),
            protocol: "file",
            slashes: true
        })
    );

    win.webContents.openDevTools();
    win.on("closed", () => {
        win = null;
    });
}

app.on("ready", createWindow);

// for Mac OS
app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
});

app.on('activate', () => {
    if (win === null) {
        createWindow()
    }
});






// Your web app's Firebase configuration
// var firebaseConfig = {
//     apiKey: "AIzaSyD-MxwrL3tmrOnj-wi4_3FfL_fJU46Pn6E",
//     authDomain: "impulse2-89c2e.firebaseapp.com",
//     databaseURL: "https://impulse2-89c2e.firebaseio.com",
//     projectId: "impulse2-89c2e",
//     storageBucket: "impulse2-89c2e.appspot.com",
//     messagingSenderId: "646973830667",
//     appId: "1:646973830667:web:d31170631dd04854c5390e"
// };
// // Initialize Firebase
// firebase.initializeApp(firebaseConfig);

// var msgref = firebase.database().ref("form");
// $('#loginForm').submit(function (e) {
//     e.preventDefault();

//     var newmsg = msgref.push();
//     newmsg.set({
//         id: $('.ID').val(),
//         password: $('.Password').val(),
//     });

//     // $('#LoginForm')[0].reset();
// });