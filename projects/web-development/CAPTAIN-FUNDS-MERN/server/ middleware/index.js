import jwt from "jsonwebtoken"

export const authMiddleware = async (req, res, next) => {           
    try {
        const cookies = req.cookies.token
        const decoded = jwt.verify(cookies, process.env.JWT_SECRET)
        req.user = decoded 
        next()
    } catch (error) {
        res.status(401).json({ message: "Unauthorized" })
    }
    
}