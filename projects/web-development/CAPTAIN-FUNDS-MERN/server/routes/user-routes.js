import express from "express";
import UserModel from "../models/user-model.js";
import bcrypt from "bcryptjs";
import jwt from "jsonwebtoken";
import emailService from "../services/emailService.js";
const router = express.Router();

router.post("/register", async (req, res) => {
  try {
    const { name, email, password, isAdmin, isActive } = req.body;

    if (!name || !email || !password) {
      return res.status(400).json({ message: "Name, email and password are required" });
    }

    // check if user already exists
    const userExists = await UserModel.findOne({ email });
    if (userExists) {
      return res.status(400).json({ message: "User already exists" });
    }
//hash password
    const hashedPassword = await bcrypt.hash(password, 10);
    //create user
    const user = await UserModel.create({
      name,
      email,
      password: hashedPassword,
      isAdmin: Boolean(isAdmin),
      isActive: isActive !== undefined ? Boolean(isActive) : true,
    });
    if (!user) {
      return res.status(400).json({ message: "User creation failed" });
    }
    const { password: _pw, ...safeUser } = user.toObject ? user.toObject() : user;

    // Send welcome email asynchronously
    setImmediate(async () => {
      try {
        await emailService.sendWelcomeEmail(email, name);
        console.log('Welcome email sent to:', email);
      } catch (error) {
        console.error('Error sending welcome email:', error);
      }
    });

    res.status(201).json({ message: "User created successfully", user: safeUser });
  } catch (error) {
    res.status(500).json({ message: "User creation failed", error });
  }
});

router.post("/login", async (req, res) => {
  try {
    //get email and password from body
    const { email, password } = req.body;
    if (!email || !password) {
      return res.status(400).json({ message: "Email and password are required" });
    }
//find user
    const user = await UserModel.findOne({ email });
    if (!user) {
      return res.status(401).json({ message: "Invalid email or password" });
    }
//compare password
    const isPasswordValid = await bcrypt.compare(password, user.password);
    if (!isPasswordValid) {
      return res.status(401).json({ message: "Invalid email or password" });
    }
//remove password from user
    const { password: _pw, ...safeUser } = user.toObject ? user.toObject() : user;
    const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET, { expiresIn: "1h" });
    res.status(200).json({ message: "Login successful", user: safeUser, token });
  } catch (error) {
    res.status(500).json({ message: "Login failed", error });
  }
});
//get all users
router.get("/", async (req, res) => {
  try {
    const users = await UserModel.find().select("-password");
    res.status(200).json({ message: "Users fetched successfully", users });
  } catch (error) {
    res.status(500).json({ message: "Failed to fetch users", error });
  }
});
// get user by token (place before dynamic :id route)
router.get("/me", async (req, res) => {
  try {
    const authHeader = req.headers.authorization || "";
    const parts = authHeader.split(" ");
    if (parts.length !== 2 || parts[0] !== "Bearer") {
      return res.status(401).json({ message: "Authorization header missing or malformed" });
    }
    const token = parts[1];
    let decoded;
    try {
      decoded = jwt.verify(token, process.env.JWT_SECRET);
    } catch (e) {
      return res.status(401).json({ message: "Invalid or expired token" });
    }
    const user = await UserModel.findById(decoded.id).select("-password");
    if (!user) {
      return res.status(404).json({ message: "User not found" });
    }
    res.status(200).json({ message: "User fetched successfully", user });
  } catch (error) {
    res.status(500).json({ message: "Failed to fetch user", error });
  }
});
// get user by email (place before dynamic :id route)
router.get("/email/:email", async (req, res) => {
  try {
    const user = await UserModel.findOne({ email: req.params.email }).select("-password");
    if (!user) {
      return res.status(404).json({ message: "User not found" });
    }
    res.status(200).json({ message: "User fetched successfully", user });
  } catch (error) {
    res.status(500).json({ message: "Failed to fetch user", error });
  }
});
//get user by id
router.get("/:id", async (req, res) => {
  try {
    const user = await UserModel.findById(req.params.id).select("-password");
    if (!user) {
      return res.status(404).json({ message: "User not found" });
    }
    res.status(200).json({ message: "User fetched successfully", user });
  } catch (error) {
    res.status(500).json({ message: "Failed to fetch user", error });
  }
});
//update user
router.put("/:id", async (req, res) => {
  try {
    const update = { ...req.body };
    if (typeof update.password === "string" && update.password.length > 0) {
      update.password = await bcrypt.hash(update.password, 10);
    } else if (update.password !== undefined) {
      delete update.password;
    }
    const user = await UserModel.findByIdAndUpdate(req.params.id, update, { new: true, runValidators: true }).select("-password");
    if (!user) {
      return res.status(404).json({ message: "User not found" });
    }
    res.status(200).json({ message: "User updated successfully", user });
  } catch (error) {
    res.status(500).json({ message: "Failed to update user", error });
  }
});
//delete user
router.delete("/:id", async (req, res) => {
  try {
    const deleted = await UserModel.findByIdAndDelete(req.params.id);
    if (!deleted) {
      return res.status(404).json({ message: "User not found" });
    }
    res.status(200).json({ message: "User deleted successfully" });
  } catch (error) {
    res.status(500).json({ message: "Failed to delete user", error });
  }
});

export default router;