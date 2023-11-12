import express from "express";
import bodyParser from "body-parser";
import path from "path";

import connectDb from "./config/db.js";

import usersFile from "./api/users.js";
import loginFile from "./api/login.js";
import updatePostFile from "./api/updateposts.js";
import getPostFile from "./api/getposts.js";
import contactFile from "./api/contact.js";

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: false}));

connectDb();

app.get("/", (req, res)=> {
    res.send("this is home route of backend");
})

app.use("/api/users", usersFile); //this route is for registering new users
app.use("/api/login", loginFile); //this route is for logging in users
app.use("/api/updatepost", updatePostFile); //this route is for sending posts
app.use("/api/getposts", getPostFile); //this route is for gettin post
app.use("/api/contact", contactFile); //this route is for contact us file


// ... other app.use middleware 
app.use(express.static(path.join(__dirname, "client", "build")))

// ...
// Right before your app.listen(), add this:
app.get("*", (req, res) => {
    res.sendFile(path.join(__dirname, "client", "build", "index.html"));
});



var PORT = process.env.PORT || 5000;

app.listen(PORT, ()=> console.log("backend is running at)" + PORT ));