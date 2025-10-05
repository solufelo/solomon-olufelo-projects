import mongoose from "mongoose";
import dotenv from "dotenv";
dotenv.config();
const MONGODB_URL = process.env.MONGODB_URL;
const dbConfig = () => {
  mongoose.connect(MONGODB_URL);
};  

try {
  mongoose.connection.on("connected", () => {
    console.log("Connected to MongoDB");
  });
  mongoose.connection.on("error", (err) => {
    console.log("MongoDB connection error", err);
  });
} catch (error) {
  console.log("MongoDB connection error", error);
} finally {
  mongoose.connection.on("error", (err) => {
    console.log("MongoDB connection error", err);
  });
}

export default dbConfig;